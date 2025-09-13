import datetime as date
import yfinance as yf
from prophet import Prophet
import pandas as pd

START = "2020-01-01"
TODAY = date.date.today().strftime("%Y-%m-%d")

def load_data(ticker):

    try:
        data = yf.download(ticker, start=START, end=TODAY, progress=False, multi_level_index=False, auto_adjust=True)
        data.reset_index(inplace=True)
        return data
    
    except Exception as e:
        print(f"Error downloading data for {ticker}: {str(e)}")
        return None

def fit_predict(data, period):
            
    data_clean = data[['ds', 'y']].dropna()
    data_clean['ds'] = pd.to_datetime(data_clean['ds'])
    
    model = Prophet(
        daily_seasonality=False,
        weekly_seasonality=True,
        yearly_seasonality=True,
        changepoint_prior_scale=0.05
    )
    
    model.fit(data_clean)
    
    future = model.make_future_dataframe(periods=period)
    
    forecast = model.predict(future)
    
    return forecast, model