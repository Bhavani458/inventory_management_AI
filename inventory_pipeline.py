import snowflake.connector
import pandas as pd
from datetime import datetime, timedelta
import random
import os
from openai import OpenAI

user = os.getenv("SNOWFLAKE_USER")
password = os.getenv("SNOWFLAKE_PASSWORD")
account = os.getenv("SNOWFLAKE_ACCOUNT")
warehouse = os.getenv("SNOWFLAKE_WAREHOUSE")
database = os.getenv("SNOWFLAKE_DATABASE")
schema = os.getenv("SNOWFLAKE_SCHEMA")

conn = snowflake.connector.connect(
    user=user, password=password, account=account,
    warehouse=warehouse, database=database, schema=schema
)
cursor = conn.cursor()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Simulate new restocks for 5 random product_ids
product_ids = [f"P{str(i).zfill(2)}" for i in random.sample(range(1, 41), 5)]
new_data = []

for pid in product_ids:
    quantity = random.randint(30, 100)
    expiration = datetime.today() + timedelta(days=random.randint(5, 60))
    restocked = datetime.today()
    new_data.append((pid, quantity, expiration.date(), restocked.date()))

# Convert to DataFrame
df_new = pd.DataFrame(new_data, columns=["PRODUCT_ID", "QUANTITY", "EXPIRATION_DATE", "LAST_RESTOCKED"])

for _, row in df_new.iterrows():
    cursor.execute(f"""
        INSERT INTO inventory (INVENTORY_ID, PRODUCT_ID, QUANTITY, EXPIRATION_DATE, LAST_RESTOCKED)
        VALUES ('I{random.randint(1000, 9999)}', '{row.PRODUCT_ID}', {row.QUANTITY},
                '{row.EXPIRATION_DATE}', '{row.LAST_RESTOCKED}')
    """)
conn.commit()




