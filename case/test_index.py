# Time: 2021/6/15 17:57
# Author: jiangzhw
# FileName: test_index.py
from pageobj.index import Index


class TestCase1:
    """test case"""

    def setup(self):
        """setup fixture"""
        self.index = Index()

    def test_login(self):
        self.index.login()

    def teardown(self):
        """teardown fixture"""
        self.index.close()
