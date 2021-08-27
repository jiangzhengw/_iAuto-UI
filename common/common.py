# Time: 2021/8/27 17:51
# Author: jiangzhw
# FileName: common.py
import configparser
import os
import platform

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


def get_ini_config(key, section='url', path='../config/url.ini'):
    """
    获取指定路径的ini文件的指定section指定key的value
    :param path:配置文件路径
    :param section:模块
    :param key:key
    :return:value
    """
    cf = configparser.RawConfigParser()
    cf.read(path)
    return cf.get(section, key)


def auto_driver(driver_type='chrome'):
    platform_system = platform.system()  # 获取底层平台标识符：获取系统类型win or mac or linux等
    print('platform.system is: {}'.format(platform_system))
    # 检查是否已配置chromedriver到环境变量内
    is_install = True
    if platform_system == 'Windows':
        result = os.popen('where chromedriverx').read()
        # is_install = False if '用提供的模式无法找到文件' in res else is_install = True
        if result == '': is_install = False
    elif platform_system == 'linux' or platform_system == 'Darwin':
        result = os.popen('which chromedriver').read()
        # is_install = False if 'no chromedriver in' in result else True
        if 'no chromedriver in' in result: is_install = False
    print("result:", result, "is_install:", is_install)
    # 初始化driver
    driver = None
    if driver_type in ['chrome', 'Chrome', 'CHROME']:
        print("浏览器类型：chrome")
        if not is_install:
            driver_path = ChromeDriverManager(
                url="https://npm.taobao.org/mirrors/chromedriver/",
                latest_release_url="https://npm.taobao.org/mirrors/chromedriver/LATEST_RELEASE").install()
            print("driver_path:", driver_path)
        else:
            driver_path = 'chromedriver'
        driver = webdriver.Chrome(executable_path=driver_path)
    elif driver_type in ['firefox', 'Firefox', 'FIREFOX']:
        print("浏览器类型：firefox")
        if not is_install:
            driver_path = GeckoDriverManager().install()
            print("driver_path:", driver_path)
        else:
            driver_path = 'geckodriver'
        driver = webdriver.Firefox(executable_path=driver_path)
    return driver


if __name__ == '__main__':
    my_driver = auto_driver(driver_type='firefox')
    my_driver.get("https://www.baidu.com")
