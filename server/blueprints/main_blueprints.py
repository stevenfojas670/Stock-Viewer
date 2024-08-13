@app.route("/details/<stock_name>", methods=['GET'])
def get_details(stock_name):
    # Load Company Overview
    # Load prices (time_series_daily)
    # Show company symbol, asset type, name, description, exchange sector, industry and market capitalization, or N/A
    # Show list of historical prices (time_series_daily)
    # For historical price item show the following: date, close price, volume and percentage change in price from the previous day
    return []


# API Function Calls
def get_overview(stocks):
    url = f'https://www.alphavantage.co/query?function=OVERVIEW&symbol={stocks}&apikey={API_KEY}'
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