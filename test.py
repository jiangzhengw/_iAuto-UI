# Time: 2022/6/1 17:57
# Author: jiangzhw
# FileName: test.py
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("http://mail.hichina.com/")
time.sleep(10)  # 使用强制等待，还是找不到啊

# 显示等待selenium.common.exceptions.TimeoutException: Message:
# WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.CSS_SELECTOR, "input#username.login_input")))
# ele = driver.find_element(By.CSS_SELECTOR, "input#username.login_input")
# ele.click()
# driver.find_element(By.CSS_SELECTOR, "input#username.login_input").send_keys("jiangzhw")

#打印pagesource后发现,确实没有元素
with open("page_source.txt", "w+",encoding="utf-8") as f:
    f.write(driver.page_source)


