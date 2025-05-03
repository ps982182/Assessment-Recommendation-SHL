# import pandas as pd

# def load_clean_shl_data(filepath="shl_job_solutions.csv"):
#     with open(filepath, encoding="utf-8") as f:
#         lines = [line.strip() for line in f if line.strip() and line.strip() != ",,,"]

#     header_indices = [i for i, line in enumerate(lines) if "Remote Testing" in line and "Test Type" in line]
#     dataframes = []

#     for idx in header_indices:
#         header = [h.strip() for h in lines[idx].split(",")]
#         next_idx = next((i for i in header_indices if i > idx), len(lines))
#         section_lines = lines[idx + 1:next_idx]

#         expanded_rows = []
#         for l in section_lines:
#             parts = l.split('... ')
#             for part in parts:
#                 row = [cell.strip() for cell in part.split(",")]
#                 if len(row) == len(header) and not any("..." in cell for cell in row):
#                     expanded_rows.append(row)

#         if expanded_rows:
#             df = pd.DataFrame(expanded_rows, columns=header)
#             first_col = df.columns[0]
#             df.rename(columns={first_col: "Job Solution"}, inplace=True)
#             dataframes.append(df)

#     if dataframes:
#         df = pd.concat(dataframes, ignore_index=True)
#         df = df[["Job Solution", "Remote Testing", "Adaptive/IRT", "Test Type"]]
#         for col in df.columns:
#             df[col] = df[col].astype(str).str.strip()
#         return df
#     else:
#         return pd.DataFrame(columns=["Job Solution", "Remote Testing", "Adaptive/IRT", "Test Type"])