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
from util import getHtml, getHeader
from bs4 import BeautifulSoup as bs

def main():
    r = getUserWeibo()

def getUserList(f = 'user.txt'):
    r = open(f).readlines()
    return r

def getUserWeibo(req=requests):
    user = getUserList()
    for u in user:
        print u,'begin'
        u = u.strip()
        base_url = 'http://weibo.cn/%s?filter=1&page=' % u
        print base_url
        pagenum = 200
        getnum = False
        i = 1
        while i <= pagenum:
            url = base_url + str(i)
            print url
            try:
                if getnum == False:
                    r = getHtml(url, '', req = req, save = 'db', tag='second')
                    pagenum = getPageNum(r)
                    getnum = True
            except:
                pass
            i += 1
        print u,'done'
    return r

def getPageNum(html):
    soup = bs(html)
    page = soup.find(id='pagelist').find(type='hidden')
    pagenum = page['value']
    pagenum = int(pagenum)
    return pagenum


def crawlGooseUserList():
    #this function useless, need to login first
    req = loginWeibo()
    #req = requests
    base_url = 'http://d.weibo.com/230771_-_EXPERTUSER?page=%d#Pl_Core_F4RightUserList__4'
    page_num = 22
    for page_index in range(1, page_num):

        url = base_url % page_index
        path = 'tmp'
        r = getHtml(url, path, req = req, save = 'db')
        print r
        break


def loginWeibo():
    #this function useless, ai...
    username = ''
    passwd = ''
    postData = {
            'username' : username,
            'password' : passwd
            }
    loginpostUrl = 'http://passport.weibo.cn/signin/login'
    headers = {
            'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Host' : 'passport.weibo.cn',
            'User-Agent' : 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.23 Mobile Safari/537.36',
            'Cookie' : '_T_WM=8d2276960cb86ea6080a9f03161404b4'
            }
    req = requests.Session()

    u = req.post(loginpostUrl, data = postData, headers=headers)
    cookies = u.cookies
    print cookies
    print u.text
    return req

if __name__ == "__main__":
    main()
