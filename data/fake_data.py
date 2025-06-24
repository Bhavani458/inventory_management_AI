import pandas as pd
import random
from datetime import datetime, timedelta
import faker

fake = faker.Faker()

# Simulate realistic vendors
vendors = []
vendor_names = ["Sysco", "US Foods", "Gordon Food Service", "Kroger Supply", "Whole Foods Market", "Amazon Fresh", "Target Fulfillment", "Costco Wholesale", "Walmart Distribution", "Local Organic Co."]
for i in range(1, 21):
    name = random.choice(vendor_names) + " #" + str(random.randint(1, 50))
    vendors.append({
        'vendor_id': f"V{str(i).zfill(2)}",
        'vendor_name': name,
        'contact_info': fake.email()
    })

# Simulate realistic product names and categories
categories = ['Dairy', 'Bakery', 'Produce', 'Meat', 'Snacks', 'Hygiene', 'Beverages', 'Canned Goods', 'Frozen Foods', 'Cleaning Supplies']
product_names = {
    'Dairy': ['Milk', 'Cheddar Cheese', 'Yogurt', 'Butter'],
    'Bakery': ['Whole Wheat Bread', 'Bagels', 'Croissants', 'Muffins'],
    'Produce': ['Bananas', 'Apples', 'Carrots', 'Spinach'],
    'Meat': ['Chicken Breast', 'Ground Beef', 'Pork Chops', 'Salmon Fillet'],
    'Snacks': ['Potato Chips', 'Granola Bars', 'Popcorn', 'Trail Mix'],
    'Hygiene': ['Toothpaste', 'Hand Soap', 'Shampoo', 'Deodorant'],
    'Beverages': ['Orange Juice', 'Soda', 'Bottled Water', 'Coffee'],
    'Canned Goods': ['Canned Beans', 'Tomato Sauce', 'Canned Tuna', 'Soup'],
    'Frozen Foods': ['Frozen Pizza', 'Ice Cream', 'Frozen Vegetables', 'Chicken Nuggets'],
    'Cleaning Supplies': ['Laundry Detergent', 'All-Purpose Cleaner', 'Sponges', 'Dish Soap']
}

products = []
product_counter = 1
for cat, items in product_names.items():
    for item in items:
        products.append({
            'product_id': f"P{str(product_counter).zfill(2)}",
            'product_name': item,
            'category': cat,
            'unit_price': round(random.uniform(1.0, 20.0), 2),
            'vendor_id': random.choice([f"V{str(i).zfill(2)}" for i in range(1, 21)])
        })
        product_counter += 1

# Simulate inventory based on products
inventory = []
for i, product in enumerate(products, 1):
    quantity = random.randint(0, 150)
    expiration_days = random.randint(3, 60) if product['category'] in ['Dairy', 'Meat', 'Produce'] else random.randint(90, 365)
    restocked_days_ago = random.randint(1, 30)
    inventory.append({
        'inventory_id': f"I{str(i).zfill(2)}",
        'product_id': product['product_id'],
        'quantity': quantity,
        'expiration_date': (datetime.today() + timedelta(days=expiration_days)).date(),
        'last_restocked': (datetime.today() - timedelta(days=restocked_days_ago)).date()
    })

# Convert to DataFrames
vendors_df = pd.DataFrame(vendors)
products_df = pd.DataFrame(products)
inventory_df = pd.DataFrame(inventory)

# Save to CSV
vendors_df.to_csv("./data/vendors_real.csv", index=False)
products_df.to_csv("./data/products_real.csv", index=False)
inventory_df.to_csv("./data/inventory_real.csv", index=False)

# Display one table
#import ace_tools as tools; tools.display_dataframe_to_user(name="Realistic Products Data", dataframe=products_df)
