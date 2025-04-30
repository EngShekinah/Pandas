import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
try:
    df = pd.read_csv("todays_data.csv")
    print("Dataset loaded successfully!")
except FileNotFoundError:
    print("Error: The file 'todays_data.csv' was not found.")
    exit()
except Exception as e:
    print(f"An error occurred while loading the dataset: {e}")
    exit()

# Display the first few rows of the dataset
print("\nFirst 5 rows of the dataset:")
print(df.head())

# Explore the structure of the dataset
print("\nDataset information:")
print(df.info())

# Check for missing values
print("\nMissing values:")
print(df.isnull().sum())

# Clean the dataset by filling missing values in 'Academic Level' with 'Unknown'
df['Academic Level'] = df['Academic Level'].fillna('Unknown')

# Verify that missing values have been handled
print("\nMissing values after handling:")
print(df.isnull().sum())

# Basic statistics of numerical columns (there are no numerical columns in this dataset but i will compute value counts)
print("\nValue counts for Gender:")
print(df['Gender'].value_counts())

print("\nValue counts for Academic Level:")
print(df['Academic Level'].value_counts())

# Groupings on a categorical column and compute value counts
gender_academic = df.groupby('Gender')['Academic Level'].value_counts()
print("\nAcademic Level distribution by Gender:")
print(gender_academic)

# Data Visualization
# 1. Bar chart showing the distribution of Gender
plt.figure(figsize=(8, 6))
sns.countplot(data=df, x='Gender')
plt.title('Distribution of Gender')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.show()

# 2. Bar chart showing the distribution of Academic Level
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='Academic Level')
plt.title('Distribution of Academic Level')
plt.xlabel('Academic Level')
plt.ylabel('Count')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# 3. Stacked bar chart of Gender by Academic Level
gender_academic_pivot = df.groupby(['Academic Level', 'Gender']).size().unstack()
gender_academic_pivot.plot(kind='bar', stacked=True, figsize=(10, 6))
plt.title('Gender Distribution by Academic Level')
plt.xlabel('Academic Level')
plt.ylabel('Count')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# 4. Pie chart of Academic Level distribution
academic_counts = df['Academic Level'].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(academic_counts, labels=academic_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Distribution of Academic Levels')
plt.tight_layout()
plt.show()

# Findings and Observations
print("\nFindings and Observations:")
print("- The dataset contains demographic information of individuals from Kenya.")
print("- The majority of individuals in the dataset identify as male.")
print("- Most of the individuals are UnderGraduates.")
print("- There are some missing values in the 'Academic Level' column, which have been filled with 'Unknown'.")
print("- The visualizations provide a clear overview of the distribution of gender and academic levels within the dataset.")