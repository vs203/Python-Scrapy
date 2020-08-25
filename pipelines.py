# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3
class LiveRatesPipeline(object):
    def __init__(self):
        self.create_connection()
        self.create_table()
    def create_connection(self):
        self.conn = sqlite3.connect("new_rate.db")
        self.curr = self.conn.cursor()
    def create_table(self):
        self.curr.execute("""
             DROP TABLE IF EXISTS live_rate_tb""")
        self.curr.execute(""" create table live_rate_tb (
                Description text,
                Rate text,
                Previous_close text )
        """)
    def process_item(self, item, spider):
        self.store_db(item)
        return item
    def store_db(self,item):
        for i in range(20):
            self.curr.execute(""" insert into live_rate_tb values( ?,?,?)""",(
                item['Description'][i],
                item['Rate'][i],
                item['Previous_Close'][i]
                          ) )
            self.conn.commit()
        


