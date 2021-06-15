# Time: 2021/6/2 15:28
# Author: jiangzhw
# FileName: index.py

from selenium.webdriver.common.by import By

from pageobj.base_page import BasePage


class Index(BasePage):
    """nowcoder index pageobj"""
    # _base_url = "https://www.baidu.com/"
    _base_url = "https://dhr.nowcoder.com/console"

    def search(self, msg):
        """login click"""
        search = (By.CSS_SELECTOR, 'input[class="s_ipt"]')
        self.input(search, msg)

    def login(self, ):
        """login"""
        interview = (By.LINK_TEXT, "面试")
        self.wait(5, interview)
        self.ele_click(interview)
