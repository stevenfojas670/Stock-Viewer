import os 
import requests
from flask import Flask, redirect, url_for, request, jsonify, url_for
from markupsafe import escape
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("AV_KEY")

app = Flask(__name__)
CORS(app)

stocks_list = ['AAPL', 'MSFT', 'NVDA', 'GOOG', 'AMZN', 'META', 'TSLA', 'CRM', 'AMD', 'BABA', 'PYPL', 'TTD', 'EA', 'ZG', 'MTCH']

@app.route("/home", methods=['GET'])
def home():
    # Call whatever function renders the tiles
    return get_prices(stocks_list)


@app.route("/details/<stock_name>", methods=['GET'])
def get_details(stock_name):
    # Load Company Overview
    # Load prices (time_series_daily)
    # Show company symbol, asset type, name, description, exchange sector, industry and market capitalization, or N/A
    # Show list of historical prices (time_series_daily)
    # For historical price item show the following: date, close price, volume and percentage change in price from the previous day
    return []


# API Function Calls
def get_overview(stock_name):
    url = f'https://www.alphavantage.co/query?function=OVERVIEW&symbol={stock}&apikey={API_KEY}'
    r = requests.get(url)
    data = r.json()

    return data


def get_prices(stocks):
    data = []
    for stock in stocks:
        url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={stock}&apikey={API_KEY}'
        r = requests.get(url)
        data.append(r.json())

    return data


if __name__ == "__main__":
    app.run(port=8080, debug=True)