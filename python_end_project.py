# -*- coding: utf-8 -*-
"""Python_End_Project.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1IledtavpeibnRnVK8wn2XYuTweRFoC_7
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#loading the dataset
df = pd.read_csv('/content/myexcel - myexcel.csv.csv')

#displaying first 5 rows of data
df.head()

"""#**Preprocessing**
---
Correcting the data in the "height" column by replacing it with random numbers between 150 and 180.
"""

#replacing 'Height' column with random values between 150 and 180.
df['Height'] = np.random.randint(150, 181, size=len(df))

df

#checking null values
df.info()

#checking the count of null values
df.isna().sum()

"""here seems that the 'College' column has 84 null values and column 'Salary' has 11 null values. Rather than dropping null values, i'm going to replace it with 'Unknown' in 'College' column and median of salary in the 'Salary' Column where null values exists."""

#handling missing values in the 'College' column using 'Unknown'.
df['College'] = df['College'].fillna('Unknown')

#handling missing values in the 'Salary' column using median of salary.
df['Salary'] = df['Salary'].fillna(df['Salary'].median())

#checking the dataframe for verifying missing or inconsistent values.
df.info()

"""#**Analysis Tasks**

Task 1 :  Distribution of employees across each team and calculate the percentage split relative to the total number of employees.
"""

#number of employees per team and percentage
team_distribution = df['Team'].value_counts()
team_percentage = (team_distribution / len(df)) * 100

#displaying the results
print('Employee Distribution by Team : ')
print(team_distribution)
print('\nPercentage Split by Team : ')
print(team_percentage)

#visualization of Distribution of Employees Across Teams.
team_distribution.plot(kind='bar', figsize=(10,6), color='skyblue')
plt.title('Distribution of Employees Across Teams')
plt.xlabel('Team')
plt.ylabel('Number of Employees')
plt.show()

#visualization of percentage split.
plt.figure(figsize=(8,8))
team_percentage.plot(kind='pie', autopct='%1.1f%%', startangle=140, colormap='tab20')
plt.title('Percentage Split of Employees by Team')
plt.ylabel('')
plt.show()

"""Task 2 : Segregate employees based on their positions with company."""

#number of employees per position
position_distribution = df['Position'].value_counts()

#displaying the results
print("Employee Distribution by Position")
print(position_distribution)

#visualization
position_distribution.plot(kind='bar', figsize=(10, 6), color='lightgreen')
plt.title('Distribution of Employees by Position')
plt.xlabel('Position')
plt.ylabel('Number of Employees')
plt.show()

"""Task 3 : Predominant age group among employees."""

#defining age groups
bins = [20, 30, 40, 50, 60]
labels = ['20-29', '30-39', '40-49', '50-59']
df['Age_Group'] = pd.cut(df['Age'], bins=bins, labels=labels, right=False)

#calculating the age group distribution
age_group_distribution = df['Age_Group'].value_counts()

#dsiplaying the results
print("Age Group Distribution")
print(age_group_distribution)

#visualization

plt.figure(figsize=(10, 6))
plt.hist(df['Age'], bins=bins, color='orange', edgecolor='black')
plt.title("Age Group Distribution")
plt.xlabel("Age")
plt.ylabel("Number of Employees")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

"""Task 4 : Team and Position having highest salary expenditure."""

#salary expenditure by team
team_salary = df.groupby('Team')['Salary'].sum().sort_values(ascending=False)

#salary expenditure by position
position_salary = df.groupby('Position')['Salary'].sum().sort_values(ascending=False)

#displaying the results
print("Total Salary by Team : ")
print(team_salary)
print("\nTotal Salary by Position : ")
print(position_salary)

# Group by Team and Position to get the sum of salaries
salary_data = df.groupby(['Team', 'Position'])['Salary'].sum().unstack()

# Stacked Bar Chart
salary_data.plot(kind='bar', stacked=True, figsize=(12, 8), colormap='tab20')
plt.title('Salary Expenditure by Team and Position')
plt.xlabel('Team')
plt.ylabel('Total Salary')
plt.legend(title='Position', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

team_salary.plot(kind='bar', figsize=(10, 6), color='purple')
plt.title('Total Salary Expenditure by Team')
plt.xlabel('Team')
plt.ylabel('Total Salary')
plt.show()

position_salary.plot(kind='bar', figsize=(10, 6), color='red')
plt.title('Total Salary Expenditure by Position')
plt.xlabel("Position")
plt.ylabel("Total Salary")
plt.show()

"""Task 5 : Correlation between Age and Salary."""

#correlation
correlation = df['Age'].corr(df['Salary'])
print(f"Correlation between Age and Salary : {correlation:.2f}")

#visualization with trendline
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Age', y='Salary', color='teal')
sns.regplot(data=df, x='Age', y='Salary', scatter=False, color='red')
plt.title("Correlation between Age and Salary")
plt.xlabel("Age")
plt.ylabel("Salary")
plt.show()

"""#Data Story


> 1. The New Orleans Pelicans is having the largest number of employees, totaling 19, making them the most staffed team. On the other hand, the Orlando Magic and Minnesota Timberwolves have the smallest teams, each employing only 14 members.

> 2. The majority of employees hold the positions of 'SG' and 'PF', with 102 and 100 employees respectively. The position with the least number of employees is 'C', which has 79 members.

> 3. The predominant age group among employees is 20-29 years, encompassing 334 individuals, followed by 30-39 years with 119 individuals. The age group of 40-49 years is the least represented, with only 3 employees.

> 4. The Cleveland Cavaliers lead in total salary expenditure, with a staggering 109,824,875.0, highlighting their investment in talent. In contrast, the Philadelphia 76ers have the lowest salary expenditure at 33,829,080.0, suggesting a different strategic approach.

> 5. When examining positions, the 'C' role incurs the highest total salary at 466,377,332.0, reflecting the importance and value placed on this position. Conversely, the 'SG' position has the lowest total salary expenditure at 405,484,816.0.

> 6. There is a positive correlation (0.21) between age and salary. This indicates that older employees generally earn more, though the correlation is moderate, suggesting that while age influences salary, other factors also play a significant role.
"""

