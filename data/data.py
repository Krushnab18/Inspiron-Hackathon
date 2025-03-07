import csv
from random import choice, randint, uniform
from datetime import datetime, timedelta

# Sample data
segments = ["Government", "Midmarket", "Channel Partners"]
countries = ["Canada", "Germany", "France", "India", "USA"]
products = ["Carretera", "Montana", "Paseo", "Velo", "Amarilla"]

# Function to generate random financial data
def generate_financial_data(num_rows=365):
    data = []
    start_date = datetime.strptime("2023-01-01", "%Y-%m-%d")

    for _ in range(num_rows):
        segment = choice(segments)
        country = choice(countries)
        product = choice(products)
        units_sold = randint(500, 3000)  # Whole number of units
        manufacturing_price = round(uniform(3, 10), 2)
        sale_price = round(uniform(12, 350), 2)
        gross_sales = round(units_sold * sale_price, 2)
        discount_rate = uniform(0.05, 0.3) if uniform(0, 1) > 0.8 else 0
        discounts = round(gross_sales * discount_rate, 2)
        sales = round(gross_sales - discounts, 2)
        cogs = round(units_sold * manufacturing_price, 2)
        profit = round(sales - cogs, 2)
        date = start_date + timedelta(days=randint(0, 364))

        data.append([
            date.strftime("%Y-%m-%d"), segment, country, product, units_sold,
            manufacturing_price, sale_price, gross_sales, discounts,
            sales, cogs, profit
        ])

    return data

# Write data to CSV
def write_to_csv(data, filename="financial_data.csv"):
    headers = [
        "Date", "Segment", "Country", "Product", "Units Sold",
        "Manufacturing Price", "Sale Price", "Gross Sales",
        "Discounts", "Sales", "COGS", "Profit"
    ]

    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(data)

    print(f"File '{filename}' generated successfully with {len(data)} rows!")

# Generate and write data
if __name__ == "__main__":
    data = generate_financial_data(num_rows=100)
    write_to_csv(data)
