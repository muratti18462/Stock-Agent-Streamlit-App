# CrewAI Stock Market Analyst

**Advanced AI Financial Analysis:** End-to-end stock market forecasting and analysis with multi-agent collaboration.

This project is a sophisticated financial analysis application built on the **CrewAI framework**, providing an end-to-end pipeline for automated stock market analysis.  
It leverages a team of specialized AI agents—a **researcher**, a **financial analyst**, and a **reporting analyst**—to generate comprehensive, real-time stock market reports.  

The system is designed to provide actionable insights by integrating up-to-the-minute market data with advanced predictive modeling and presents the results in an **interactive web application**.

Simply provide a stock ticker and a forecast period, and the crew will deliver a detailed financial report, complete with:
- An **executive summary**
- A **model-based forecast analysis**
- **Investor recommendations**

---

## Key Features
- **Multi-Agent Collaboration**: A crew of three distinct agents works together to perform a complete analysis.  
- **Real-time Data Integration**: Uses the `SerperDevTool` and a custom `StockDataTool` to gather the latest news, analyst ratings, and competitor information from sources like Yahoo Finance.  
- **Predictive Modeling**: The Financial Analyst agent utilizes a custom `ProphetForecastTool` to generate future price predictions and confidence intervals.  
- **Comprehensive Reporting**: The final output is a well-structured, easy-to-read financial report in Markdown format.  
- **Interactive Web Interface**: A user-friendly Streamlit application allows for easy input and a clean, organized display of the final report.  

---

## How It Works
The project follows a sequential process, with each agent performing a specialized task:

1. **Researcher Agent**  
   - Gathers raw, up-to-the-minute information on the specified stock.  
   - Searches the web for recent news, major announcements, and analyst ratings.  
   - Provides a **qualitative foundation** for the report.  

2. **Financial Analyst Agent**  
   - Takes raw data from the researcher.  
   - Uses the Prophet model to perform **quantitative analysis**.  
   - Forecasts future price trends and provides data points like `yhat`, `yhat_lower`, and `yhat_upper`.  

3. **Reporting Analyst Agent**  
   - Synthesizes all information from the previous agents.  
   - Compiles qualitative research and quantitative predictions into a **professional financial report**.  

---

## Technologies Used
- **CrewAI**: Framework for orchestrating the multi-agent system.  
- **Streamlit**: For building the interactive web interface.  
- **Yahoo Finance**: Source for real-time and historical stock data.  
- **CrewAI Tools**: `SerperDevTool` for web search.  
- **Python Libraries**:  
  - `yfinance` for stock data  
  - `prophet` for time-series forecasting  
  - `pandas` for data manipulation  

---

## 📂 Project Structure

### Tree View
```bash
├── crew/
│   ├── __init__.py
│   ├── config/
│   │   ├── agents.yaml           # Agent roles and backstories
│   │   └── tasks.yaml            # Task descriptions and expected outputs
│   ├── crew.py                   # Defines the main Crew and its agents/tasks
│   └── tools.py                  # Contains the custom tools (StockDataTool, ProphetForecastTool)
├── main.py                       # Main script to run the crew
├── README.md                     # This file
├── requirements.txt              # List of project dependencies
└── .env                          # Environment variables (API keys)



### Prerequisites
- Python **3.9+**  
- A **SerperDev API key**
