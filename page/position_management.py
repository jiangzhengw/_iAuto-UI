# Time: 2021/8/20 17:32
# Author: jiangzhw
# FileName: position_management.py
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By

from common.common import get_ini_config
from page.add_recruitment_pro import AddRecruitmentPro
from page.base_page import BasePage


class PositionManagement(BasePage):
    """职位管理 page"""
    _base_url = get_ini_config('position_management')

    def switch_project(self, pro_type='school'):
        """
        切换到其他招聘类型
        :param pro_type:切换项目类型
        :return:null
        """
        switch_ele = (By.CSS_SELECTOR, 'span.type-text')
        school = (By.CSS_SELECTOR, 'i.project-types-school')
        briefcase = (By.CSS_SELECTOR, '.icon-briefcase')
        self.hover_element(switch_ele)
        if pro_type == 'school':
            self.find_element(school).click()
        elif pro_type == '实习':
            self.find_element(briefcase).click()

    def add_icon_click(self):
        """点击新建按钮"""
        add_icon = (By.CSS_SELECTOR, '.ico-plus')
        self.find_element(add_icon).click()
        return AddRecruitmentPro(self._driver)

    def open_recruitment_project(self, project_name):
        """
        打开指定招聘项目
        :param project_name:项目名称
        :return:null
        """
        pro_name = (By.LINK_TEXT, project_name)
        self.find_element(pro_name).click()
        return_pro = (By.CSS_SELECTOR, 'a.link-green.mr2')
        self.wait(10, return_pro)

    def back_to_project(self):
        """返回项目列表"""
        back = (By.CSS_SELECTOR, 'a.link-green.mr2')
        attempts = 0
        while attempts < 2:
            try:
                self.find_element(back).click()
                break
            except StaleElementReferenceException:
                attempts += 1
