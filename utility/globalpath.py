# -*- coding: utf-8 -*-
# @Time : 2022/7/29 10:44
# @Author : liuyuancai
# @File : globalpath.py
# @Project : woniusales_api
import os

base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 项目的根目录
host_path = os.path.join(base_path, "utility/config.json")  # 配置的host地址
user_path = os.path.join(base_path, "Test_data/user.json")
