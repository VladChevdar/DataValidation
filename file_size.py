filename = 'employees.csv'

# Count bytes
with open(filename, 'rb') as f:
    num_bytes = len(f.read())

# Count records
import pandas as pd
df = pd.read_csv(filename)
num_records = len(df)

print(f"Number of bytes: {num_bytes}")
print(f"Number of records: {num_records}")