# 🧠 AI-Powered Inventory Management Assistant

An intelligent inventory tracking and reorder recommendation system for small convenience stores — powered by **Streamlit**, **Snowflake**, **OpenAI GPT-4**, and **SendGrid**, with CI/CD automation via **GitHub Actions**.
---
## Problem

While visiting a local convenience store, I noticed the owner relied on **manual inventory logs** and **paper-based restocking reminders**. This inefficient process led to frequent stockouts, missed expiry dates, and stress.
---

## 🎯 Goal

To build a **smart, automated assistant** that helps store owners:
- Track and visualize their inventory
- Get **AI-powered reorder suggestions**
- Receive **daily email alerts** for items expiring soon
- Automate inventory updates using CI/CD

---

## 🛠️ Tech Stack

| Component        | Technology Used |
|------------------|-----------------|
| Frontend UI      | [Streamlit](https://streamlit.io/) |
| AI Integration   | [OpenAI GPT-4](https://openai.com/) |
| Backend Storage  | [Snowflake](https://www.snowflake.com/) |
| Alerts           | [SendGrid Email API](https://sendgrid.com/) |
| CI/CD            | [GitHub Actions](https://docs.github.com/en/actions) |
| Scheduling       | GitHub Actions CRON |
| Secrets Management | GitHub Secrets & `.env` |

---

## ⚙️ Features

✅ **Inventory Dashboard**  
Visualize all items, categories, quantities, vendors, and expiration dates in an interactive UI.

✅ **AI Reorder Assistant**  
GPT-4 evaluates current inventory and provides reorder recommendations with product names and quantities.

✅ **Natural Language Querying**  
Ask inventory questions like:  
> “Which items are expiring this week?”  
> “What should I reorder today?”

✅ **Automated Expiry Email Alerts**  
Low-stock or expiring items are emailed to the store owner via SendGrid.

✅ **Daily Inventory Update Pipeline**  
A GitHub Actions workflow runs every morning:
- Simulates new inventory rows
- Appends them to Snowflake
- Triggers reorder suggestions

✅ **Secure and Modular**  
All credentials handled through `.env` or GitHub Secrets.
---
## How It Works
1. Streamlit app connects to Snowflake and loads inventory data.
2. OpenAI GPT-4 handles:
   - Text-to-SQL for user queries
   - Reorder suggestions based on low-stock logic
3. SendGrid alerts store owner about upcoming expiry risks
4. GitHub Actions pipeline (`inventory_pipeline.py`) runs daily and:
   - Inserts new simulated stock data
   - Optionally logs AI reorder decisions
---
## 📦 Setup

1. Clone the repo  
2. Set up `.env` or GitHub Secrets  
3. Install dependencies  
   ```bash
   pip install -r requirements.txt
   ```
4. Run the app
   ```bash
   streamlit run app.py
   ```
---
## 🚀 Results
Built a **fully automated, AI-assisted inventory system** that:
* Saves time
* Reduces spoilage
* Prevents stockouts
* Helps small business owners **focus on more strategic tasks** without manual logging
---

## Future Improvements
* Integrate barcode scanner + OCR
* Add role-based access control (Admin/Viewer)
* Include real sales data for demand forecasting
* WhatsApp/SMS alerts via Twilio
---

## Author
Bhavani Priya Ganji
📫 [LinkedIn](https://www.linkedin.com/in/bhavani-priya45/) | [GitHub](https://github.com/Bhavani458)
## 📄 License
This project is open-sourced under the [MIT License](LICENSE).
```
