# Time: 2021/6/2 14:56
# Author: jiangzhw
# FileName: base_page.py
import base64
import json
import time
import traceback

import requests
from PIL import Image
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from common.log import LOG

_cookie_path = '../config/cookies.json'


class BasePage:
    """BASIC Page"""
    _base_url = ""

    def __init__(self, driver: WebDriver = None, browser='chrome', is_login=True):
        """
        初始化WebDriver等
        :param driver:WebDriver
        """
        if driver is None:
            if browser in ['chrome', 'Chrome', 'CHROME']:
                chrome_options = webdriver.ChromeOptions()
                # 复用指定端口浏览器
                # opt.debugger_address = "127.0.0.1:9222"
                # 启用无头浏览器模式
                # opt.add_argument('--headless')
                # 禁用gpu
                # opt.add_argument('--disable-gpu')
                # 无界面情况下可以使用以下代码
                # chrome_options.add_argument('--headless')
                chrome_options.add_argument('--disable-gpu')
                self._driver = webdriver.Chrome(options=chrome_options)
            elif browser in ['firefox', 'FireFox', 'Firefox', 'FIREFOX']:
                self._driver = webdriver.Firefox()
            elif browser in ['ie', 'IE', 'Ie']:
                self._driver = webdriver.Ie()
            else:
                self._driver = None
                LOG.error('Cannot support such explorer:{0} now,retry for others!'.format(browser))
            self._driver.implicitly_wait(5)
            self._driver.maximize_window()
        else:
            self._driver = driver

        """
        # 将cookies存储到python自带数据库内
        db = shelve.open("cookies")
        # 获取登录账号cookie
        self._driver.get_cookies()
        __cookies = []
        db['cookies'] = __cookies
        cookies = db['cookies']
        """
        if self._base_url != "":
            self._driver.get(self._base_url)
            if is_login:
                # cookie复用
                self._driver.delete_all_cookies()
                with open(_cookie_path, 'r', encoding='utf-8') as f:
                    cookies = json.load(f)
                    for cookie in cookies:
                        if 'expiry' in cookie:
                            cookie.pop('expiry')
                        self._driver.add_cookie(cookie)
                self._driver.get(self._base_url)
            else:
                self._driver.get(self._base_url)
            time.sleep(1)

    def close(self, timeout=5):
        """
        结束5s关闭页面
        :param timeout:等待时间
        :return:
        """
        LOG.info("等待{}s后，关闭driver！".format(timeout))
        time.sleep(timeout)
        self._driver.quit()

    def find_element(self, locator):
        """
        find_element 二次封装
        :param locator: 定位符
        :return:WebElement
        """
        if isinstance(locator, tuple):
            LOG.info(u'开始点击元素:{0}'.format(locator))
            return self._driver.find_element(*locator)
        else:
            LOG.error("元素定位格式错误，请检查入参格式是否为tuple！")

    def find_elements(self, locator, index):
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
            WebDriverWait(self._driver, timeout).until(lambda x: self.find_element(locator),
                                                       message="element not found")
            LOG.info(u'等待元素:{}'.format(locator))
            return True
        except TimeoutError as e:
            LOG.error("等待：{}s超时！！！".format(locator))
            raise e

    def ele_click(self, locator):
        """
        点击指定element元素
        :param locator:element locator
        :return:null
        """
        try:
            LOG.info(u'点击元素：{}'.format(locator))
            self.find_element(locator).click()
            return True
        except Exception as e:
            LOG.error(u'元素：{}未定位到！！！'.format(locator))
            raise e

    def ele_index_click(self, ele_locator, index):
        """
        点击指定index的elements元素
        :param ele_locator:elements locator
        :param index:click index
        :return:
        """
        try:
            self.find_elements(ele_locator, index).click()
            LOG.info(u'点击元素：{}'.format(ele_locator))
        except Exception as e:
            LOG.error(u'元素：{}未定位到！！！'.format(ele_locator))
            raise e

    def input(self, locator, msg):
        """
        指定input输入指定内容
        :param locator:element locator
        :param msg:to input msg
        :return:
        """
        try:
            self.find_element(locator).send_keys(msg)
            LOG.info(u'向元素 {} 输入文字：{}'.format(locator, msg))
        except Exception as e:
            LOG.error(u'元素：{}未定位到！！！'.format(locator))
            raise e

    def clear_input(self, locator):
        """
        清空输入框
        :param locator: 定位器
        :return:
        """
        self.wait(locator)
        try:
            self.find_element(locator).clear()
            LOG.info(f'开始清空元素内容:{locator}')
        except Exception as e:
            LOG.error(f"元素{locator}不可清空！！！")
            raise e

    def open(self, url):
        """
        打开url
        :param url: 网址连接
        """
        try:
            self._driver.get(url)
            LOG.info(u'打开网址：{}'.format(url))
        except Exception as e:
            LOG.error(u'url:{} 错误！'.format(url))
            raise e

    def get_url(self):
        """
        获取当前网址
        :return: url
        """
        LOG.info(u'获取当前网址：{}'.format(self._driver.current_url))
        return self._driver.current_url

    def hover_element(self, locator):
        """
        悬浮元素
        :param locator:定位器
        :return:null
        """
        try:
            time.sleep(1)
            LOG.info(f'开始悬浮元素:{locator}')
            ActionChains(self._driver).move_to_element(self.find_element(locator)).perform()
        except Exception as e:
            LOG.error(f"等待：{locator}超时！！！")
            raise e

    def run_script(self, script):
        """
        执行脚本：js or jq
        :param script:待执行的脚本
        :return:bool result
        """
        try:
            self._driver.execute_script(script)
            LOG.info(f'开始执行script:{script}')
            return True
        except Exception as e:
            LOG.error(f"执行script:{script}失败!")
            LOG.debug(traceback.format_exc(e))
            return False

    def get_text(self, locator):
        """
        获取控件text
        :param locator:
        :return:
        """
        pass

    def get_attribute_value(self, locator, attribute):
        """
        获取控件属性值
        :param locator:控件定位
        :param attribute: 属性名
        :return:value
        """
        pass

    def double_click(self, locator):
        """
        双击元素
        :param locator:定位
        :return:null
        """
        try:
            ActionChains(self._driver).double_click(locator).perform()
            LOG.info(f'双击元素:{locator}')
        except Exception as e:
            LOG.error(f'双击元素：{locator}失败')
            raise e

    def save_screen(self, file_name):
        """
        全屏截图
        :param file_name:文件名字
        :return:null
        """
        self._driver.save_screenshot(f'../output/screenshot/{file_name}.png')

    def screen_part(self, locator, file_name):
        """
        部分截图
        :param file_name: 截图文件名
        :param locator:定位
        :return: null
        """
        self.find_element(locator).screenshot(f'../output/screenshot/{file_name}.png')

    def screen_part_v2(self, locator, file_name):
        """
        部分截图v2
        :param file_name: 截图文件名
        :param locator:定位
        :return: null
        """
        self._driver.save_screenshot('all.png')
        left = locator.location['x']
        top = locator.location['y']
        right = locator.location['x'] + locator.size['width']
        bottom = locator.location['y'] + locator.size['height']
        im = Image.open('all.png')
        im = im.crop((left, top, right, bottom))
        im.save(f'../output/screenshot/{file_name}.png')

    def screen_part_v3(self, locator, file_name):
        """
        部分截图v3
        :param locator:定位
        :param file_name:截图文件名
        :return:null
        """
        session_id = self._driver.session_id
        r = requests.get(f'http://localhost:9102/session/{session_id}/element/{locator.id}/screenshot')
        print(r.status_code)
        print(r.text)
        with open(f'../output/screenshot/{file_name}.png', 'wb') as f:
            img_data = base64.b64decode(r.json()["value"])
            f.write(img_data)
