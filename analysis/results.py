import pandas as pd
import numpy as np

# load data
df = pd.read_csv("trials/master.csv")

# compute avg absolute error by vis type and sort from lowest to highest error
avg_error = df.groupby('Vis')['Error'].apply(lambda x: x.abs().mean()).sort_values()

# report avg error by vis type
print("Average Error per visualization:")
for vis, err in avg_error.items():
    print(f"{vis}: {err:.4f}")
