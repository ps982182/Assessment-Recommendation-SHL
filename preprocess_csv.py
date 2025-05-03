# import pandas as pd
# import re

# def preprocess_and_save(filepath="shl_job_solutions.csv", output="cleaned_data.parquet"):
#     with open(filepath, encoding="utf-8") as f:
#         lines = [line.strip() for line in f if line.strip() and line.strip() != ",,,"]
    
#     header_indices = [i for i, line in enumerate(lines) if "Remote Testing" in line and "Test Type" in line]
#     dataframes = []

#     for idx in header_indices:
#         header = [h.strip() for h in lines[idx].split(",")]
#         next_idx = next((i for i in header_indices if i > idx), len(lines))
#         section_lines = lines[idx + 1:next_idx]
#         rows = []

#         for line in section_lines:
#             parts = line.split('... ')
#             for part in parts:
#                 row = [cell.strip() for cell in part.split(",")]
#                 if len(row) == len(header) and "..." not in part:
#                     rows.append(row)

#         if rows:
#             df = pd.DataFrame(rows, columns=header)
#             df.rename(columns={df.columns[0]: "Job Solution"}, inplace=True)
#             dataframes.append(df)

#     if dataframes:
#         df = pd.concat(dataframes, ignore_index=True)
#         df = df[["Job Solution", "Remote Testing", "Adaptive/IRT", "Test Type"]]
#         for col in df.columns:
#             df[col] = df[col].astype(str).str.strip()
#         df["job_lower"] = df["Job Solution"].str.lower()
#         df["test_type_lower"] = df["Test Type"].str.lower()
#         df.to_parquet(output, index=False)
#         print(f"Cleaned data saved to {output}")
#     else:
#         print("No data to save.")

# preprocess_and_save()
