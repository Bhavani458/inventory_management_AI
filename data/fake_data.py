#import libraries to generate fake datasets
import pandas as pd
import random
from datetime import datetime, timedelta
import faker

fake = faker.Faker()

# Generate vendors - vendor_id, name and contact info
vendors = []
for i in range(1, 21):
    vendors.append({
        'vendor_id': i,
        'vendor_name': fake.company(),
        'contact_info': fake.email()
    })

# Generate products - can add more products 
categories = ['Dairy', 'Bakery', 'Produce', 'Meat', 'Snacks', 'Hygiene', 'Beverages', 'Canned Goods']
products = []
for i in range(1, 201):
    products.append({
        'product_id': i,
        'product_name': fake.word().capitalize() + " " + random.choice(['Juice', 'Bread', 'Milk', 'Chips', 'Soap', 'Fruit', 'Beans', 'Meat']),
        'category': random.choice(categories),
        'unit_price': round(random.uniform(1.0, 20.0), 2),
        'vendor_id': random.randint(1, 20)
    })

# Generate inventory
inventory = []
for i in range(1, 201):
    product_id = random.randint(1, 200)
    expiration_days = random.randint(1, 180)
    last_restock_days = random.randint(1, 30)
    inventory.append({
        'inventory_id': i,
        'product_id': product_id,
        'quantity': random.randint(0, 100),
        'expiration_date': (datetime.today() + timedelta(days=expiration_days)).date(),
        'last_restocked': (datetime.today() - timedelta(days=last_restock_days)).date()
    })

# Convert to DataFrames
vendors_df = pd.DataFrame(vendors)
products_df = pd.DataFrame(products)
inventory_df = pd.DataFrame(inventory)

# Save to CSV
vendors_df.to_csv("./data/vendors.csv", index=False)
products_df.to_csv("./data/products.csv", index=False)
inventory_df.to_csv("./data/inventory.csv", index=False)

# Show the output
#import ace_tools as tools; tools.display_dataframe_to_user(name="Vendors Data", dataframe=vendors_df)
#tools.display_dataframe_to_user(name="Products Data", dataframe=products_df)
#tools.display_dataframe_to_user(name="Inventory Data", dataframe=inventory_df)
