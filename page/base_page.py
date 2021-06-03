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
    logger = logging.getLogger("BasePage")

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

    def wait(self, timeout, locator):
        """
        等待方法封装
        :param timeout:等待时间
        :param locator:等待方法
        :return:null
        """
        try:
            WebDriverWait(self._driver, timeout).until(lambda x: self.find(locator), message="element not found")
            self.logger.info(u'等待元素:%s' % locator)
            return True
        except TimeoutError as e:
            self.logger.error("等待：%s超时！！！" % locator)
            return False

    def ele_click(self, ele_locator):
        """
        点击指定element元素
        :param ele_locator:element locator
        :return:null
        """
        try:
            self.logger.info(u'点击元素：%s' % ele_locator)
            self.find(ele_locator).click()
            return True
        except Exception as e:
            self.logger.error(u'元素：%s未定位到！！！' % ele_locator)
            return False

    def ele_index_click(self, ele_locator, index):
        """
        点击指定index的elements元素
        :param ele_locator:elements locator
        :param index:click index
        :return:
        """
        try:
            self.logger.info(u'点击元素：%s' % ele_locator)
            self.finds(ele_locator, index).click()
            return True
        except Exception as e:
            self.logger.error(u'元素：%s未定位到！！！' % ele_locator)
            return False

    def input(self, locator, msg):
        """
        指定input输入指定内容
        :param locator:element locator
        :param msg:to input msg
        :return:
        """
        self.find(locator).send_keys(msg)
        self.logger.info(u'向元素 %s 输入文字：%s' % (locator, msg))

    def clear(self, locator):
        """
        清空内容
        :param locator:定位方法
        :return:
        """
        self.find(locator).clear()
        self.logger.info(u'清空内容：%s' % locator)

    def open(self, url):
        """
        打开url
        :param url: 网址连接
        """
        self._driver.get(url)
        self.logger.info(u'打开网址：%s' % url)

    def get_url(self):
        """
        获取当前网址
        :return: url
        """
        self.logger.info(u'获取当前网址：%s' % self._driver.current_url)
        return self._driver.current_url
