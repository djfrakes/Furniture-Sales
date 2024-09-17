import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = '/Users/daxjulian/Desktop/Furniture.csv'  # Make sure this is the correct path to your file
data = pd.read_csv(file_path)

#Calculating the stats 
summary_stats= data[['price', 'sales', 'profit_margin', 'inventory', 'revenue']].describe()

print(summary_stats)

# Filter rows where revenue is less than 0
loss_products = data[data['revenue'] < 0]
# Display relevant columns to examine the loss-making products
loss_products[['category', 'price', 'sales', 'revenue']]

print(loss_products)

# Select only numerical columns for correlation
numeric_data = data.select_dtypes(include=['float64', 'int64'])

# Compute the correlation matrix
correlation_matrix = numeric_data.corr()

# Plot the heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Heatmap')
plt.show()  

# Create a scatter plot: price vs. sales
plt.figure(figsize=(8, 6))
plt.scatter(data['price'], data['sales'], alpha=0.5)

# Add labels and title
plt.title('Scatter Plot of Price vs Sales')
plt.xlabel('Price')
plt.ylabel('Sales')

# Show the plot
plt.show()

# Calculate the correlation between price and sales
correlation = data['price'].corr(data['sales'])
print(f'Correlation between Price and Sales: {correlation}')


# Create a scatter plot: discount_percentage vs. sales
plt.figure(figsize=(8, 6))
plt.scatter(data['discount_percentage'], data['sales'], alpha=0.5)

# Add labels and title
plt.title('Scatter Plot of Discount_percentage vs Sales')
plt.xlabel('Discount_percentage')
plt.ylabel('Sales')

# Show the plot
plt.show()

# Calculate the correlation between price and sales
correlation = data['discount_percentage'].corr(data['sales'])
print(f'Correlation between Discount_Percentage and Sales: {correlation}')