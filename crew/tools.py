import yfinance as yf
from crewai_tools import BaseTool, tool
from pydantic import BaseModel, Field
import pandas as pd
from prophet import Prophet
import json

class StockDataToolSchema(BaseModel):
    """Input schema for the StockDataTool."""
    ticker: str = Field(description="The stock ticker symbol, e.g., 'AAPL'.")

class StockDataTool(BaseTool):
    name: str = "Stock Data Tool"
    description: str = "Downloads stock data for a given ticker from Yahoo Finance. Returns the data as a JSON string."
    args_schema: BaseModel = StockDataToolSchema

    def _run(self, ticker: str):
        try:
            stock = yf.Ticker(ticker)
            hist = stock.history(period="1y")
            if hist.empty:
                return f"No data found for ticker: {ticker}"
            
            # Format data for JSON output
            hist.reset_index(inplace=True)
            hist['Date'] = hist['Date'].dt.strftime('%Y-%m-%d')
            return json.dumps(hist.to_dict('records'))
        except Exception as e:
            return f"An error occurred while fetching data: {e}"

class ProphetForecastToolSchema(BaseModel):
    """Input schema for the ProphetForecastTool."""
    data: str = Field(description="JSON string of historical stock data.")
    forecast_period: str = Field(description="The period for the forecast, e.g., '1 year'.")

class ProphetForecastTool(BaseTool):
    name: str = "Prophet Forecast Tool"
    description: str = "Performs a time-series forecast using the Prophet model. " \
                       "Accepts historical stock data as a JSON string and a forecast period. " \
                       "Returns the forecast as a JSON string."
    args_schema: BaseModel = ProphetForecastToolSchema

    def _run(self, data: str, forecast_period: str):
        try:
            df = pd.read_json(data)
            df['ds'] = pd.to_datetime(df['Date'])
            df['y'] = df['Close']
            
            model = Prophet()
            model.fit(df)
            
            periods = 0
            if "year" in forecast_period:
                periods = int(forecast_period.split()[0]) * 365
            elif "month" in forecast_period:
                periods = int(forecast_period.split()[0]) * 30
            elif "day" in forecast_period:
                periods = int(forecast_period.split()[0])
            
            future = model.make_future_dataframe(periods=periods)
            forecast = model.predict(future)
            
            forecast.rename(columns={'ds': 'Date', 'yhat': 'Forecast'}, inplace=True)
            forecast['Date'] = forecast['Date'].dt.strftime('%Y-%m-%d')
            
            # Return only the relevant forecast columns
            return json.dumps(forecast[['Date', 'Forecast', 'yhat_lower', 'yhat_upper']].to_dict('records'))
        except Exception as e:
            return f"An error occurred during forecasting: {e}"
