# -*- coding: utf-8 -*-
# @Time : 2022/7/28 15:05
# @Author : liuyuancai
# @File : client.py
# @Project : woniusales_api
import requests
from utility.custom_log import log
from baseapi.variable import variable


class Base_page:
    @log
    def run_request(self, method, url, data, headers, host=None):
        if host is None:
            url = variable.host["qa_host"] + url
        else:
            url = variable.host[host] + url
        pidata = {"url": url, "headers": headers, "verify": False}
        if method == 'get':
            pidata["params"] = data
            res = requests.get(**pidata)
        elif method == 'put':
            pidata["data"] = data
            res = requests.put(**pidata)
        elif method == 'delete':
            res = requests.delete(**pidata)
        else:
            pidata["data"] = data
            res = requests.post(**pidata)
        return res


base_page = Base_page()
