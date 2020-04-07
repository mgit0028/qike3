# -*- coding: UTF-8 -*-

import pymysql
# 建库
try:
    conn=pymysql.connect(
        host='localhost',
        port=3306,
        user='u0_a169',
        passwd='',
    )
    cur=conn.cursor()
    create_database_sql='CREATE DATABASE IF NOT EXISTS py3_tstgr DEFAULT CHARSET utf8 COLLATE utf8_general_ci;'
    cur.execute(create_database_sql)
    cur.close()
    print('创建数据库 py3_tstgr 成功！')
except pymysql.Error as e:
    print('pymysql.Error: ',e.args[0],e.args[1])