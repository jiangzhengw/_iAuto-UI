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
driver.implicitly_wait(5)
# time.sleep(3)  # 使用强制等待，还是找不到

# 显示等待selenium.common.exceptions.TimeoutException: Message:
# WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.CSS_SELECTOR, "input#username.login_input")))
# driver.switch_to.frame(2)
# ele = driver.find_element(By.CSS_SELECTOR, "input#username")
# ele.send_keys("jiangzhw")
# driver.close()
ele = driver.find_element(By.XPATH, '//*')
print(ele)

# 打印pagesource后发现,确实没有元素,但是web前端的pagesource并不能代表全部元素
# with open("page_source.txt", "w", encoding="utf-8") as f:
#     f.write(driver.page_source)

# 打印window标签数量
# print(driver.window_handles) #['CDwindow-4A4805D456FBF088AAB5A403E7711C4D']


# 通过xpath打印全部控件
# page_eles = driver.find_element(By.XPATH, "//*")

# 截图查看 ,是存在的
# driver.get_screenshot_as_file("alibb.png")
