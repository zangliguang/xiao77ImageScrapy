# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
import pymysql.cursors
import uuid
import datetime


class Xiao77Pipeline(object):
    def process_item(self, item, spider):
        return item


class imagePipLine(object):
    def __init__(self):
        self.conn = pymysql.connect(host='localhost', user='root', passwd='', db='db_liguang_se', port=3306,
                                    charset='utf8')
        self.cur = self.conn.cursor()  # 获取一个游标
        self.insertsql = "INSERT INTO image_info (image_id, image_title,image_type,image_link_head,image_link_tail,image_date,image_count,image_create_time) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"

    def process_item(self, item, spider):
        # sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
        # cursor.execute(sql, ('webmaster@python.org', 'very-secret'))
        self.cur.execute("SET NAMES utf8")
        print("-----" + str(item['image_id']) + "-----")
        print("-----" + item['image_title'] + "-----")
        print("-----" + item['image_type'] + "-----")
        print("-----" + item['image_link_head'] + "-----")
        print("-----" + item['image_link_tail'] + "-----")
        print("-----" + item['image_date'] + "-----")
        print("-----" + str(item['image_count']) + "-----")
        self.cur.execute(self.insertsql, (
            str(item['image_id']), str(item['image_title']), item['image_type'], item['image_link_head'],
            item['image_link_tail'],
            item['image_date'], int(item['image_count']), datetime.datetime.now()))
        self.conn.commit()
        print('*****************************')

        # self.cur.close()  # 关闭游标
        # self.conn.close()  # 释放数据库资源
        return item
