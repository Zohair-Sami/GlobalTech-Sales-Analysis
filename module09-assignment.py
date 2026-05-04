# Module 9 Assignment: Introduction to Data Analysis with Pandas
# GlobalTech Sales Analysis

# Import required libraries
import pandas as pd
import numpy as np

print("=" * 60)
print("GLOBALTECH QUARTERLY SALES ANALYSIS")
print("=" * 60)

# TODO 1: Load and Explore the Dataset

from io import StringIO

csv_content = """Date,Region,Store,Category,Product,Units,Unit_Price,Total_Sales,Promotion
2024-01-15,North America,NA001,Smartphones,PhoneX,12,899.99,10799.88,No
2024-01-18,Europe,EU002,Computers,LaptopPro,8,1299.99,10399.92,Yes
2024-01-20,Asia,AS001,Audio,WirelessEarbuds,25,149.99,3749.75,No
2024-01-22,North America,NA002,Wearables,SmartWatch,15,249.99,3749.85,No
2024-01-25,Latin America,LA001,Smartphones,PhoneX,7,899.99,6299.93,Yes
2024-01-27,Europe,EU001,Accessories,PhoneCase,35,24.99,874.65,No
2024-01-30,Asia,AS002,Smartphones,PhoneSE,18,499.99,8999.82,No
2024-02-02,North America,NA001,Computers,LaptopPro,6,1299.99,7799.94,No
2024-02-05,Europe,EU002,Wearables,SmartWatch,20,249.99,4999.80,Yes
2024-02-08,North America,NA003,Audio,WirelessEarbuds,30,149.99,4499.70,Yes
2024-02-10,Asia,AS001,Accessories,ChargingCable,45,19.99,899.55,No
2024-02-12,Latin America,LA001,Computers,TabletBasic,12,399.99,4799.88,No
2024-02-15,North America,NA002,Smartphones,PhoneSE,14,499.99,6999.86,No
2024-02-18,Europe,EU001,Audio,BlueSpeaker,22,79.99,1759.78,Yes
2024-02-20,Asia,AS002,Wearables,FitnessTracker,28,129.99,3639.72,No
2024-02-22,North America,NA001,Accessories,PhoneCase,50,24.99,1249.50,Yes
2024-02-25,Latin America,LA002,Smartphones,PhoneX,9,,8099.91,No
2024-02-28,Europe,EU002,Computers,LaptopBasic,10,899.99,8999.90,No
2024-03-02,North America,NA003,Wearables,FitnessTracker,,129.99,2599.80,Yes
2024-03-05,Asia,AS001,Smartphones,PhoneSE,15,499.99,7499.85,No
2024-03-08,Europe,EU001,Accessories,ChargingCable,60,19.99,1199.40,Yes
2024-03-10,North America,NA002,Computers,TabletPro,7,599.99,4199.93,No
2024-03-12,Latin America,LA001,Audio,WirelessEarbuds,18,149.99,2699.82,No
2024-03-15,North America,NA001,Wearables,SmartWatch,12,249.99,2999.88,No
2024-03-18,Europe,EU002,Smartphones,PhoneX,11,899.99,9899.89,Yes
2024-03-20,Asia,AS002,Computers,LaptopPro,6,1299.99,7799.94,No
2024-03-22,North America,NA001,Audio,BlueSpeaker,25,79.99,1999.75,No
2024-03-25,Latin America,LA002,Accessories,PhoneCase,40,,999.60,No
"""
sales_data_csv = StringIO(csv_content)

# 1.1 Load the dataset and store it in a DataFrame called 'sales_df'

sales_df = pd.read_csv(sales_data_csv)

# 1.2 Display the first 5 rows of the dataset
print(sales_df.head())

# 1.3 Display basic
sales_df.info()

# 1.4 Get dimensions of DataFrame
print(sales_df.shape)

# 1.5 Display summary statistics for numerical columns using describe()
print(sales_df.describe())

# TODO 2: Column Selection and Basic Analysis

# 2.1 Select and display only the 'Product', 'Units', and 'Total_Sales columns
print(sales_df[["Product", "Units", "Total_Sales"]])

