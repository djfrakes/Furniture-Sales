# Furniture-Sales

## Table of Contents

- [Project Overview](#project-overview)
- [Dataset](#dataset)
- [Results](#results)

### Project Overview
This project performs an exploratory data analysis (EDA) of a furniture sales dataset. The goal is to uncover insights such as summary statistics, correlations between different variables, and identifying products that result in a loss. Key visualizations like scatter plots and a heatmap are generated to better understand the relationships between different features like price, sales, and discount_percentage.

### Tools
- Python

### Dataset

The dataset used in this analysis is sourced from Kaggle.
Source: Kaggle - Furniture Sales Dataset https://www.kaggle.com/datasets/rajagrawal7089/furniture-sales-data

Make sure to use the Furniture.csv dataset, which contains various attributes of furniture products such as:
- price: Price of the product
- sales: Number of units sold
- profit_margin: Percentage profit margin on the product
- inventory: Current stock of the product
- revenue: Total revenue from the product
- discount_percentage: Discount percentage on the product

Additional categorical features like category, location, and season.
### Features
- Summary Statistics: Calculate and display key statistics (mean, median, quartiles, etc.) for the numerical columns such as price, sales, profit_margin, inventory, and revenue.
- Identify Loss-Making Products: Filters products where revenue is negative and displays relevant information about these products.
- Correlation Analysis: Computes and visualizes correlations between numerical variables in the dataset using a heatmap.
- Scatter Plots: Visualizes relationships between variables like price vs sales and discount_percentage vs sales using scatter plots.
- Correlation Calculation: Calculates the correlation coefficient for price vs sales and discount_percentage vs sales to assess the strength of these relationships.

### Requirements
Before running the analysis, ensure you have the following Python libraries installed:
- pandas
- matplotlib
- seaborn
### Analysis Breakdown
#### Summary Statistics
The script calculates key summary statistics for the numerical columns such as price, sales, profit_margin, inventory, and revenue. This helps in understanding the overall distribution of these variables.

#### Identifying Loss-Making Products
The code filters the products with negative revenue, giving you a clear view of products that are operating at a loss.

#### Correlation Analysis and Heatmap
A correlation matrix is computed to identify relationships between numerical variables such as price, sales, and profit_margin. A heatmap is generated to visualize the strength of these correlations.

#### Scatter Plots
Price vs Sales: A scatter plot to visualize the relationship between price and sales.
Discount Percentage vs Sales: A scatter plot to analyze the effect of discounts on sales.

#### Example Output
1. Scatter Plot: Price vs Sales
![Scatter_Plot](https://github.com/user-attachments/assets/79d11238-4ae2-44ef-a7dc-6e47ab55d579)

2. Correlation Heatmap
![Heatmap](https://github.com/user-attachments/assets/42d5e6cd-d5af-4fcb-ac80-b5c1cdbeb4e5)

### Results
1. The scatter plot of price vs sales shows no strong correlation (correlation coefficient ~ -0.006).
2. There is also minimal correlation between discount_percentage and sales.
3. Some products are running at a loss, as identified through negative revenue values.


