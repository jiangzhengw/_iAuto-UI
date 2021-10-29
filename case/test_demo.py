# Time: 2021/10/28 19:45
# Author: jiangzhw
# FileName: test_demo.py
from page.demo import Demo


class TestMain:
    """Main case"""

    def setup(self):
        self.demo = Demo(is_login=False)

    def test_set_online_time(self):
        self.demo.switch_to_frame()

    # def teardown(self):
        # self.demo.close(100)
