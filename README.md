# AI-Powered Inventory Management Assistant

An intelligent inventory management system designed to help small convenience store owners automate restocking, track expiring items, and reduce manual effort.

This project integrates:
- **Streamlit** for the UI
- **Snowflake** for data warehousing
- **OpenAI GPT-4** for AI-driven insights
- **SendGrid** for email alerts
- **GitHub Actions** for automated daily updates

---

## Problem

Many small store owners rely on manual logs to track inventory and decide when to restock. This leads to:
- Missed expiration dates
- Stockouts and overstocking
- Time-consuming inventory reviews

---

## Goal

Build a user-friendly, automated system that:
- Tracks inventory in real time
- Sends alerts for soon-to-expire items
- Uses AI to recommend restock quantities
- Updates inventory automatically each day

---

## Features

### Inventory Dashboard  
Visualize items, categories, quantities, vendors, and expiration dates in an interactive UI.

### AI Reorder Assistant  
Uses GPT-4 to analyze low-stock products and generate reorder suggestions with quantities and product names.

### Natural Language Querying  
Ask free-form questions like:  
> “Which items are expiring this week?”  
> “What should I reorder today?”

### Automated Expiry Email Alerts  
Notifies store owners of expiring inventory via SendGrid email integration.

### Daily Inventory Update Pipeline  
Automated workflow using GitHub Actions that:
- Simulates and inserts new inventory data
- Logs reorder decisions based on GPT recommendations

### Secure and Modular  
All secrets are stored in `.env` (for local) or GitHub Secrets (for production CI/CD).

---

## Tech Stack

| Component           | Technology Used                        |
|---------------------|-----------------------------------------|
| Frontend UI         | [Streamlit](https://streamlit.io/)     |
| AI Integration      | [OpenAI GPT-4](https://openai.com/)     |
| Backend Data Store  | [Snowflake](https://www.snowflake.com/) |
| Alerts              | [SendGrid](https://sendgrid.com/)       |
| CI/CD Pipeline      | [GitHub Actions](https://github.com/)   |
| Scheduling          | GitHub Actions (CRON)                   |
| Secrets Management  | `.env` and GitHub Secrets               |

---

## How It Works

1. The Streamlit app queries Snowflake to load inventory data.
2. Users interact via a dashboard or GPT-powered text interface.
3. GPT-4 translates natural language to SQL and suggests reorders.
4. A GitHub Actions pipeline runs daily to:
   - Insert new simulated inventory entries
   - Trigger AI reorder checks and log decisions
5. Email alerts are sent for products nearing expiration.

---

## Result

A convenient, AI-assisted application that:
- Saves time and manual effort
- Reduces product loss due to expiration
- Helps store owners make better stocking decisions
- Provides a scalable foundation for real-time inventory intelligence

---

## Future Improvements

- Barcode scanner + OCR integration
- Role-based access control (Admin/Viewer)
- Sales-driven demand forecasting
- SMS/WhatsApp alerts using Twilio

---

## Author

**Bhavani Priya Ganji**  
[LinkedIn](https://www.linkedin.com/in/bhavani-priya45/)  
[GitHub](https://github.com/Bhavani458)
