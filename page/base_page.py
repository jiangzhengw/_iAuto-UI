# Time: 2021/6/2 14:56
# Author: jiangzhw
# FileName: base_page.py
import logging.config
import os
import time

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

path_file = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
print(path_file)


class BasePage:
    """BASIC Page"""
    _base_url = ""

    # log配置
    # 读取配置文件 # 采用配置文件
    logging.config.fileConfig(f"{path_file}\conf\logger.conf")
    # 创建logger
    logger = logging.getLogger("main")

    def __init__(self, driver: WebDriver = None):
        """
        初始化WebDriver等

        :param driver:WebDriver
        """
        if driver is None:
            self._driver = webdriver.Chrome()
            self._driver.implicitly_wait(5)
        else:
            self._driver = driver
        if self._base_url != "":
            self._driver.get(self._base_url)

    def close(self):
        """
        结束10s关闭页面

        :return: null
        """
        time.sleep(10)
        self._driver.quit()

    def find(self, locator):
        """
        find_element 二次封装

        :param locator: 定位符
        :return:WebElement
        """
        if isinstance(locator, tuple):
            return self._driver.find_element(*locator)
        else:
            self.logger.exception("元素定位格式错误，请检查定位！")
            print("元素定位格式错误，请检查定位！")

    def finds(self, locator, index):
        """
        返回指定定位符的指定索引的元素

        :param locator: 定位符
        :param index: 索引
        :return: WebElement:in list of WebElement
        """
        return self._driver.find_elements(*locator)[index]

    def wait(self, timeout, method):
        """
        等待方法封装

        :param timeout:等待时间
        :param method:等待方法
        :return:null
        """
        WebDriverWait(self._driver, timeout).until(method)

    def ele_click(self, ele_locator):
        """
        点击指定element元素

        :param ele_locator:element locator
        :return:null
        """
        self.find(ele_locator).click()

    def ele_index_click(self, ele_locator, index):
        """
        点击指定index的elements元素

        :param ele_locator:elements locator
        :param index:click index
        :return:
        """
        self.finds(ele_locator, index).click()

    def input(self, locator, msg):
        """
        指定input输入指定内容

        :param locator:element locator
        :param msg:to input msg
        :return:
        """
        self.find(locator).send_keys(msg)
