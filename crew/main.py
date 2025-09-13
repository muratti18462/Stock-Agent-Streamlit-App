import os
import pandas as pd
from crewai import Agent, Crew, Process, Task
from crewai_tools import SerperDevTool
from .crew import LatestAiDevelopmentCrew
from dotenv import load_dotenv

from stocks.stocks_model import load_data, fit_predict

load_dotenv()

os.environ['SERPER_API_KEY'] = os.getenv('SERPER_API_KEY', '')

os.environ['OPENAI_API_BASE'] = 'http://localhost:11434'
os.environ['OPENAI_MODEL_NAME'] = 'ollama/llama3.2:latest'
os.environ['OPENAI_API_KEY'] = 'ollama' 

def run_stock_crew(ticker: str, prophet_forecast: pd.DataFrame, period: int) -> str:
    """
    Runs the stock analysis crew with the prophet forecast data.
    """
    
    forecast_json = prophet_forecast.to_json()

    inputs = {
        'topic': ticker,
        'prophet_prediction': forecast_json,
        'period': period
    }
    
    crew = LatestAiDevelopmentCrew().crew()
    result = crew.kickoff(inputs=inputs)
    
    return result