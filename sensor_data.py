import pandas as pd

# Load your CSV file
df = pd.read_csv("sensor_data_2025-03-01.csv")

# Display first 5 rows
print(df.head())

# Display summary
print(df.info())

# Display statistics
print(df.describe())
