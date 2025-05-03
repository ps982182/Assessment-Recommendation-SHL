# engine.py

import pandas as pd

class SHLRecommendationEngine:
    def __init__(self, csv_path="shl_job_solutions.csv"):
        self.df = pd.read_csv(csv_path)
        # Standardize column names
        self.df.columns = [c.strip().replace(" ", "_").replace("/", "_") for c in self.df.columns]
        # Fill NaNs
        self.df = self.df.fillna("")
        # Build a search blob for each row
        self.df["search_blob"] = (
            self.df["Job_Solution"].str.lower() + " " +
            self.df["Test_Type"].str.lower().str.replace(",", " ")
        )

    def recommend(self, query, top_n=5, remote=None, adaptive=None):
        query = query.lower()
        # Simple scoring: count how many words from query appear in search_blob
        query_words = query.split()
        def score(row):
            return sum(qw in row for qw in query_words)
        self.df["score"] = self.df["search_blob"].apply(score)
        results = self.df[self.df["score"] > 0]
        # Apply optional filters
        if remote is not None:
            results = results[results["Remote_Testing"].str.lower() == remote.lower()]
        if adaptive is not None:
            results = results[results["Adaptive_IRT"].str.lower() == adaptive.lower()]
        # Fallback: if no results, show top_n random
        if results.empty:
            results = self.df.sample(top_n)
        else:
            results = results.sort_values("score", ascending=False)
        return results.head(top_n)[["Job_Solution", "Remote_Testing", "Adaptive_IRT", "Test_Type"]].reset_index(drop=True)

# For quick testing
if __name__ == "__main__":
    engine = SHLRecommendationEngine()
    print(engine.recommend("manager solution"))
