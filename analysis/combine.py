import pandas as pd
import glob as glob
import numpy as np


files = glob.glob("trials/a3*.csv")

df = pd.concat([pd.read_csv(f) for f in files])

df["Error"] = np.log2(np.abs(df["ReportedPercent"]/ df["TruePercent"]) + 0.125)
df["Error"] = df["Error"].where(df["ReportedPercent"] != df["TruePercent"], 0)

df.to_csv("trials/master.csv", index=False)

print(f"Combined {len(files)} files, {len(df)} total trials ")
