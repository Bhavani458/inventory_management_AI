# AI-Powered Inventory Management Assistant

An intelligent inventory management system built to help small convenience store owners automate restocking, track expiring items, and reduce manual effort. This project uses Streamlit for the UI, Snowflake as the data warehouse, OpenAI for AI-driven insights, SendGrid for alerts, and GitHub Actions for automated inventory updates.

## Problem

Many small store owners still rely on manual logging to track inventory and decide when to restock. This often results in missed expirations, stockouts, and wasted time.

## Goal

Create a user-friendly, automated system that:
- Tracks inventory in real time
- Sends alerts for soon-to-expire items
- Uses AI to recommend what and how much to reorder
- Updates inventory automatically each day

## Features

- **Interactive Streamlit app** with inventory dashboard
- **GPT-4 integration** to answer natural language questions and provide reorder suggestions
- **Email alerts via SendGrid** for products nearing expiration
- **Automated daily inventory updates** using GitHub Actions
- Secure configuration with environment variables and GitHub Secrets

## Tech Stack
| Component        | Technology Used |
|------------------|-----------------|
| Frontend UI      | [Streamlit](https://streamlit.io/) |
| AI Integration   | [OpenAI GPT-4](https://openai.com/) |
| Backend Storage  | [Snowflake](https://www.snowflake.com/) |
| Alerts           | [SendGrid Email API](https://sendgrid.com/) |
| CI/CD            | [GitHub Actions](https://docs.github.com/en/actions) |
| Scheduling       | GitHub Actions CRON |
| Secrets Management | GitHub Secrets & `.env` |

## Features
**Inventory Dashboard**  
Visualize all items, categories, quantities, vendors, and expiration dates in an interactive UI.
**AI Reorder Assistant**  
GPT-4 evaluates current inventory and provides reorder recommendations with product names and quantities.
**Natural Language Querying**  
Ask inventory questions like:  
> “Which items are expiring this week?”  
> “What should I reorder today?”
**Automated Expiry Email Alerts**  
Low-stock or expiring items are emailed to the store owner via SendGrid.
**Daily Inventory Update Pipeline**  
A GitHub Actions workflow runs every morning:
- Simulates new inventory rows
- Appends them to Snowflake
- Triggers reorder suggestions
**Secure and Modular**  
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
   - logs AI reorder decisions
---

## Result

The final system provides a convenient, AI-powered solution that saves store owners time and reduces risk of errors or missed restocks. It transforms manual inventory tracking into an automated, intelligent process.

## Future Improvements
- Integrate barcode scanner + OCR
- Add role-based access control (Admin/Viewer)
- Include real sales data for demand forecasting
- WhatsApp/SMS alerts via Twilio

## Author
Bhavani Priya Ganji  
[LinkedIn](https://www.linkedin.com/in/bhavani-priya45/) | [GitHub](https://github.com/Bhavani458)

