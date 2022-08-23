# -*- coding: utf-8 -*-
# @Time : 2022/7/29 15:41
# @Author : liuyuancai
# @File : test_member_manage.py
# @Project : woniusales_api
from baseapi.variable import variable
from baseapi.All_api import all_api
from utility.public_fun import crud_mysql


def test_01():
    data = all_api.add_member(
        {"customername": "我我我", "customerphone": "13652469851", "childsex": "男",
         "childdate": "1994-11-02"})
    a = crud_mysql("delete from customer where customername='我我我'")
    for i in a:
        if "我我我" not in i:
            assert 1 == 1
