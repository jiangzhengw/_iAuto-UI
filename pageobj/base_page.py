# Time: 2021/6/2 14:56
# Author: jiangzhw
# FileName: base_page.py
import logging
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

logger = logging.getLogger("Main.BasePage")


class BasePage:
    """BASIC Page"""
    _base_url = ""

    def __init__(self, driver: WebDriver = None):
        """
        初始化WebDriver等
        :param driver:WebDriver
        """
        # 复用指定端口浏览器
        opt = Options()
        # opt.debugger_address = "127.0.0.1:9222"

        # 复用cookies
        __cookies = [
            {'domain': 'dhr.nowcoder.com', 'httpOnly': False, 'name': 'HRCLIENTID', 'path': '/', 'secure': False,
             'value': 'dfd97ba6480d7d6a37263ff47beaba99'},
            {'domain': 'dhr.nowcoder.com', 'httpOnly': False, 'name': 's', 'path': '/', 'secure': False,
             'value': '5af9d32299f984a152376c19827f00c9'},
            {'domain': '.nowcoder.com', 'expiry': 1626350711, 'httpOnly': False, 'name': 'hrat', 'path': '/',
             'sameSite': 'None', 'secure': True,
             'value': '2d22aa0e05401f9e882ec6474b498a9dbeca79ba34b958ea0b39b0e1177bd158'},
            {'domain': '.nowcoder.com', 'expiry': 1623760757, 'httpOnly': False,
             'name': 'c196c3667d214851b11233f5c17f99d5_gr_session_id_a511b848-316f-4009-ada5-c50ffaabe1d9', 'path': '/',
             'secure': False, 'value': 'true'},
            {'domain': '.nowcoder.com', 'httpOnly': False, 'name': 'Hm_lpvt_a808a1326b6c06c437de769d1b85b870',
             'path': '/', 'secure': False, 'value': '1623758958'},
            {'domain': '.nowcoder.com', 'expiry': 2249122747, 'httpOnly': True, 'name': 'experimentation_subject_id',
             'path': '/', 'secure': False,
             'value': 'Ijc5N2QzYjliLTQ5YzAtNGNiMy05MGY3LWNiYmYyZDU5Y2Q5OSI%3D--5a3057a42d3636dbb1986263061b64d79bc26628'},
            {'domain': '.nowcoder.com', 'expiry': 1623760757, 'httpOnly': False,
             'name': 'c196c3667d214851b11233f5c17f99d5_gr_session_id', 'path': '/', 'secure': False,
             'value': 'a511b848-316f-4009-ada5-c50ffaabe1d9'},
            {'domain': '.nowcoder.com', 'expiry': 1655294957, 'httpOnly': False,
             'name': 'Hm_lvt_a808a1326b6c06c437de769d1b85b870', 'path': '/', 'secure': False,
             'value': '1623738763,1623738771,1623740092,1623758922'},
            {'domain': '.nowcoder.com', 'expiry': 3770628347, 'httpOnly': False, 'name': 'from', 'path': '/',
             'sameSite': 'None', 'secure': True, 'value': '1'},
            {'domain': '.nowcoder.com', 'expiry': 1633227874, 'httpOnly': False, 'name': 'NOWCODERUID', 'path': '/',
             'sameSite': 'None', 'secure': True, 'value': 'EEA2B4CD83034712CF6A7978F389219F'},
            {'domain': 'dhr.nowcoder.com', 'expiry': 1637374754, 'httpOnly': False, 'name': '_bl_uid', 'path': '/',
             'secure': False, 'value': '5qkCgp8s1Idz7teyR6Cy6499dvwn'},
            {'domain': '.nowcoder.com', 'expiry': 1933035874, 'httpOnly': False, 'name': 'NOWCODERCLINETID',
             'path': '/', 'sameSite': 'None', 'secure': True, 'value': '5BBBF024161FD61595B01F4C7E680353'},
            {'domain': '.nowcoder.com', 'expiry': 1938502026, 'httpOnly': False,
             'name': 'c196c3667d214851b11233f5c17f99d5_gr_last_sent_cs1', 'path': '/', 'secure': False,
             'value': '494088990'},
            {'domain': '.nowcoder.com', 'expiry': 1939118957, 'httpOnly': False, 'name': 'gr_user_id', 'path': '/',
             'secure': False, 'value': 'd11071d6-7afc-4f71-88c6-87cb8194b7a4'}]
        if driver is None:
            self._driver = webdriver.Chrome(options=opt)
            self._driver.implicitly_wait(5)
        else:
            self._driver = driver
        if self._base_url != "":
            self._driver.get(self._base_url)
            for cookie in __cookies:
                # 取消cookie的有效时长设置
                if 'expiry' in cookie:
                    cookie.pop('expiry')
                self._driver.add_cookie(cookie)
            self._driver.get(self._base_url)

    def set_cookies(self):
        """设置浏览器cookies"""
        pass

    def close(self, timeout=5):
        """
        结束10s关闭页面
        :return: null
        """
        logger.info("等待%ds后，关闭driver！" % timeout)
        time.sleep(timeout)
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
            logger.error("元素定位格式错误，请检查入参格式是否为tuple！")

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
            logger.info(u'等待元素:%s' % str(locator))
            return True
        except TimeoutError as e:
            logger.error("等待：%s超时！！！" % str(locator))
            raise e

    def ele_click(self, ele_locator):
        """
        点击指定element元素
        :param ele_locator:element locator
        :return:null
        """
        try:
            logger.info(u'点击元素：%s' % str(ele_locator))
            self.find(ele_locator).click()
            return True
        except Exception as e:
            logger.error(u'元素：%s未定位到！！！' % str(ele_locator))
            raise e

    def ele_index_click(self, ele_locator, index):
        """
        点击指定index的elements元素
        :param ele_locator:elements locator
        :param index:click index
        :return:
        """
        try:
            logger.info(u'点击元素：%s' % str(ele_locator))
            self.finds(ele_locator, index).click()
            return True
        except Exception as e:
            logger.error(u'元素：%s未定位到！！！' % str(ele_locator))
            raise e

    def input(self, locator, msg):
        """
        指定input输入指定内容
        :param locator:element locator
        :param msg:to input msg
        :return:
        """
        self.find(locator).send_keys(msg)
        logger.info(u'向元素 %s 输入文字：%s' % (locator, msg))

    def clear(self, locator):
        """
        清空内容
        :param locator:定位方法
        :return:
        """
        self.find(locator).clear()
        logger.info(u'清空内容：%s' % str(locator))

    def open(self, url):
        """
        打开url
        :param url: 网址连接
        """
        self._driver.get(url)
        logger.info(u'打开网址：%s' % url)

    def get_url(self):
        """
        获取当前网址
        :return: url
        """
        logger.info(u'获取当前网址：%s' % self._driver.current_url)
        return self._driver.current_url
