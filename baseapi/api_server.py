# -*- coding: utf-8 -*-
# @Time : 2022/7/28 15:43
# @Author : liuyuancai
# @File : api_server.py
# @Project : woniusales_api
from baseapi.variable import variable
from utility.client import base_page


class Apiservice:

    def api_swagger(self, method, url, params=None, headers=None, host=None, who=None):
        if who is None:
            who = "user"
        header = {"Cookie": variable.token[who], "Content-Type": "application/json"}
        if headers is not None:
            header["Content-Type"] = headers
        return base_page.run_request(method, url, params, header, host)


api_total = Apiservice()
