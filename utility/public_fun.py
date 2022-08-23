# -*- coding: utf-8 -*-
# @Time : 2022/7/29 11:09
# @Author : liuyuancai
# @File : public_fun.py
# @Project : woniusales_api
import json

import pymysql


def read_json(path):
    with open(path, "r") as f:
        file = json.load(f)
    return file


def crud_mysql(sql):
    # 用户名
    u = 'root'
    # 密码
    p = '123456'
    # 主机地址
    h = '127.0.0.1'
    # h="localhost:3306"
    # 需要连接的数据库名称
    d = "woniusales"
    # 使用connect方法创建一个连接
    conn = pymysql.connect(host=h, user=u, password=p, database=d)
    # 获取游标
    cur = conn.cursor()
    # 执行sql语句
    cur.execute(sql)
    # 打印结果 fetchall() 打印全部结果 fetchone()获取一条结果  fetchmany(count) 指定条数
    # print(cur.fetchall())
    # 提交sql语句
    conn.commit()
    # 关闭连接
    conn.close()
    return cur.fetchall()
