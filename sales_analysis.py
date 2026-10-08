

import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv("Superstore_Raw.csv")



data["Order Date"] = pd.to_datetime(data["Order Date"], dayfirst=True)

data = data.drop_duplicates()

print("\n========== DATASET OVERVIEW ==========")
print("Shape:", data.shape)

print("\nMissing Values:")
print(data.isnull().sum())

print("\nDuplicate Rows:", data.duplicated().sum())

print("\nColumns:")
print(data.columns.tolist())




category_data = data.groupby("Category")[["Sales", "Profit"]].sum()

category_data["Profit_Margin"] = (
    category_data["Profit"] / category_data["Sales"] * 100
)

print("\n========== CATEGORY ANALYSIS ==========")
print(category_data)




subcategory_data = data.groupby("Sub-Category")[["Sales", "Profit"]].sum()

subcategory_data["Profit_Margin"] = (
    subcategory_data["Profit"] /
    subcategory_data["Sales"] * 100
)

print("\n========== SUB-CATEGORY ANALYSIS ==========")
print(subcategory_data.sort_values("Profit_Margin"))




region_data = data.groupby("Region")[["Sales", "Profit"]].sum()

region_data["Profit_Margin"] = (
    region_data["Profit"] /
    region_data["Sales"] * 100
)

print("\n========== REGION ANALYSIS ==========")
print(region_data)




segment_data = data.groupby("Segment")[["Sales", "Profit"]].sum()

segment_data["Profit_Margin"] = (
    segment_data["Profit"] /
    segment_data["Sales"] * 100
)

print("\n========== SEGMENT ANALYSIS ==========")
print(segment_data)


yearly_data = data.groupby(
    data["Order Date"].dt.year
)[["Sales", "Profit"]].sum()

yearly_data["Profit_Margin"] = (
    yearly_data["Profit"] /
    yearly_data["Sales"] * 100
)

print("\n========== YEARLY ANALYSIS ==========")
print(yearly_data)


monthly_data = data.groupby(
    data["Order Date"].dt.month
)[["Sales", "Profit"]].sum()

monthly_data["Profit_Margin"] = (
    monthly_data["Profit"] /
    monthly_data["Sales"] * 100
)

print("\n========== MONTHLY ANALYSIS ==========")
print(monthly_data)




product_profit = (
    data.groupby("Product Name")["Profit"]
    .sum()
    .sort_values()
)

top_10_products = product_profit.tail(10)
bottom_10_products = product_profit.head(10)

print("\n========== TOP 10 PRODUCTS ==========")
print(top_10_products)

print("\n========== BOTTOM 10 PRODUCTS ==========")
print(bottom_10_products)



discount_profit = data.groupby("Discount")["Profit"].mean()

print("\n========== DISCOUNT VS AVERAGE PROFIT ==========")
print(discount_profit)



tables_data = data[data["Sub-Category"] == "Tables"]

tables_region = tables_data.groupby(
    "Region"
)[["Sales", "Profit"]].sum()

tables_region["Profit_Margin"] = (
    tables_region["Profit"] /
    tables_region["Sales"] * 100
)

print("\n========== TABLES BY REGION ==========")
print(tables_region)


# East + Tables
east_tables = data[
    (data["Sub-Category"] == "Tables") &
    (data["Region"] == "East")
]

east_tables_products = (
    east_tables.groupby("Product Name")["Profit"]
    .sum()
    .sort_values()
)

print("\n========== EAST + TABLES PRODUCTS ==========")
print(east_tables_products)




product_name = (
    "Riverside Furniture Oval Coffee Table, "
    "Oval End Table, End Table with Drawer"
)

specific_product = east_tables[
    east_tables["Product Name"] == product_name
]

print("\n========== SPECIFIC PRODUCT ANALYSIS ==========")

print("Number of Transactions:",
      specific_product.shape[0])

print("Total Sales:",
      specific_product["Sales"].sum())

print("Total Quantity:",
      specific_product["Quantity"].sum())

print("Total Profit:",
      specific_product["Profit"].sum())

print("Average Discount:",
      specific_product["Discount"].mean())

specific_sales = specific_product["Sales"].sum()
specific_profit = specific_product["Profit"].sum()

specific_margin = (
    specific_profit / specific_sales * 100
)

print("Profit Margin:",
      specific_margin, "%")




category_data[["Sales", "Profit"]].plot(
    kind="bar",
    figsize=(10, 5)
)

plt.title("Sales and Profit by Category")
plt.xlabel("Category")
plt.ylabel("Amount")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


# ---- Profit by Sub-Category ----

subcategory_profit = (
    data.groupby("Sub-Category")["Profit"]
    .sum()
    .sort_values()
)

subcategory_profit.plot(
    kind="bar",
    figsize=(12, 6)
)

plt.title("Profit by Sub-Category")
plt.xlabel("Sub-Category")
plt.ylabel("Total Profit")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()


# ---- Sales & Profit by Region ----

region_data[["Sales", "Profit"]].plot(
    kind="bar",
    figsize=(10, 5)
)

plt.title("Sales and Profit by Region")
plt.xlabel("Region")
plt.ylabel("Amount")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


# ---- Yearly Sales & Profit ----

plt.figure(figsize=(10, 5))

plt.plot(
    yearly_data.index,
    yearly_data["Sales"],
    marker="o",
    label="Sales"
)

plt.plot(
    yearly_data.index,
    yearly_data["Profit"],
    marker="o",
    label="Profit"
)

plt.xlabel("Year")
plt.ylabel("Amount")
plt.title("Yearly Sales and Profit Trend")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()



plt.figure(figsize=(10, 5))

plt.plot(
    yearly_data.index,
    yearly_data["Profit_Margin"],
    marker="o"
)

plt.xlabel("Year")
plt.ylabel("Profit Margin (%)")
plt.title("Yearly Profit Margin Trend")
plt.grid(True)
plt.tight_layout()
plt.show()



plt.figure(figsize=(10, 5))

plt.plot(
    discount_profit.index * 100,
    discount_profit.values,
    marker="o"
)

plt.xlabel("Discount (%)")
plt.ylabel("Average Profit")
plt.title("Discount vs Average Profit")

plt.axhline(0, linestyle="--")

plt.grid(True)
plt.tight_layout()
plt.show()




plt.figure(figsize=(12, 6))

bottom_10_products.plot(kind="bar")

plt.xlabel("Product")
plt.ylabel("Total Profit")
plt.title("Bottom 10 Products by Profit")
plt.xticks(rotation=45, ha="right")

plt.tight_layout()
plt.show()



plt.figure(figsize=(12, 6))

top_10_products.plot(kind="bar")

plt.xlabel("Product")
plt.ylabel("Total Profit")
plt.title("Top 10 Products by Profit")
plt.xticks(rotation=45, ha="right")

plt.tight_layout()
plt.show()




print("\n\n========== FINAL BUSINESS INSIGHTS ==========")

print("""
1. Technology generated the highest total sales and profit
   among the three main categories.

2. Tables were the weakest sub-category by profit margin,
   with a negative overall profit margin.

3. Higher discount levels were generally associated with
   lower average profit in the dataset.

4. East-region Tables showed a strongly negative profit
   margin and higher average discount.

5. The Riverside Furniture product in East + Tables had
   a 40% average discount and a -30% profit margin.

6. Sales and total profit increased substantially from
   2023 to 2026.

7. 2025 had the highest yearly profit margin, while
   2026 had the highest total sales and total profit.

8. Loss-making products should be reviewed for pricing,
   discounting, and cost-related issues.
""")

print("\n========== ANALYSIS COMPLETED ==========")