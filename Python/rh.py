import robin_stocks as rh
import json
import random

# import stocks from json file and choose random stock
with open('../stocks.json') as json_file:
    stocks = json.load(json_file)
stockChoice = random.choice(stocks)
print(stockChoice)

# login to users Robinhood account and purchase $5 worth of stock
# TODO: get user info from sign in
rh.login("braypolk@comcast.net")
profile = rh.load_account_profile()

stockInfo = rh.find_instrument_data(stockChoice)
if(stockInfo[0].get('fractional_tradability') == "tradable"):
    print("SUCCESS")
    # timeInForce must be gfd
    print(rh.order_buy_fractional_by_price(symbol=stockChoice, amountInDollars=1.00, timeInForce='gfd'))
