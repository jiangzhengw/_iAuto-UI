# Time: 2021/6/4 17:25
# Author: jiangzhw
# FileName: test_case_demo2.py
from pageObject.index import Index


class TestCase2:
    """test case"""

    def setup(self):
        """setup fixture"""
        self.index = Index()

    def test_demo1(self):
        """demo case"""
        msg = "111"
        self.index.search(msg)

    def test_demo2(self):
        """demo case"""
        msg = "222"
        self.index.search(msg)

    def teardown(self):
        """teardown fixture"""
        self.index.close()
