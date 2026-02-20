import pandas as pd
import glob as glob
import numpy as np

# load and concatenate all trials
files = glob.glob("trials/a3*.csv")

# combine all trials
df = pd.concat([pd.read_csv(f) for f in files])

# calculate error using Cleveland & McGill's formula
df["Error"] = np.log2(np.abs(df["ReportedPercent"] - df["TruePercent"]) + 0.125)
df["Error"] = df["Error"].where(df["ReportedPercent"] != df["TruePercent"], 0)

# save combined data as a master file
df.to_csv("trials/master.csv", index=False)

# report file summary
print(f"Combined {len(files)} files, {len(df)} total trials ")
