import streamlit as st
from stocks.stocks_model import load_data, fit_predict
from plotly import graph_objs as go
from prophet.plot import plot_plotly
import pandas as pd
from crew.main import run_stock_crew

st.title('Stock Forecast with AI Agents')

stocks = ('GOOGL', 'AAPL', 'MSFT', 'TSLA', 'AMZN', 'META')
selected_stock = st.selectbox('Select dataset for prediction', stocks)

n_years = st.slider('Years of prediction:', 1, 4)
period = n_years * 365

if st.button('Generate Report'):
    st.text('Loading stock data...')
    
    data = load_data(selected_stock)
    
    if data is None or data.empty:
        st.error(f"Failed to load data for {selected_stock}. Please try a different stock symbol.")
        st.stop()
    
    st.success('Data loaded successfully!')

    def plot_raw_data():
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=data.index, y=data['Open'], name="stock_open"))
        fig.add_trace(go.Scatter(x=data.index, y=data['Close'], name="stock_close"))
        fig.layout.update(title_text='Time Series data with Rangeslider', xaxis_rangeslider_visible=True)
        st.plotly_chart(fig)
    plot_raw_data()
    
    st.subheader('Prophet Model Forecast')
    
    data_prophet = data.reset_index()[['Date', 'Close']].rename(columns={"Date": "ds", "Close": "y"})
    data_prophet = data_prophet.dropna()
        
    forecast, model = fit_predict(data_prophet, period)
    
    st.write('Forecast data (last 5 rows)')
    st.dataframe(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail())
    
    fig1 = plot_plotly(model, forecast)
    st.plotly_chart(fig1)
    
    st.write("Forecast components")
    fig2 = model.plot_components(forecast)
    st.pyplot(fig2)
    
    st.subheader('AI Agent Research and Analysis')
    with st.spinner('Running AI agents to generate a comprehensive report...'):
        try:

            final_report = run_stock_crew(selected_stock, forecast, period)
            st.subheader('Final Financial Report')
            st.markdown(final_report)
        except Exception as e:
            st.error(f"An error occurred: {e}")
            st.markdown("Please check the terminal for more details on the error.")
