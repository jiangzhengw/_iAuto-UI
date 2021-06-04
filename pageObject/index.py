# Time: 2021/6/2 15:28
# Author: jiangzhw
# FileName: index.py

from selenium.webdriver.common.by import By

from pageObject.base_page import BasePage


class Index(BasePage):
    """nowcoder index pageObject"""
    _base_url = "https://www.baidu.com/"

    def search(self, msg):
        """login click"""
        search = (By.CSS_SELECTOR, 'input[class="s_ipt"]')
        self.input(search, msg)
