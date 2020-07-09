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
rh.login(username="braypolk@comcast.net", password="")
profile = rh.load_account_profile()
print(profile)
# TODO: get the cash held by robinhood and check to see if enough money is in account

# test price will be 1 cent
stockInfo = rh.find_instrument_data(stockChoice)
rh.order_buy_fractional_by_price(stockChoice, 0.01)
# TODO: need to test for error if stock is invalid
print("printing stock Info from robinhood")
print(stockInfo)
