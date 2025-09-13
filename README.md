CrewAI Stock Market Analyst
Advanced AI Financial Analysis: End-to-end stock market forecasting and analysis with multi-agent collaboration.

This project is a sophisticated financial analysis application built on the CrewAI framework, providing an end-to-end pipeline for automated stock market analysis. It leverages a team of specialized AI agents—a researcher, a financial analyst, and a reporting analyst—to generate comprehensive, real-time stock market reports. The system is designed to provide actionable insights by integrating up-to-the-minute market data with advanced predictive modeling and presents the results in an interactive web application.

Simply provide a stock ticker and a forecast period, and the crew will deliver a detailed financial report, complete with an executive summary, a model-based forecast analysis, and specific investor recommendations.

📝 Table of Contents
✨ Key Features

🏗️ How It Works

💻 Technologies Used

📁 File Structure

🚀 Getting Started

🤝 Contributing

📜 License

✨ Key Features
Multi-Agent Collaboration: A crew of three distinct agents works together to perform a complete analysis.

Real-time Data Integration: Uses the SerperDevTool and a custom StockDataTool to gather the latest news, analyst ratings, and competitor information from sources like Yahoo Finance.

Predictive Modeling: The Financial Analyst agent utilizes a custom ProphetForecastTool to generate future price predictions and confidence intervals.

Comprehensive Reporting: The final output is a well-structured, easy-to-read financial report in Markdown format.

Interactive Web Interface: A user-friendly Streamlit application allows for easy input and a clean, organized display of the final report.

🏗️ How It Works
The project follows a sequential process, with each agent performing a specialized task:

Researcher Agent: This agent is responsible for gathering raw, up-to-the-minute information on the specified stock. It searches the web for recent news, major announcements, and analyst ratings to provide a qualitative foundation for the report.

Financial Analyst Agent: The financial analyst takes the raw data from the researcher and uses the Prophet model to perform a quantitative analysis. It forecasts future price trends and provides crucial data points like yhat, yhat_lower, and yhat_upper to inform the recommendations.

Reporting Analyst Agent: The final agent's task is to synthesize all the information from the previous two agents. It compiles the qualitative research and the quantitative model predictions into a single, cohesive, and professional financial report.

💻 Technologies Used
CrewAI: The powerful framework for orchestrating the multi-agent system.

Streamlit: The web framework used to create the interactive user interface.

Yahoo Finance: The primary source for fetching real-time and historical stock data.

CrewAI Tools: SerperDevTool for web search.

Python Libraries: yfinance for historical stock data, prophet for time-series forecasting, and pandas for data manipulation.

📁 File Structure
├── crew/
│   ├── __init__.py
│   ├── config/
│   │   ├── agents.yaml           # Agent roles and backstories
│   │   └── tasks.yaml           # Task descriptions and expected outputs
│   ├── crew.py                  # Defines the main Crew and its agents/tasks
│   └── tools.py                 # Contains the custom tools (StockDataTool, ProphetForecastTool)
├── main.py                      # Main script to run the crew
├── README.md                    # This file
├── requirements.txt             # List of project dependencies
└── .env                         # Environment variables (API keys)

🚀 Getting Started
Prerequisites

Python 3.9 or higher

A SerperDev API key

Installation

Clone the repository:

git clone <your-repository-url>
cd <your-repository-name>

Create a virtual environment and activate it:

python -m venv venv
# On macOS/Linux
source venv/bin/activate
# On Windows
venv\Scripts\activate

Install the required packages:

pip install -r requirements.txt

Configuration

Create a .env file in the root directory.

Add your SerperDev API key to the file:

SERPER_API_KEY="your-api-key"

Running the Crew

From the root directory, run the main.py script with your desired stock ticker and forecast period:

python main.py --topic "TSLA" --forecast_period "1 year"

The script will print the crew's execution steps and the final report to the console.

🤝 Contributing
Contributions are what make the open-source community an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

Fork the Project

Create your Feature Branch (git checkout -b feature/AmazingFeature)

Commit your Changes (git commit -m 'Add some AmazingFeature')

Push to the Branch (git push origin feature/AmazingFeature)

Open a Pull Request
