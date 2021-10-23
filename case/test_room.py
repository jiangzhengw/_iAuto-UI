# Time: 2021/10/23 20:49
# Author: jiangzhw
# FileName: test_room.py

class TestRoom:
    """Main case"""

    def setup(self):
        self.main = Main()

    def test_set_online_time(self):
        self.main.resume_click()

    def teardown(self):
        self.main.close()