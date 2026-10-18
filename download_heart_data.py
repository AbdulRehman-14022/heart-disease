from pathlib import Path
import pandas as pd
from ucimlrepo import fetch_ucirepo

OUT = Path(__file__).resolve().parent / "heart_cleveland.csv"
heart_disease = fetch_ucirepo(id=45)
X = heart_disease.data.features.copy()
y = heart_disease.data.targets.copy()

# UCI's target is 0 to 4; convert it to binary disease/no-disease.
target_col = y.columns[0]
df = X.copy()
df["target"] = pd.to_numeric(y[target_col], errors="coerce")
df = df.dropna(subset=["target"])
df["target"] = (df["target"] > 0).astype(int)

df.to_csv(OUT, index=False)
print(f"Saved {len(df)} rows to {OUT}")
