import json, hmac, hashlib, time, requests, base64
from requests.auth import AuthBase
import linecache
import sys

from datetime import datetime, timedelta

import urllib3
urllib3.disable_warnings()

import math

api_url = 'https://api.pro.coinbase.com/'

class CoinbaseExchangeAuth(AuthBase):
    def __init__(self, api_key, secret_key, passphrase):
        self.api_key = api_key
        self.secret_key = secret_key
        self.passphrase = passphrase

    def __call__(self, request):
        timestamp = str(time.time())
        message = timestamp + request.method + request.path_url + (request.body or '')
        hmac_key = base64.b64decode(self.secret_key)
        signature = hmac.new(hmac_key, message.encode('utf-8'), hashlib.sha256)
        signature_b64 = base64.b64encode(signature.digest())

        request.headers.update({
            'CB-ACCESS-SIGN': signature_b64,
            'CB-ACCESS-TIMESTAMP': timestamp,
            'CB-ACCESS-KEY': self.api_key,
            'CB-ACCESS-PASSPHRASE': self.passphrase,
            'Content-Type': 'application/json'
        })
        return request

def getbalance(acct,auth):
    r = requests.get(api_url + 'accounts/' + acct, auth=auth)
    r = r.json()
    return(float(r['balance']))

def getpriceticker(product,auth):
    r = requests.get(api_url + 'products/' + product + '/ticker', auth=auth)
    r = r.json()
    return(float(r['price']))

def getpricemidmarket(product,auth):
    tryingToGet = True
    while tryingToGet:
        req = api_url + 'products/' + product + '/book'
        try:
            r = requests.get(req,auth = auth)
            r = r.json()
            current = (float(r['bids'][0][0]) + float(r['asks'][0][0]))/float(2)
            tryingToGet = False
        except Exception as e:
            print('Exception:')
            print(e)
            dotPause(1,True)
            tryingToGet = True

    return(current)

# Market orders fill immediately and are takers.

# Size is quote (target) currency.

def buyproductmarket(product,amount,auth):
    order = {
        'type'          : 'market',
        'side'          : 'buy',
        'size'          : amount,
        'product_id'    : product
    }
    r = requests.post(api_url + 'orders', json = order, auth = AUTH)
    r = r.json()
    return(r)

def sellproductmarket(product,amount,auth):
    order = {
        'type'          : 'market',
        'side'          : 'sell',
        'size'          : amount,
        'product_id'    : product
    }
    r = requests.post(api_url + 'orders', json = order, auth = AUTH)
    r = r.json()
    return(r)

# Limit orders go in the order book and will be filled when they can
# This means:
# * A limit buy is below market price and will buy
#   when someone is willing to sell at that price or lower.

def buyproductlimit(product,amount,buyprice,auth):
    order = {
        'type'          : 'limit',
        'side'          : 'buy',
        'price'         : buyprice,
        'size'          : amount,
        'product_id'    : product
    }
    r = requests.post(api_url + 'orders', json = order, auth = AUTH)
    r = r.json()
    return(r)

# * A limit sell is above market price and will sell
#   when someone is willing to buy at that price or higher.

def sellproductlimit(product,amount,sellprice,auth):
    order = {
        'type'          : 'limit',
        'side'          : 'sell',
        'price'         : sellprice,
        'size'          : amount,
        'product_id'    : product
    }
    r = requests.post(api_url + 'orders', json = order, auth = AUTH)
    r = r.json()
    return(r)

# Stop limit orders.
# A stop limit order is a type of order that becomes a limit order
# when the stop price is reached, but is canceled if the price goes too far.
# * Stop limit sell: 1BTC, stop = 30000, limit = 29990
#   When price hits 30000 becomes a limit sell and will attempt to sell 1BTC
#   at or above 29990.
# nb. 'stop' : 'entry' triggers when the last trade price is at or above stop_price.

def sellproductstoplimit(product,amount,stopprice,limitprice,auth):
    order = {
        'product_id'    : product,
        'side'          : 'sell',
        'type'          : 'limit',
        'size'          : amount,
        'stop'          : 'entry',
        'stop_price'    : stopprice,
        'price'         : limitprice
    }
    r = requests.post(api_url + 'orders', json = order, auth = AUTH)
    r = r.json()
    return(r)

# * Stop limit buy: 1BTC, stop = 25000, limit = 25100
#   When price hits 25000 becomes a limit buy and will attempt to buy 1BTC
#   at or below $25100.
# nb. 'stop' : 'loss' triggers when the last trade price is at or below stop_price.

def buyproductstoplimit(product,amount,stopprice,limitprice,auth):
    order = {
        'product_id'    : product,
        'side'          : 'buy',
        'type'          : 'limit',
        'size'          : amount,
        'stop'          : 'loss',
        'stop_price'    : stopprice,
        'price'         : limitprice
    }
    r = requests.post(api_url + 'orders', json = order, auth = AUTH)
    r = r.json()
    return(r)
