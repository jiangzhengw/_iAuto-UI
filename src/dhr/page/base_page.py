# Time: 2021/6/2 14:56
# Author: jiangzhw
# FileName: base_page.py
import time

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    """BASIC Page"""
    _base_url = ""

    def __init__(self, driver: WebDriver = None):
        """init method"""
        if driver is None:
            self._driver = webdriver.Chrome()
            self._driver.implicitly_wait(5)
        else:
            self._driver = driver
        if self._base_url != "":
            self._driver.get(self._base_url)

    def close(self):
        """base find method"""
        time.sleep(10)
        self._driver.quit()

    def find(self):
        """find"""
        pass
