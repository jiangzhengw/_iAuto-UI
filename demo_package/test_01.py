# Time: 2021/12/29 0:00
# Author: jiangzhw
# FileName: test_01.py
import sys

import pytest


@pytest.mark.xfail(sys.platform == "win32", reason="no reason")
class TestCase1(object):
    def test_1(self):
        print("测试用例1")

    def test_2(self):
        print("测试用例2")


class TestCase2(object):
    def test_3(self):
        print("测试用例3")

    @pytest.mark.flaky(reruns=2, reruns_delay=1)
    def test_4(self):
        print("测试用例4")
        assert 1 + 2 == 33


@pytest.mark.xfail(reason="no reason", strict=True)
def test_5():
    print('执行测试用例5')
# @pytest.mark.smoke
# def test_02():
#     print(sys.platform)
