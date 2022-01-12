# Time: 2021/12/28 20:59
# Author: jiangzhw
# FileName: test_class.py
import pytest


class TestClass:
    def test_one(self):
        x = "this"
        print("测试调试信息1")
        assert "h" in x

    @pytest.mark.mmm
    def test_two(self):
        x = "hello"
        print("测试调试信息2")
        assert hasattr(x, "check")

    def test_three(self):
        x = "keys"
        assert "k" in x
