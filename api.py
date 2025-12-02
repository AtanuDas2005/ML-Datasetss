import requests
import pandas as pd

# API URL
url = "https://jsonplaceholder.typicode.com/users"

# Fetch data
response = requests.get(url)

# Convert JSON → Python object
data = response.json()

# Convert to DataFrame
df = pd.DataFrame(data)

# Display DataFrame
print(df.head())
