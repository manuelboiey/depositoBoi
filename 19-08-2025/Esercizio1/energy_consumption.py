import pandas as pd
import numpy as np

# Read dataset
df = pd.read_csv("AEP_hourly.csv")

# Convert to datetime
df["Datetime"] = pd.to_datetime(df["Datetime"])

# Add column only of the data
df["Date"] = df["Datetime"].dt.date

# Compute daily average
daily_mean = df.groupby("Date")["AEP_MW"].mean().rename("Daily_Mean")

# Merge daily average with original DataFrame
df = df.merge(daily_mean, on="Date")

# Difference with respect to average
df["Delta"] = df["AEP_MW"] - df["Daily_Mean"]

# Status over, under, equal to average
df["Status"] = np.select(
    [df["Delta"] > 0, df["Delta"] < 0],
    ["Above Average", "Below Average"],
    default="Equal to Average"
)

df.drop(columns=["Date", "Daily_Mean"], inplace=True)

# Save results to a new CSV file
df.to_csv("AEP_hourly_tagged.csv", index=False)

# Show the first 10 rows of the DataFrame
print(df.head(10))
