#!/usr/bin/env python
# -*- coding:utf-8 -*-

import pika
# ユーザー名とパスワード
credential= pika.PlainCredentials('user','pass')
# 接続パラメーター作成
connect_param = pika.ConnectionParameters(
                    host='seaof-hoge.arukascloud.io',
                    port=31402,
                    credentials=credential)
connection = pika.BlockingConnection(connect_param)
channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')
print(" [x] Sent 'Hello World!'")
connection.close()
