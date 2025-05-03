# app.py

import streamlit as st
from engine import SHLRecommendationEngine

st.set_page_config(page_title="SHL Assessment Recommendation Engine", layout="wide")
st.title("SHL Assessment Recommendation Engine")

@st.cache_resource
def load_engine():
    return SHLRecommendationEngine()

engine = load_engine()

query = st.text_input("Describe your hiring/assessment need:", "manager solution personality test")

col1, col2 = st.columns(2)
with col1:
    remote = st.selectbox("Remote Testing required?", ("Any", "Yes", "No"))
with col2:
    adaptive = st.selectbox("Adaptive/IRT required?", ("Any", "Yes", "No"))

if st.button("Get Recommendations"):
    remote_filter = None if remote == "Any" else remote
    adaptive_filter = None if adaptive == "Any" else adaptive
    results = engine.recommend(query, remote=remote_filter, adaptive=adaptive_filter)
    st.write("### Recommended Assessments")
    st.dataframe(results, use_container_width=True)
else:
    st.write("Enter your requirement and click **Get Recommendations**.")

st.markdown("---")
st.markdown("**Tip:** Try queries like `accounting`, `developer`, `manager`, `personality`, etc.")
