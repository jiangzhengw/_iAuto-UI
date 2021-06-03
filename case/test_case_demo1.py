# Time: 2021/6/2 14:57
# Author: jiangzhw
# FileName: test_case_demo1.py
from page.index import Index


class TestCase:
    """test case"""

    def setup(self):
        """setup fixture"""
        self.index = Index()

    def test_demo1(self):
        """demo case"""
        self.index.login()

    def teardown(self):
        """teardown fixture"""
        self.index.close()
