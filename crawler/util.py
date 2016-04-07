#!/usr/bin/env python
# encoding: utf-8
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import os
import time
import random
import requests
import datetime
import db

def getHtml(url, path, retry = 3, req = None, ignoreFile = False, save='file', tag = ''):
    ret = getJson(url, retry, req)
    if ret is None:
        return False
    if save == 'file':
        if os.path.exists(path) and ignoreFile == False:
            f = open(path).read()
            if len(f) > 500:
                return False
        saveStr2File(ret, path)
    elif save == 'db':
        saveStr2Db(ret, url, tag=tag)
    return ret

def saveStr2Db(ret, url, table='raw_html', tag = ''):
    if ret is None or ret == '':
        return False
    d = {
            'url':url,
            'content':ret,
            'tag':tag,
            'date':datetime.datetime.now(),
            }
    try:
        collection = db.db[table]
        r = collection.insert(d)
        return r
    except:
        return False


def saveStr2File(content, path):
    fo = open(path, 'w')
    fo.write(content)
    return True

cookie = 'YF-Ugrow-G0=3a02f95fa8b3c9dc73c74bc9f2ca4fc6; login_sid_t=10d5ae9758bc06dd89c2959cb0be5e90; _s_tentry=-; Apache=1285878793156.5852.1460015367078; SINAGLOBAL=1285878793156.5852.1460015367078; ULV=1460015367083:1:1:1:1285878793156.5852.1460015367078:; SUS=SID-2605852175-1460015535-GZ-asfvm-841584dbfc965df320154190155ea992; SUE=es%3Da5d4dc8ab4d179645fa4407132b38609%26ev%3Dv1%26es2%3De1327c6d7af912b212ad5a455a63a9d0%26rs0%3DKcrrkA%252Bn26hB3m7tuyyuqngoLKAgt%252BBu1v3v%252F%252B26sfZkB%252BcQDPwcVWG2kOUw01gq3TB9qDfEsAOTAM4kiUX3nD1CjHfGkoIr78iC8LWRgYIw5zbiiLLxgTkwKlU9FFwAD%252Bi0hyqw0b2L%252BZHsjjWJo7nwjUAt%252Bhf11T2TsWcDlnc%253D%26rv%3D0; SUP=cv%3D1%26bt%3D1460015535%26et%3D1460101935%26d%3Dc909%26i%3Da992%26us%3D1%26vf%3D0%26vt%3D0%26ac%3D0%26st%3D0%26uid%3D2605852175%26name%3Dwgx998877%2540gmail.com%26nick%3D%25E7%258E%258B%25E5%259B%25BD%25E9%2591%25AB998877%26fmp%3D%26lcp%3D2015-01-08%252000%253A57%253A56; SUB=_2A256AmH_DeRxGeRI61cZ9SzNzDmIHXVZdtQ3rDV8PUNbuNBeLWr1kW9LHeuL11u_2la2lTUGY1nYMEO9QpvISw..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9Whk3Fl-OL4YRyhbG2Hxkjgp5JpX5K2t; SUHB=0xnDJi5mVnwHej; ALF=1491551532; SSOLoginState=1460015535; un=wgx998877@gmail.com'

def getJson(url, retry = 3, req = None):
    r = 0
    if req is None:
        req = requests
    while (r < retry):
        try:
            h = getHeader()
            h['cookies'] = cookie
            ret = req.get(url, headers=h)
            return ret.text
            #time.sleep(1);
        except Exception,e :
            print e
            time.sleep(0.5)
        r += 1
    return None

def getHeader():
    header = {
        "User-Agent":"Mozilla/5.0 (Windows NT 5.1; rv:37.0) Gecko/20100101 Firefox/37.0"
    }
    userAgent=[
    "Mozilla/5.0 (Windows NT 5.1; rv:37.0) Gecko/20100101 Firefox/37.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; GTB7.0)",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1",
    "Opera/9.80 (Windows NT 6.1; U; zh-cn) Presto/2.9.168 Version/11.50",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36"
    ]
    header["User-Agent"] = random.choice(userAgent)
    return header

