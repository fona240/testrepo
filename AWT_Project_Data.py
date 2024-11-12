
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file into a pandas DataFrame
df = pd.read_csv("C:/Users/Funda/Downloads/AWT/AWT/sand.csv", low_memory=False)

# Specify the columns to keep
columns_to_keep = ['type', 'code', 'fatal', 'message', 'metricType']

# Specify the column to search for the value "ErrorMetric"
search_column = 'metricType' 
search_value = 'ErrorMetric'

# Filter rows where the specified column contains the search value
filtered_df = df[df[search_column] == search_value][columns_to_keep]

# Filter the DataFrame to keep only the specified columns
"""filtered_df = df[columns_to_keep]"""

# Remove rows with any missing values
"""filtered_df = filtered_df.dropna(how='all')"""

# filtered DataFrame to a new CSV file
"""filtered_df.to_csv("C:/Users/Funda/Downloads/AWT/AWT/Error_filtered_sand.csv", index=False)

# Save the DataFrame to an Excel file
filtered_df.to_excel("C:/Users/Funda/Downloads/AWT/AWT/Error_filtered_sand.xlsx", index=False)"""

# Count the occurrences of each error type in bar plot
error_counts = filtered_df['type'].value_counts()
plt.figure(figsize=(10, 6))
sns.barplot(x=error_counts.index, y=error_counts.values, palette="viridis")
plt.xlabel('Error Type')
plt.ylabel('Frequency')
plt.title('Frequency of Each Error Type')
plt.xticks(rotation=45)
plt.show()

# Count the number of fatal vs non-fatal errors in pie chart
fatal_counts = filtered_df['fatal'].value_counts()
plt.figure(figsize=(6, 6))
plt.pie(fatal_counts, labels=['Non-Fatal', 'Fatal'], autopct='%1.1f%%', startangle=90, colors=['skyblue', 'salmon'])
plt.title('Distribution of Fatal vs Non-Fatal Errors')
plt.show()