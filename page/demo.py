# Time: 2021/10/28 19:31
# Author: jiangzhw
# FileName: demo.py

from common.common import get_ini_config
from page.base_page import BasePage


class Demo(BasePage):
    """面试房间"""
    _base_url = get_ini_config("demo")

    def switch_to_frame(self):
        print("123")
