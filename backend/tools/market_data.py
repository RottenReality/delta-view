from langchain.tools import tool
import yfinance as yf


@tool('get_stock_price', description='Function that returns the current stock price based on a ticker symbol.')
def get_stock_price(ticker: str):
    stock = yf.Ticker(ticker)
    return stock.history()['Close'].iloc[-1]


@tool('get_historical_stock_price', description='Function that returns the historical stock price based on a ticker symbol and a date range.')
def get_historical_stock_price(ticker: str, start_date: str, end_date: str):
    stock = yf.Ticker(ticker)
    return stock.history(start=start_date, end=end_date).to_dict()


@tool('get_balance_sheet', description='Function that returns the balance sheet data for a given ticker symbol.')
def get_balance_sheet(ticker: str):
    stock = yf.Ticker(ticker)
    return stock.balance_sheet


@tool('get_stock_news', description='Function that returns news based on a given ticker symbol.')
def get_stock_news(ticker: str):
    stock = yf.Ticker(ticker)
    return stock.news


market_data_tools = [
    get_stock_price,
    get_historical_stock_price,
    get_balance_sheet,
    get_stock_news,
]