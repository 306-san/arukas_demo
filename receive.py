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
# コネクション作成
connection = pika.BlockingConnection(connect_param)
channel = connection.channel()

channel.queue_declare(queue='hello')

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
