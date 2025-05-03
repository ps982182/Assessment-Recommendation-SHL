import streamlit as st
import pandas as pd

df = pd.read_csv("shl_data.csv")

st.title("📊 SHL Assessment Recommendation Engine")

remote = st.checkbox("✅ Remote Testing Required", value=True)
adaptive = st.checkbox("✅ Adaptive/IRT Required", value=True)
keywords = st.text_input("🔎 Enter Job Role Keywords (comma-separated)")
test_types = st.text_input("🧠 Enter Desired Test Types (comma-separated, e.g. A, P, B)")

if st.button("🎯 Recommend Assessments"):
    result = df.copy()
    if remote:
        result = result[result["Remote Testing"] == "Yes"]
    if adaptive:
        result = result[result["Adaptive/IRT"] == "Yes"]
    if keywords:
        keyword_list = [k.strip() for k in keywords.split(",")]
        result = result[result["Job Solution"].str.contains('|'.join(keyword_list), case=False)]
    if test_types:
        type_list = [t.strip() for t in test_types.split(",")]
        result = result[result["Test Type"].apply(lambda x: any(t in x for t in type_list))]
    
    st.write("### 🔍 Recommended Job Solutions:")
    st.dataframe(result)
