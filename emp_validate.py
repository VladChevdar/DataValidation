import pandas as pd

# Load data
df = pd.read_csv('employees.csv')
known_eids = set(df['eid'])
city_counts = df['city'].value_counts()
df = df.dropna(subset=['salary'])

# Calculate
num_null_names = df['name'].isnull().sum()
num_hired_before_2015 = (df['hire_date'] < '2015-01-01').sum()
num_hired_before_birth = (df['hire_date'] < df['birth_date']).sum()
num_unknown_managers = ((df['reports_to'].notnull()) & (~df['reports_to'].isin(known_eids))).sum()
num_one_emp_cities = len(city_counts[city_counts == 1])

# Output
print(f"Employees with missing name: {num_null_names}")
print(f"Employees hired before 2015: {num_hired_before_2015}")
print(f"Employees hired before their birth date: {num_hired_before_birth}")
print(f"Employees with unknown manager: {num_unknown_managers}")
print(f"Number of cities with only one employee: {num_one_emp_cities}")

# Histogram
df = df[(df['salary'] >= 50000) & (df['salary'] <= 200000)]
plt.figure(figsize=(10, 5))
sns.histplot(df['salary'], kde=True, color='skyblue', bins=10, edgecolor='black')
plt.title('Distribution of Salaries (Filtered)')
plt.xlabel('Salary')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()
