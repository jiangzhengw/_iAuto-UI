# Time: 2021/6/2 15:28
# Author: jiangzhw
# FileName: index.py

from selenium.webdriver.common.by import By

from pageobj.main import Main
from utils.base_api import BaseAPI


class Index(BaseAPI):
    """nowcoder index pageobj"""
    # _base_url = "https://www.baidu.com/"
    _base_url = "https://dhr.nowcoder.com/console#resume/%22action%22%3A%22position%2FeditProject%2Findex%22"

    def search(self, msg):
        """login click"""
        search = (By.CSS_SELECTOR, 'input[class="s_ipt"]')
        self.input(search, msg)

    def login(self, ):
        """login"""
        interview = (By.LINK_TEXT, "面试")
        self.wait(5, interview)
        self.ele_click(interview)

    def swith_to_main(self):
        """swith to main page"""
        return Main(self._driver)
