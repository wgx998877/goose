#!/usr/bin/env python
# encoding: utf-8

from pymongo import MongoClient

host = 'localhost'
port = 27017
user = 'sa'
passwd = '4619200'
conn_str = 'mongodb://%s:%s@%s:%d' % (user, passwd, host, port)

client = MongoClient(conn_str)
db = client.goose

user_list_table = db.user_list
raw_html_table = db.raw_html
weibo_content_table = db.weibo_content

if __name__ == "__main__":
    print raw_html_table.find_one()

