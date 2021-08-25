# Time: 2021/8/24 22:34
# Author: jiangzhw
# FileName: demo.py
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://dhr.nowcoder.com/")
time.sleep(30)
driver.get("https://dhr.nowcoder.com/console#resume/%22action%22%3A%22position%2FeditProject%2Findex%22")
js = 'document.querySelector(".data-oprt .control-group:nth-child(1) > input").removeAttribute("readonly");'
time.sleep(5)
# driver.execute_script(js)
ele = (By.CSS_SELECTOR, '.data-oprt .control-group:nth-child(1) > input')
driver.execute_script('arguments[0].removeAttribute("readonly")', driver.find_element(*ele))
driver.close()