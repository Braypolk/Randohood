import robin_stocks as rh
import json
import random

# import stocks from json file and choose random stock
with open('../stocks.json') as json_file:
    stocks = json.load(json_file)
stockChoice = random.choice(stocks)
print("Random stock from stocks.json")
print(stockChoice)

# login to users Robinhood account and purchase $5 worth of stock
# TODO: get user info from sign in
# password = input("Enter Password: ")
password = "Bray8951!"
rh.login(username="braypolk@comcast.net", password="")
profile = rh.load_account_profile()

stockInfo = rh.find_instrument_data(stockChoice)
if(stockInfo[0].get('fractional_tradability') == "tradable"):
    print("SUCCESS")
    # print(rh.order_buy_fractional_by_price(stockChoice, 1.00, 'ioc'))
# print(rh.order("TEUM", 1, 'market', 'immediate','buy', None, None, 'gtc', False))
print("printing stock Info from robinhood")
print(stockInfo)
