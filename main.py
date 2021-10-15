import requests
from flask import Flask
from flask import render_template

app = Flask(__name__)

URL = "https://min-api.cryptocompare.com/data/v2/histominute?fsym={}&tsym={}&limit={}"

def get_price(coin,currency,limit):
    sum = 0
    try:
        response = requests.get(URL.format(coin,currency,limit)).json()
        for i in range(10):
            sum += response['Data']['Data'][i]['close']
        data = {'price': response['Data']['Data'][9]['close'], 'average': sum/10}
        return data
    except:
        return False


@app.route("/")
def hello_world():
    currencyPrice = get_price("BTC","USD","10")
    if currencyPrice:
        return render_template("index.html",data=currencyPrice)

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000)

