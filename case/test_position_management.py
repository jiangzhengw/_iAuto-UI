# Time: 2021/8/25 12:27
# Author: jiangzhw
# FileName: test_position_management.py
import pytest

from page.position_management import PositionManagement


class TestPositionManagement:
    """职位管理 case"""

    def setup(self):
        self.position_management = PositionManagement()

    @pytest.mark.set_online_time
    @pytest.mark.P0
    def test_set_online_time(self):
        data = {
            'start_date': '2021-09-01',
            'start_time': '00:00:00',
            'end_date': '2022-09-01',
            'end_time': '00:00:00'
        }
        self.position_management.switch_project()
        self.position_management.back_to_project()
        add_page = self.position_management.add_icon_click()
        add_page.set_online_time(data['start_date'], data['start_time'], data['end_date'], data['end_time'])

    @pytest.mark.set_online_time
    @pytest.mark.P3
    def test_set_online_time02(self):
        pass

    @pytest.mark.new_recruit_project
    @pytest.mark.P0
    def test_new_recruit_project(self):
        data = {
            'name': 'UI自动化测试-姜正炜-01',
            'start_date': '2021-09-01',
            'start_time': '00:00:00',
            'end_date': '2022-09-01',
            'end_time': '00:00:00'
        }
        self.position_management.switch_project()
        self.position_management.back_to_project()
        add_page = self.position_management.add_icon_click()
        add_page.input_pro_name(data['name'])
        add_page.set_online_time(data['start_date'], data['start_time'], data['end_date'], data['end_time'])
        add_page.set_done_click()

    def teardown(self):
        self.position_management.close(timeout=10)
