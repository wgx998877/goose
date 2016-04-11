#!/usr/bin/env python
# encoding: utf-8

import requests
import json
from dataapi import Client

def main():
    client = Client()
    client.init('ed109e5b2acd1026f1ed8f9f9f4569ce8e32ba02c253b8d42606d74b46909814')
    print 'init ok'
    url = '/api/subject/getNewsByTickers.json?field=&secID=&exchangeCD=&ticker=600000&secShortName=&beginDate=20150301&endDate=20150305'
    code, result = client.getData(url)
    print code
    print result
'''
    s = getStock('600026.XSHG', '600026')
    print s
def getStock(secid, ticker, equType='A'):
    url = 'http://apis.baidu.com/wxlink/getequ/getequ?secID=%s&ticker=%s&equTypeCD=%s&field=primeOperating' % (secid, ticker, equType)
    header = {'apikey':'3543127ea13dfa10841f8cb7441428d2'}
    r = requests.get(url, headers=header)
    return r.text
'''

if __name__ == "__main__":
    main()
