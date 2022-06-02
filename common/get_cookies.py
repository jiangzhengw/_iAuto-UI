# Time: 2021/8/19 10:26
# Author: jiangzhw
# FileName: get_cookies.py
import json
import time

from selenium import webdriver

# 获取cookies
driver = webdriver.Chrome()
driver.get("https://hr.nowcoder.com/login")
time.sleep(30)
# 输入登录信息
# driver.find_element(By.LINK_TEXT, '立即登录').click()
cookies = driver.get_cookies()

with open('../config/cookies.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(cookies))

driver.close()
"""
import time

from selenium import webdriver

# 获取cookies
driver = webdriver.Chrome()
driver.get("https://hr.nowcoder.com/login")
time.sleep(30)
# 输入登录信息
# driver.find_element(By.LINK_TEXT, '立即登录').click()
cookies = driver.get_cookies()

with open('../conf/cookies.txt', 'w+', encoding='utf-8') as f:
    for cookie in cookies:
        f.writelines(cookie)

driver.close()

# 读取cookies
filename = '../conf/cookies.txt'
with open(filename, 'r+', encoding='utf-8') as f:
    cookies = f.read()
    print(cookies)
"""