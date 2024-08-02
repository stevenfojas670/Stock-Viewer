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

@app.route("/", methods=['GET'])
def home():
    return stocks_prices


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


stocks_prices = [
    {
        "company": "3M",
        "description": "3M, based in Minnesota, may be best known for its Scotch tape and Post-It Notes, but it also produces sand paper, adhesives, medical products, computer screen filters, food safety items, stationery products and many products used in automotive, marine, and aircraft industries.",
        "initial_price": 44.28,
        "price_2002": 56.27,
        "price_2007": 95.85,
        "symbol": "MMM"
    },
    {
        "company": "Amazon.com",
        "description": "Amazon.com, Inc. is an online retailer in North America and internationally. The company serves consumers through its retail Web sites and focuses on selection, price, and convenience. It also offers programs that enable sellers to sell their products on its Web sites, and their own branded Web sites. In addition, the company serves developer customers through Amazon Web Services, which provides access to technology infrastructure that developers can use to enable virtually various type of business. Further, it manufactures and sells the Kindle e-reader. Founded in 1994 and headquartered in Seattle, Washington.",
        "initial_price": 89.38,
        "price_2002": 17.01,
        "price_2007": 93.43,
        "symbol": "AMZN"
    },
    {
        "company": "Campbell Soup",
        "description": "Campbell Soup is a worldwide food company, offering condensed and ready-to-serve soups; broth, stocks, and canned poultry; pasta sauces; Mexican sauces; canned pastas, gravies, and beans; juices and beverages; and tomato juices. Its customers include retail food chains, mass discounters, mass merchandisers, club stores, convenience stores, drug stores and other retail, and commercial and non-commercial establishments. Campbell Soup Company was founded in 1869 and is headquartered in Camden, New Jersey.",
        "initial_price": 37.0,
        "price_2002": 22.27,
        "price_2007": 36.4,
        "symbol": "CPB"
    },
    {
        "company": "Disney",
        "description": "The Walt Disney Company, founded in 1923, is a worldwide entertainment company, with movies, cable networks, radio networks, movie production, musical recordings and live stage plays. Disney also operates Walt Disney World in Florida and Disneyland in California, Disney Cruise Line, and international Disney resorts. Disney owns countless licenses and literary properties and publishes books and magazines.",
        "initial_price": 40.68,
        "price_2002": 15.24,
        "price_2007": 35.47,
        "symbol": "DIS"
    },
    {
        "company": "Dow Chemical",
        "description": "The Dow Chemical Company manufactures raw materials that go into consumer products and services. These materials include food and pharmaceutical ingredients, electronic displays, semiconductor packaging, water purification, insulation, adhesives, pest control, polyurethane, polystyrene (goes into plastics), and crude-oil based raw materials. Dow was founded in 1897 and is based in Midland, Michigan.",
        "initial_price": 38.83,
        "price_2002": 27.65,
        "price_2007": 44.67,
        "symbol": "DOW"
    },
    {
        "company": "Exxon Mobil",
        "description": "Exxon Mobil engages in the exploration and production of crude oil and natural gas, and manufacture of petroleum products. The company manufactures commodity petrochemicals. The company has operations in the United States, Canada/South America, Europe, Africa, Asia, and Australia/Oceania. Exxon Mobil Corporation was founded in1870 and is based in Irving, Texas.",
        "initial_price": 39.0,
        "price_2002": 32.82,
        "price_2007": 91.36,
        "symbol": "XOM"
    },
    {
        "company": "Ford",
        "description": "Ford Motor Co. develops, manufactures, sells and services vehicles and parts worldwide. Ford sells cars and trucks primarily under the Ford and Lincoln brands. It sells to consumers (through retail dealers) and to rental car companies, leasing companies, and governments. Ford also provides maintenance and repair services. Ford also offers financing to vehicle purchasers. Ford was founded in 1903 and is based in Dearborn, Michigan.",
        "initial_price": 27.34,
        "price_2002": 9.63,
        "price_2007": 8.37,
        "symbol": "F"
    },
    {
        "company": "The Gap",
        "description": "The Gap, Inc. sells retail clothing, accessories and personal care products globally under the brand names Gap, Old Navy, Banana Republic, Piperlime, Athleta and Intermix. Products include sports apparel, casual clothing, sleepwear, footwear and infants\u2019 and children\u2019s clothing. The company has company-owned stores as well as franchise stores, online stores and catalogs. The Gap was founded in 1969 and is headquartered in San Francisco, California.",
        "initial_price": 46.0,
        "price_2002": 11.56,
        "price_2007": 18.9,
        "symbol": "GPS"
    }
]

stocks_overview = get_overview(stocks_list)


if __name__ == "__main__":
    app.run(port=8080, debug=True)