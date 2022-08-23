# -*- coding: utf-8 -*-
# @Time : 2022/7/28 15:00
# @Author : liuyuancai
# @File : conftest.py
# @Project : woniusales_api
import pytest

from baseapi.login import auth_login
from baseapi.variable import variable
from utility.public_fun import read_json
from utility.globalpath import host_path, user_path


def pytest_addoption(parser):
    """ 读取命令行运行环境配置
        eg：pytest --setting=prod2_terminal ...
        调试用例时 点击用例左边绿色箭头  在additional arguments 输入指定的参数
    """
    parser.addoption(
        "--tester",
        action="store",
        default="liu",
        help="assign which env to use"
    )


@pytest.fixture(scope="session", autouse=True)
def get_cmdopts(request):
    variable.host = read_json(host_path)  # 获取host
    variable.tester = request.config.getoption("--tester")  # 获取tester
    auth_login.login_sales()
