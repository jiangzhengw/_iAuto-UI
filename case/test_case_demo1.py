# Time: 2021/6/2 14:57
# Author: jiangzhw
# FileName: test_case_demo1.py
from pageObject.index import Index


class TestCase:
    """test case"""

    def setup(self):
        """setup fixture"""
        self.index = Index()

    def test_demo1(self):
        """demo case"""
        msg = "哈哈哈"
        self.index.search(msg)

    def test_demo2(self):
        """demo case"""
        msg = "你猜我猜不猜"
        self.index.search(msg)

    def teardown(self):
        """teardown fixture"""
        self.index.close()