# 2.2 Calculate the total units sold across all records
total_units = sales_df["Units"].sum()
print(total_units)
    
# 2.3 Calculate the total sales amount across all records
total_revenue = sales_df["Total_Sales"].sum()
print(total_revenue)

# 2.4 Calculate the average unit price per product
avg_unit_price = sales_df["Unit_Price"].mean()
print(avg_unit_price)

# TODO 3: Row Selection and Filtering

# 3.1 Select sales from North America region only
na_sales = sales_df[sales_df["Region"] == "North America"]
print(na_sales)

# 3.2 Select sales where Units sold is greater than 20
high_volume_sales = sales_df[sales_df["Units"] > 20]
print(high_volume_sales)

# 3.3 Select sales of the 'PhoneX' product that were on promotion
phonex_promo = sales_df[
    (sales_df["Product"] == "PhoneX") &
    (sales_df["Promotion"] == "Yes")
    ]
print(phonex_promo)

# 3.4 Select sales from February 2024
feb_sales = sales_df[sales_df["Date"].str.startswith("2024-02")]

# TODO 4: Advanced Filtering and Analysis

# 4.1 Find the product with highest total sales
best_product = sales_df.groupby("Product")["Total_Sales"].sum().idxmax()
print(best_product)

# 4.2 Calculate total sales by region and sort in descending order
sales_by_region = sales_df.groupby("Region")["Total_Sales"].sum().sort_values(ascending=False)
print(sales_by_region)

# 4.3 Calculate average units sold per category
avg_units_by_category = sales_df.groupby("Category")["Units"].mean()
print(avg_units_by_category)

# 4.4 Compare sales performance of items on promotion vs. not on promotion
promo_comparison = {
    "promo_avg_sales": sales_df[sales_df["Promotion"] == "Yes"]["Total_Sales"].mean(),
    "no_promo_avg_sales": sales_df[sales_df["Promotion"] == "No"]["Total_Sales"].mean(),
    "promo_total_revenue": sales_df[sales_df["Promotion"] == "Yes"]["Total_Sales"].sum(),
    "no_promo_total_revenue": sales_df[sales_df["Promotion"] == "No"]["Total_Sales"].sum()
}                            

print(promo_comparison)

# TODO 5: Missing Value Detection and Reporting

# 5.1 Identify columns with missing values and count them

missing_counts = sales_df.isnull().sum()
print(missing_counts)

# 5.2 Calculate what percentage of the data is missing in each column

missing_percentages = (sales_df.isnull().sum() / len(sales_df) * 100)
print(missing_percentages)

# TODO 6: Insights and Business Analysis

# 6.1 Create a summary of the top performing category in each region
top_categories_by_region = sales_df.groupby(["Region", "Category"])["Total_Sales"].sum()

top_categories_by_region = top_categories_by_region.groupby("Region").idxmax().str[1]

print(top_categories_by_region)


# 6.2 Calculate average unit price for each product category
avg_price_by_category = sales_df.groupby("Category")["Unit_Price"].mean()
print(avg_price_by_category)

# 6.3 For each product, calcultale total revenue and percentage of overall sales
product_revenue_analysis = sales_df.groupby("Product")["Total_Sales"].sum()

total_revenue = product_revenue_analysis.sum()

product_revenue_analysis = pd.DataFrame({
    "total_revenue": product_revenue_analysis,
    "percentage": (product_revenue_analysis / total_revenue) * 100
    })
print(product_revenue_analysis)

# TODO 7: Generate Analysis Report
print("\n" + "=" * 60)
print("GLOBALTECH Q1 2024 SALES ANALYSIS REPORT")
print("=" * 60)

# 7.1 Display overall sales performance
average_sale_value = total_revenue / total_units
print("Overall Performance:")
print(f"\n- Total Revenue: {total_revenue}")
print(f"\n- Total Units Sold: {total_units}")
print(f"\n- Average Sale Value: {average_sale_value}")

# 7.2 Display regional performance summary
print("\nRegional Performance:")

for region, revenue in sales_by_region.items():
    print(f"\n- {region}: ${revenue:,.2f}")


