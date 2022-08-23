# -*- coding: utf-8 -*-
# @Time : 2022/7/28 15:01
# @Author : liuyuancai
# @File : member_manage.py
# @Project : woniusales_api
from baseapi.api_server import api_total


class Member_manage:

    def add_member(self, data):
        """会员新增"""
        url = "/WoniuSales_20180508_V1.4_bin/customer/add"
        # _data = {"customername": data["customername"], "customerphone": data["customerphone"],
        #          "childsex": data["childsex"], "childdate": data["childdate"], "creditkids": 0,
        #          "creditcloth": 0}
        _data = f"customername={data['customername']}&customerphone={data['customerphone']}" \
                f"&childsex={data['childsex']}&childdate={data['childdate']}&creditkids=0&creditcloth=0"
        _data = _data.encode("utf-8")
        header = "application/x-www-form-urlencoded; charset=UTF-8"
        return api_total.api_swagger("post", url, _data, headers=header)
