import coinbasestuff as cb
import time
import sys
import linecache

API_KEY = 'YOU FILL IN'
API_SECRET = 'YOU FILL IN'
API_PASS = 'YOU FILL IN'

auth = cb.CoinbaseExchangeAuth(API_KEY, API_SECRET, API_PASS)

mmp = [0]
mmpold = cb.getpricemidmarket('BTC-USD',auth)
while True:
    time.sleep(1)
    try:
        mmpnew = cb.getpricemidmarket('BTC-USD',auth)
        mmp.append(mmpold - mmpnew)
        mmpold = mmpnew
        if len(mmp) > 60:
            mmp.pop(0)

        # Find the MCS.

        maxoverall = mmp[0]
        start = 0
        end = 0
        tempstart = 0
        tempend = 0
        maxendingati = mmp[0]
        for i in range(1,len(mmp)):
            if maxendingati + mmp[i] > mmp[i]:
                maxendingati = maxendingati + mmp[i]
                tempend = i
            else:
                maxendingati = mmp[i]
                tempstart = i
                tempend = i
            if maxendingati > maxoverall:
                maxoverall = maxendingati
                start = tempstart
                end = tempend

        print("{:+.2f}".format(maxoverall) + ' over a ' + str(end-start+1) + ' second interval in the last minute.')

    except Exception as e:
        exc_type, exc_obj, tb = sys.exc_info()
        f = tb.tb_frame
        lineno = tb.tb_lineno
        filename = f.f_code.co_filename
        linecache.checkcache(filename)
        line = linecache.getline(filename, lineno, f.f_globals)
        print('EXCEPTION IN ({}, LINE {} "{}"): {}'.format(filename, lineno, line.strip(), exc_obj))
