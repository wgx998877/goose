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
import chardet


def main():
    #parse()
    show()

def show():
    r = db.weibo_content_table.find()
    f = open('goose', 'w')
    for i in r:
        i = i['content']
        f.write(i[3:] + '\n')

def parse(save = False):
    r = db.raw_html_table.find()
    cnt = 0
    for i in r:
        content = i['content']
        soup = bs(content, 'lxml')
        #s = soup.find_all("span", class_='ctt')
        s = soup.find_all("div", class_='c')
        for j in s:
            #print j
            c = j.find("span", class_='ctt')
            t = j.find("span", class_='ct')
            if c and c.string:
                aw = c.string
                tm = t.string.split(' ')[0]
                if aw[1] == u'评':
                    #aw = aw.encode('utf8')
                    #tm = tm.encode('utf8')
                    tag = 'evaluate'
                    ret = {
                            'origin_time': tm,
                            'content': aw,
                            'tag': tag
                            }
                    if save:
                        db.weibo_content_table.save(ret)
                    cnt += 1
                    print cnt


if __name__ == "__main__":
    main()
