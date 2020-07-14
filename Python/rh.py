import robin_stocks as rh
import json
import random
import requests
from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)
@app.route("/")
def home():
    return redirect(url_for('login'))

@app.route("/login", methods=['GET','POST'])
def login():
    if request.method == 'POST':
        # TODO: store session should be false for final
        print(rh.login(username=request.form['username'], password=request.form['password'], expiresIn=3000, scope="internal" ,by_sms=True, store_session=True))
        # TODO: need to deal with 2FA
        profile = rh.load_account_profile()
        return redirect(url_for('purchase'))
    return render_template('index.html')

@app.route("/purchase")
def purchase():
    # import stocks from json file and choose random stock
    with open('../stocks.json') as json_file:
        stocks = json.load(json_file)
    stockChoice = random.choice(stocks)
    print(stockChoice)
    print("SUCCESS")
    amount = 1.00
    # timeInForce must be gfd
    # purchase = rh.order_buy_fractional_by_price(symbol=stockChoice, amountInDollars=amount, timeInForce='gfd')
    # price = purchase["price"]
    price=""
    return render_template("overview.html", randomStock=stockChoice, purchasePrice=price, dollarAmountPurchased=amount)

@app.route("/logout")
def logout():
    rh.logout()
    return redirect(url_for('login'))

if __name__ == "__main__":
    # app.run(debug = True)
    app.run(host='0.0.0.0', port=3245, debug=True)