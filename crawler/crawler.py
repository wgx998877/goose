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
    #crawlGooseUserList()
    url = 'http://weibo.com/aitangming'
    r = getUserWeibo(url)
    print r

def getUserWeibo(url):
    r = getHtml(url, '', save = db)
    return r

def crawlGooseUserList():
    #req = loginWeibo()
    req = requests
    base_url = 'http://d.weibo.com/230771_-_EXPERTUSER?page=%d#Pl_Core_F4RightUserList__4'
    page_num = 22
    for page_index in range(1, page_num):

        url = base_url % page_index
        path = 'tmp'
        r = getHtml(url, path, req = req, save = 'db')
        print r
        break




def loginWeibo():
    username = 'wgx998877@gmail.com'
    passwd = 'wgx4619200'
    weiboUrl = 'http://weibo.cn/pub/'
    loginUrl  = bs(requests.get(weiboUrl).content).find("div",{"class":"ut"}).find("a")['href']
    origInfo  = bs(requests.get(loginUrl).content)
    loginInfo = origInfo.find("form")['action']
    loginpostUrl = 'http://login.weibo.cn/login/'+loginInfo
    headers = { 'Host': 'login.weibo.cn',
            'User-Agent' : 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; BOIE9;ZHCN)',
            'Referer' : 'http://login.weibo.cn/login/?ns=1&revalid=2&backURL=http%3A%2F%2Fweibo.cn%2F&backTitle=%D0%C2%C0%CB%CE%A2%B2%A9&vt=',
           }
    postData = { 'mobile': username,
             origInfo.find("form").find("input",{"type":"password"})['name']: passwd,
             'remember':'on',
             'backURL':origInfo.find("form").find("input",{"name":"backURL"})['value'],
             'backTitle': origInfo.find("form").find("input",{"name":"backTitle"})['value'],
             'tryCount': origInfo.find("form").find("input",{"name":"tryCount"})['value'],
             'vk': origInfo.find("form").find("input",{"name":"vk"})['value'],
             'submit': origInfo.find("form").find("input",{"name":"submit"})['value'],
             }
    req = requests.Session()
    u = req.post(loginpostUrl, data = postData, headers=headers)
    cookies = u.cookies
    print cookies
    print u.text
    return req

if __name__ == "__main__":
    main()
