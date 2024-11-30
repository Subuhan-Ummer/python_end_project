# python_end_project

# **Employee Data Analysis Project**

## **Project Overview**
This project involves analyzing an employee dataset with 458 entries across 9 columns. The primary objective is to preprocess the data, perform analysis, and provide visual insights to uncover trends and patterns. Tasks include handling missing values, analyzing team and position distributions, salary expenditure, and age-salary correlation.

---

## **Preprocessing Steps**
1. **Height Column**: Replaced inconsistent height values with random integers between 150 and 180.
2. **Handling Missing Values**:
   - **College**: Filled missing values with "Unknown."
   - **Salary**: Replaced missing values with the median salary.

---

## **Analysis Tasks**

### **1. Distribution of Employees Across Teams**
- Identified the number of employees per team and calculated the percentage split relative to the total.
- **Insight**: The New Orleans Pelicans have the most employees (19), while the Orlando Magic and Minnesota Timberwolves have the least (14).
- **Visualization**: Bar chart and pie chart.

### **2. Employee Segregation by Position**
- Analyzed the count of employees per position.
- **Insight**: The "SG" position  has the highest count (102), followed by "PF" at 100. The least common position is "C"  with 79 employees.
- **Visualization**: Bar chart.

### **3. Predominant Age Group**
- Grouped employees into age categories: 20-29, 30-39, etc.
- **Insight**: The 20-29 age group dominates with 334 employees, followed by 30-39 (119 employees). Only 3 employees fall into the 40-49 group.
- **Visualization**: Histogram.

### **4. Salary Expenditure by Team and Position**
- Calculated total salary expenditure for each team and position.
- **Insight**:
  - **Team**: Cleveland Cavaliers have the highest salary expenditure ($109,824,875.0), while Philadelphia 76ers have the lowest ($33,829,080.0).
  - **Position**: "C" incur the highest expenditure ($466,377,332.0), while "SG" have the lowest ($405,484,816.0).
- **Visualization**: Stacked bar chart.

### **5. Correlation Between Age and Salary**
- Analyzed the relationship between age and salary using correlation.
- **Insight**: A positive correlation (0.21) indicates older employees generally earn more, though other factors also influence salary.
- **Visualization**: Scatter plot with trendline.

---

## **Data Story**

1. The **New Orleans Pelicans** have the largest number of employees, totaling **19**, making them the most staffed team. On the other hand, the **Orlando Magic** and **Minnesota Timberwolves** have the smallest teams, each employing only **14** members.
   
2. The majority of employees hold the positions of **SG** and **PF**, with **102** and **100** employees respectively. The position with the least number of employees is **C**, which has **79** members.
   
3. The predominant age group among employees is **20-29 years**, encompassing **334** individuals, followed by **30-39 years** with **119** individuals. The age group of **40-49 years** is the least represented, with only **3** employees.

4. The **Cleveland Cavaliers** lead in total salary expenditure, with a staggering **$109,824,875.0**, highlighting their investment in talent. In contrast, the **Philadelphia 76ers** have the lowest salary expenditure at **$33,829,080.0**, suggesting a different strategic approach.
   
5. When examining positions, the **C** role incurs the highest total salary at **$466,377,332.0**, reflecting the importance and value placed on this position. Conversely, the **SG** position has the lowest total salary expenditure at **$405,484,816.0**.

6. There is a **positive correlation (0.21)** between age and salary. This indicates that older employees generally earn more, though the correlation is moderate, suggesting that while age influences salary, other factors also play a significant role.

---

## **Visualizations**
Each analysis task is accompanied by an appropriate visualization:
- **Bar charts**: Team and position distributions.
- **Pie chart**: Team percentage splits.
- **Histogram**: Age group distribution.
- **Stacked bar chart**: Salary expenditure by team and position.
- **Scatter plot**: Age vs. Salary correlation.

---

## **Files in the Repository**
1. **`Python_End_Project.py`**: Contains the complete code, analysis, and visualizations.
2. **Dataset**: `myexcel - myexcel.csv` (uploaded dataset for analysis).
3. **Screenshots**: Screenshots of visualizations included for reference.

---


