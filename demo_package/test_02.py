# Time: 2021/12/29 0:00
# Author: jiangzhw
# FileName: test_02.py
import pytest


def test_02(fixturedemo):
    print('执行test_02测试用例2')


@pytest.mark.xfail()
def test_01():
    print("执行test_02测试用例1")


def tes_01():
    print("测试用例tes01")
