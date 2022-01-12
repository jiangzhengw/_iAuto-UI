# Time: 2022/1/12 22:56
# Author: jiangzhw
# FileName: test_03.py
import pytest


@pytest.mark.flaky(reruns=2, reruns_delay=3)
def test_case1():
    print("执行测试用例1")
    assert 1 + 1 == 3


def test_case2():
    print("执行测试用例2")
    assert 1 + 3 == 6


def test_case3():
    print("执行测试用例3")
    assert 1 + 3 == 4
