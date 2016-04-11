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


def getJson(url, retry = 3, req = None):
    r = 0
    if req is None:
        req = requests
    while (r < retry):
        try:
            h = getHeader()
            #h['cookies'] = cookie
            #print h
            ret = req.get(url, headers=h, cookies=getCookies())
            return ret.text
            #time.sleep(1);
        except Exception,e :
            print e
            time.sleep(0.5)
        r += 1
    return None

def getCookies():

    cookies = {
                '_T_WM':'00f3d7e52fbb96b4c9dde5234b6aba51',
                'SUB':'_2A256B-VyDeRxGeRG61QS-C_Fzz2IHXVZC4s6rDV6PUJbrdANLWTHkW1LHesfC7i3mQX30MZOU714G0eiE0zWmQ..',
                'gsid_CTandWM':'4u9R33741UirXiAEKNJPRbM4dfb',
                '_T_WL':'1',
                '_WEIBO_UID':'2806381941',
                'SUS':'SID-2806381941-1428935102-GZ-z05gd-be25ee0f2ed9e813daceb679eb48061e',
                'SSOLoginState':'1428935102',
             }
    cookies = {
            'SUHB':'0XDkbKAghs7_ao',
            '_T_WM':'79ecab12f0d1e52b0b7e16c1f2518ee5',
            'SUB':'_2A256AmsMDeRxGeRI61cZ9SzNzDmIHXVZDXVErDV6PUJbrdANLVfAkW1LHeuD5Ar_nqMJRMGD6neZk_IrBwpM1g..',
            'gsid_CTandWM':'uVGe6b91qis1LiqF29ulaVTS2P',
            'H5_INDEX':'1',
            'H5_INDEX_TITLE':'%E9%91%AB_Darcy',
            }
    return cookies

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

