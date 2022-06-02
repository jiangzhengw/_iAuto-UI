# Time: 2021/8/27 18:06
# Author: jiangzhw
# FileName: test_main.py
from page.main import Main


class TestMain:
    """Main case"""

    def setup(self):
        self.main = Main()

    def test_set_online_time(self):
        self.main.resume_click()

    def teardown(self):
        self.main.close()
