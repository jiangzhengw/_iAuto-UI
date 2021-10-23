# Time: 2021/10/23 20:50
# Author: jiangzhw
# FileName: room.py
from common.common import get_ini_config
from page.base_page import BasePage


class Room(BasePage):
    """面试房间"""
    _base_url = get_ini_config('position_management')
