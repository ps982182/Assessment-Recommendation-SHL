# import csv

# with open("shl_job_solutions.csv", "r", encoding="utf-8") as infile, open("shl_job_solutions_yes.csv", "w", encoding="utf-8", newline="") as outfile:
#     reader = csv.reader(infile)
#     writer = csv.writer(outfile)
#     header = next(reader)
#     writer.writerow(header)
#     for row in reader:
#         # Replace only the 2nd and 3rd columns if they are "No"
#         if len(row) >= 4:
#             row[1] = "Yes"
#             row[2] = "Yes"
#         writer.writerow(row)

# print("Done! All 'No' replaced with 'Yes' in the relevant columns.")
