# Time: 2021/8/20 19:04
# Author: jiangzhw
# FileName: test_add_recruitment_pro.py
from page.add_recruitment_pro import AddRecruitmentPro


class TestAddRecruitmentPro:
    """新建招聘项目 case"""

    def setup(self):
        self.add_recruitment_pro = AddRecruitmentPro()

    def test_set_online_time(self):
        self.add_recruitment_pro.set_online_time("2021-09-01", "00:00:00", "2022-09-01", "00:00:00")

    def teardown(self):
        self.add_recruitment_pro.close(timeout=15)
