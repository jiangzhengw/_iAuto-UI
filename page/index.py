# Time: 2021/6/2 15:28
# Author: jiangzhw
# FileName: index.py

from selenium.webdriver.common.by import By

from page.base_page import BasePage


class Index(BasePage):
    """nowcoder index page"""
    _base_url = "https://www.baidu.com/"

    def login(self):
        """login click"""
        self.logger.debug("debug")
        self.logger.info("info")
        self.logger.warning("warning")
        self.logger.error("error")
        self.logger.critical("critical")
        self.logger.exception("exception 自定义", exc_info=False)
        self._driver.find_element(By.CSS_SELECTOR, 'input[class="s_ipt"]').send_keys("哈哈哈哈")
