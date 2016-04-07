#!/usr/bin/env python
# encoding: utf-8

from pymongo import MongoClient

host = 'localhost'
port = 27017

client = MongoClient(host, port)
db = client.goose

user_list_table = db.user_list
raw_html_table = db.raw_html
weibo_content_table = db.weibo_content


