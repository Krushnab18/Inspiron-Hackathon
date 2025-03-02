import pandas as pd
from faker import Faker
import random
from datetime import datetime, timedelta

# Initialize Faker
fake = Faker()

# Define constants
NUM_ROWS = 791  # 1 year of daily data
SEGMENTS = ["Retail", "Wholesale"]
COUNTRIES = ["USA", "India", "UK", "Germany", "Japan"]
PRODUCTS = ["Product A", "Product B", "Product C", "Product D"]

# Generate dummy data
data = []
start_date = datetime(2023, 1, 1)

for _ in range(NUM_ROWS):
    date = (start_date + timedelta(days=_)).strftime("%Y-%m-%d")
    segment = random.choice(SEGMENTS)
    country = random.choice(COUNTRIES)
    product = random.choice(PRODUCTS)
    units_sold = random.randint(50, 500)
    manufacturing_price = round(random.uniform(10, 100), 2)
    sale_price = round(manufacturing_price * random.uniform(1.5, 3.0), 2)
    gross_sales = round(units_sold * sale_price, 2)
    discounts = round(gross_sales * random.uniform(0.05, 0.20), 2)
    sales = round(gross_sales - discounts, 2)
    cogs = round(units_sold * manufacturing_price, 2)
    profit = round(sales - cogs, 2)

    data.append([
        date, segment, country, product, units_sold, manufacturing_price,
        sale_price, gross_sales, discounts, sales, cogs, profit
    ])

# Create a DataFrame
columns = [
    "Date", "Segment", "Country", "Product", "Units Sold", "Manufacturing Price",
    "Sale Price", "Gross Sales", "Discounts", "Sales", "COGS", "Profit"
]
df = pd.DataFrame(data, columns=columns)

# Save to CSV (optional)
df.to_csv("financial_data.csv", index=False)

# Display the first 5 rows
print(df.head())
