import pandas as pd

# Load dataset
df = pd.read_csv("shl_data.csv")

# User input (can later come from UI)
user_input = {
    "remote": True,
    "adaptive": True,
    "keywords": ["Analyst", "Bank"],
    "test_types": ["A", "P"]
}

# Filter logic
filtered = df.copy()

if user_input["remote"]:
    filtered = filtered[filtered["Remote Testing"] == "Yes"]
if user_input["adaptive"]:
    filtered = filtered[filtered["Adaptive/IRT"] == "Yes"]
if user_input["keywords"]:
    filtered = filtered[filtered["Job Solution"].str.contains('|'.join(user_input["keywords"]), case=False)]
if user_input["test_types"]:
    filtered = filtered[filtered["Test Type"].apply(lambda x: any(t in x for t in user_input["test_types"]))]

print(filtered[["Job Solution", "Test Type"]])
