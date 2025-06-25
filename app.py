import streamlit as st #streamlit for app ui
import pandas as pd #for data manipulation
from openai import OpenAI #openai api key
import snowflake.connector #connect to snowflake
from snowflake.connector.pandas_tools import write_pandas
from email.mime.text import MIMEText 
import requests
import random

# Load secrets
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Snowflake connection
@st.cache_resource
def get_connection():
    return snowflake.connector.connect(
        user=st.secrets["SNOWFLAKE_USER"],
        password=st.secrets["SNOWFLAKE_PASSWORD"],
        account=st.secrets["SNOWFLAKE_ACCOUNT"],
        warehouse=st.secrets["SNOWFLAKE_WAREHOUSE"],
        database=st.secrets["SNOWFLAKE_DATABASE"],
        schema=st.secrets["SNOWFLAKE_SCHEMA"]
    )

conn = get_connection()
cursor = conn.cursor()

# Load data
@st.cache_data(ttl=300)
def load_data():
    df_inventory = pd.read_sql("SELECT * FROM inventory", conn)
    df_products = pd.read_sql("SELECT * FROM products", conn)
    df_vendors = pd.read_sql("SELECT * FROM vendors", conn)
    # Convert date fields to datetime
    df_inventory["EXPIRATION_DATE"] = pd.to_datetime(df_inventory["EXPIRATION_DATE"])
    df_inventory["LAST_RESTOCKED"] = pd.to_datetime(df_inventory["LAST_RESTOCKED"])
    return df_inventory, df_products, df_vendors

df_inventory, df_products, df_vendors = load_data()

st.title("🧠 AI Inventory Management Assistant")

# Inventory overview
st.header("📦 Inventory Overview")
st.dataframe(df_inventory)

# Low stock filter
st.subheader("🔻 Low Stock Alert")
low_stock = df_inventory[df_inventory["QUANTITY"] < 10]
st.dataframe(low_stock)

# Expiring soon filter
st.subheader("⏳ Expiring in Next 7 Days")
today = pd.Timestamp.today()
expiring = df_inventory[df_inventory["EXPIRATION_DATE"] <= today + pd.Timedelta(days=7)]
st.dataframe(expiring)

# GPT-4 Text-to-SQL
st.header("💬 Ask Inventory Questions (Text-to-SQL)")
user_question = st.text_input("Ask a question about your inventory:")

if user_question:
    prompt = f"""
    Convert the following question into a Snowflake-compatible SQL query using these tables:
    - inventory(inventory_id, product_id, quantity, expiration_date, last_restocked)
    - products(product_id, product_name, category, unit_price, vendor_id)
    - vendors(vendor_id, vendor_name, contact_info)

    Question: {user_question}
    SQL:
    """

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )
    sql_query = response.choices[0].message.content.strip()
    st.code(sql_query, language="sql")

    try:
        result_df = pd.read_sql(sql_query, conn)
        st.dataframe(result_df)
    except Exception as e:
        st.error(f"SQL Execution Error: {e}")

# GPT-4 reorder suggestions
st.header("🧠 AI Reorder Suggestions")

# Merge low_stock with products to include product names
low_stock_merged = pd.merge(low_stock, df_products, on="PRODUCT_ID", how="left")

# Create a readable summary for GPT
low_stock_summary = "\n".join([
    f"{row['PRODUCT_NAME']} (ID: {row['PRODUCT_ID']}, {row['QUANTITY']} units)" 
    for _, row in low_stock_merged.iterrows()
])

if low_stock_summary:
    suggestion_prompt = f"""
    The following products are currently low in stock:

    {low_stock_summary}

    Based on typical inventory management practices, suggest which items should be reordered and in what quantity. Be specific and concise.
    """

    reorder_response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": suggestion_prompt}],
        temperature=0.3
    )

    suggestion_text = reorder_response.choices[0].message.content.strip()
    st.markdown(f"### 🤖 Suggested Reorders:\n{suggestion_text}")
else:
    st.info("No low stock items right now. Reorder suggestions will appear when inventory drops.")

def send_via_sendgrid(subject, body, to_email):
    url = "https://api.sendgrid.com/v3/mail/send"
    headers = {
        "Authorization": f"Bearer {st.secrets['SENDGRID_API_KEY']}",
        "Content-Type": "application/json"
    }
    data = {
        "personalizations": [{
            "to": [{"email": to_email}],
            "subject": subject
        }],
        "from": {"email": st.secrets["EMAIL_SENDER"]},
        "content": [{
            "type": "text/plain",
            "value": body
        }]
    }
    response = requests.post(url, headers=headers, json=data)
    return "✅ Email sent!" if response.status_code == 202 else f"❌ Failed: {response.text}"

st.header("📬 Send Expiry Email Notification")
if st.button("Send Email Alert for Expiring Items"):
    if not expiring.empty:
        # Merge to enrich expiring data
        expiring_merged = pd.merge(expiring, df_products, on="PRODUCT_ID", how="left")
        expiring_merged = pd.merge(expiring_merged, df_vendors, on="VENDOR_ID", how="left")

        # Format the body with key info
        lines = []
        for _, row in expiring_merged.iterrows():
            lines.append(
                f"{row['PRODUCT_ID']} - {row['PRODUCT_NAME']} order from {row['VENDOR_NAME']} "
                f"(Qty: {row['QUANTITY']}, Expiry date: {row['EXPIRATION_DATE'].date()})"
            )

        body = "🚨 The following items are expiring in the next 7 days:\n\n" + "\n".join(lines)
        subject = "Inventory Expiry Alert"
        message = send_via_sendgrid(subject, body, st.secrets["EMAIL_RECEIVER"])
        if "✅" in message:
            st.success("Email sent successfully!")
        else:
            st.error("Error sending email!")
    else:
        st.info("No items expiring in the next 7 days.")

cursor.execute("""
    INSERT INTO restock_log (log_id, created_at, prompt, gpt_response)
    VALUES (%s, CURRENT_TIMESTAMP, %s, %s)
""", (f"log_{random.randint(10000,99999)}", suggestion_prompt, suggestion_text))


