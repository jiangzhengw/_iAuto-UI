# Time: 2021/8/4 16:56
# Author: jiangzhw
# FileName: main.py
import configparser

from selenium.webdriver.common.by import By

from pageobj.base_page import BasePage


class Main(BasePage):
    """Main page"""
    # done:封装get_config() func,提高复用
    cf = configparser.RawConfigParser()
    cf.read('../config/url.ini')
    _base_url = cf.get('url', 'main')

    def interview_click(self):
        """点击面试"""
        interview_ele = (By.XPATH, '/html/body/div[2]/div[2]/div/div[1]/ul/li[2]')
        self.find_element(interview_ele).click()

    def resume_click(self):
        """点击简历库-职位管理"""
        resume_ele = (By.XPATH, '/html/body/div[2]/div[2]/div/div[1]/ul/li[3]/a')
        self.find_element(resume_ele).click()
        job_man_ele = (By.CSS_SELECTOR, '.sub-job')
        self.find_element(job_man_ele).click()
        print(self._base_url)
