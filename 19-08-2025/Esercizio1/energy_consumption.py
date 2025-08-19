import pandas as pd
import numpy as np

# Read dataset
df = pd.read_csv("./AEP_hourly.csv")

# Convert to datetime
df["Datetime"] = pd.to_datetime(df["Datetime"])

# Compute daily average
df["Daily_Mean"] = df.groupby(df["Datetime"].dt.date)["AEP_MW"].transform("mean")

# Difference with respect to average
df["Delta"] = df["AEP_MW"] - df["Daily_Mean"]

# Status over, under, equal to average
df["Status"] = np.select(
    [df["Delta"] > 0, df["Delta"] < 0],
    ["Above Average", "Below Average"],
    default="Equal to Average"
)

# Save results to a new CSV file
df.to_csv("AEP_hourly_tagged.csv", index=False)

# Show the first 10 rows of the DataFrame
print(df.head(10))
