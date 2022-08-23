# -*- coding: utf-8 -*-
# @Time : 2022/7/28 14:58
# @Author : liuyuancai
# @Email : wayne_lau@aliyun.com
# @File : login.py
# @Project : woniusales_api
from baseapi.variable import variable
from utility.client import base_page
from utility.globalpath import user_path
from utility.public_fun import read_json


class Login:

    def login_sales(self):
        for i, j in read_json(user_path)[variable.tester].items():
            variable.user[i] = j
            variable.account, variable.password = j[0], j[1]
            url = "/WoniuSales_20180508_V1.4_bin/user/login"
            data = {"username": j[0], "password": j[1], "verifycode": "0000"}
            _test = base_page.run_request("post", url, data, None, None)
            cookie = _test.headers["Set-Cookie"][:44]
            variable.token[i] = cookie


auth_login = Login()
