import robin_stocks as rh
import json
import random
import os
import requests
import logging
from flask import Flask, render_template, request, url_for, redirect, Response

code = 0

app = Flask(__name__)
@app.route("/")
def home():
    return redirect(url_for('login'))

@app.route("/login", methods=['GET','POST'])
def login():
    if request.method == 'POST':
        try:
            rh.login(username=request.form['username'], password=request.form['password'], expiresIn=3000, scope="internal" ,by_sms=True, store_session=False)
        except:
            return render_template('index.html')
        # TODO: store session should be false for final
        # TODO: need to deal with 2FA
        profile = rh.load_account_profile()
        return redirect(url_for('purchase'))
    return render_template('index.html')

@app.route("/purchase", methods=['GET','POST'])
def purchase():  
    amount = 1.00
    if request.method == 'POST':
        amount = request.form['userDefAmount']
    # import stocks from json file and choose random stock
    stocks = requests.get('https://dumbstockapi.com/stock?format=tickers-only&exchange=NASDAQ').json()
    stockChoice = random.choice(stocks)
    print(stockChoice)
    # timeInForce must be gfd
    # purchase = rh.order_buy_fractional_by_price(symbol=stockChoice, amountInDollars=amount, timeInForce='gfd')
    # price = purchase["price"]
    price=""
    return render_template("overview.html", randomStock=stockChoice, dollarAmountPurchased=amount, purchasePrice=price)

@app.route("/logout")
def logout():
    rh.logout()
    return redirect(url_for('login'))

@app.route("/multifactor", methods=['GET','POST'])
def multifactor():
    if request.method == 'POST':
        global code
        code = request.form['code']
    return render_template('check.html')

def check():
    redirect(url_for('multifactor'))
    return code

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)), debug=True)