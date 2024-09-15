import pandas as pd

# Define data as a dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
# Create a DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
print(df)
df.to_csv('output.csv', index=False)
