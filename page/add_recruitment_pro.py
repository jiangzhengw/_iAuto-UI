# Time: 2021/8/23 17:37
# Author: jiangzhw
# FileName: add_recruitment_pro.py
import time

from selenium.webdriver.common.by import By

from common.common import get_ini_config
from page.base_page import BasePage


class AddRecruitmentPro(BasePage):
    """新建招聘项目 page"""
    _base_url = get_ini_config('add_recruitment_pro')

    def input_pro_name(self, content):
        """
        设置项目名称
        :param content:输入内容
        :return:null
        """
        pro_name = (By.CSS_SELECTOR, '#jsCpn_4_component_0 input')
        self.input(pro_name, content)

    def input_pro_mark(self, content):
        """
        设置项目备注
        :param content:输入内容
        :return:null
        """
        pro_mark = (By.CSS_SELECTOR, '#jsCpn_6_component_1 input')
        self.input(pro_mark, content)

    def set_max_oa(self, content):
        """
        设置最大网申数
        :param content:输入内容
        :return:null
        """
        pro_mark = (By.CSS_SELECTOR, '#jsCpn_138_component_14 input')
        self.input(pro_mark, content)

    def set_max_pi(self, content):
        """
        设置最大内推数
        :param content:输入内容
        :return:null
        """
        pro_mark = (By.CSS_SELECTOR, '.control-group input')
        self.input(pro_mark, content)

    def set_recruitment(self, params: list):
        """
        设置招聘流程
        :param params: 设置参数
        :return:null
        """
        write = (By.XPATH, '//*[@id="jsCpn_121_component_1"]/div[1]/div[3]/label[3]/span')
        interview = (By.XPATH, '//*[@id="jsCpn_121_component_1"]/div[1]/div[3]/label[4]/span')
        if "笔试" in params:
            self.find_element(write).click()
        elif "面试" in params:
            self.find_element(interview).click()
        else:
            raise Exception("请输入正确的招聘流程参数！")

    def is_lock_resume(self, is_lock=False):
        """
        是否允许锁定简历
        :param is_lock:boolean
        :return:null
        """
        lock = (By.XPATH, '//*[@id="jsCpn_128_checkbox_54"]')
        not_lock = (By.XPATH, '//*[@id="jsCpn_127_checkbox_53"]')
        if is_lock:
            self.find_element(lock).click()
        else:
            self.find_element(not_lock).click()

    def set_manager_auto(self, is_auto=False):
        """
        设置管理权限
        :param is_auto:是否开启管理权限
        :return:null
        """
        auto = (By.XPATH, '//*[@id="jsCpn_607_checkbox_41"]/span')
        not_auto = (By.XPATH, '//*[@id="jsCpn_608_checkbox_42"]/span')
        if is_auto:
            self.find_element(auto).click()
        else:
            self.find_element(not_auto).click()

    def max_online(self, number):
        """
        设置最大同时网申数
        :param number: 最大网申数目
        :return:null
        """
        max_online = (By.CSS_SELECTOR, '[placeholder="同一候选人最多可网申的职位数"]')
        self.input(max_online, number)

    def max_push_in(self, number):
        """
        设置最大同时内推数
        :param number:最大内推数目
        :return:null
        """
        max_pi = (By.CSS_SELECTOR, '[placeholder="同一候选人最多可内推的职位数"]')
        self.input(max_pi, number)

    def set_search_time(self, n=1):
        """
        设置应聘者可查询状态时间
        :param n:1五分钟2两小时3一天4两天
        :return:null
        """
        ele_1 = (By.XPATH, '//*[@id="jsCpn_615_checkbox_43"]')
        ele_2 = (By.XPATH, '//*[@id="jsCpn_616_checkbox_44"]')
        ele_3 = (By.XPATH, '//*[@id="jsCpn_617_checkbox_45"]')
        ele_4 = (By.XPATH, '//*[@id="jsCpn_618_checkbox_46"]')
        map_dict = {
            1: ele_1,
            2: ele_2,
            3: ele_3,
            4: ele_4
        }
        self.find_element(map_dict[n]).click()

    def set_position_category(self, classify=False, city=False):
        """
        职位分类设置
        :param classify:职位分类
        :param city:工作城市
        :return:
        """
        position_type = (By.XPATH, '//*[@id="jsCpn_620_checkbox_47"]')
        city_ele = (By.XPATH, '//*[@id="jsCpn_621_checkbox_48"]')
        if classify:
            self.find_element(position_type).click()
        if city:
            self.find_element(city_ele).click()

    def add_position_category(self, name, **kwargs):
        """
        新增职位分类
        :param name:职位名称
        :param kwargs:关键字参数
        :return:null
        """
        add_position = (By.CSS_SELECTOR, 'a.btn.btn-primary.btn-auto.js-add-type')
        add_option = (By.CSS_SELECTOR, 'a.link-green.js-add-choice')
        name_ele = (By.CSS_SELECTOR, '[placeholder="输入名称，不能超过10个字符"]')
        option_ele = (By.CSS_SELECTOR, '[placeholder="输入选项，不能超过18个字符"]')
        self.find_element(add_position).click()
        # 新增职位分类
        self.wait(add_option)
        self.input(name_ele, name)
        length = len(kwargs)
        kw_values = list(kwargs.values())
        if 0 < length < 2:
            self.input(option_ele, kw_values[0])
        else:
            self.input(option_ele, kw_values[0])
            for i in range(length - 1):
                self.find_element(add_option).click()
                self.input(option_ele, kw_values[i + 1])

    def delete_option(self):
        """新增职位分类-删除选项"""
        delete_button = (By.CSS_SELECTOR, 'a.icon-trash.js-trash')
        delete_list = self.find_elements(delete_button)
        for ele in delete_list:
            ele.click()

    def set_online_time(self, start_date, start_time, end_date, end_time, is_now=False):
        """
        设置网申投递开放时间

        :param start_date: 开始日期
        :param start_time: 开始时间
        :param end_date: 结束日期
        :param end_time: 结束时间
        :param is_now: 是否即日起
        :return: null
        """
        # start_date_ele = self.find_element(*(By.CSS_SELECTOR, '[placeholder="开始日期"]'))
        # start_time_ele = self.find_element(*(By.CSS_SELECTOR, '[placeholder="开始时间"]'))
        # end_date_ele = self.find_element(*(By.CSS_SELECTOR, '[placeholder="结束日期"]'))
        # end_time_ele = self.find_element(*(By.CSS_SELECTOR, '[placeholder="结束时间"]'))
        # self.driver.execute_script("arguments[0].removeAttribute(\"readonly\")", start_date_ele)
        # self.driver.execute_script("arguments[0].removeAttribute(\"readonly\")", start_time_ele)
        # self.driver.execute_script("arguments[0].removeAttribute(\"readonly\")", end_date_ele)
        # self.driver.execute_script("arguments[0].removeAttribute(\"readonly\")", end_time_ele)
        now = (By.XPATH, '//*[@id="jsCpn_42_checkbox_10"]')
        # 设置开始日期时间
        if is_now:
            self.find_element(now).click()
        else:
            js_script1 = f'document.querySelector(".data-oprt .control-group:nth-child(1) > input").removeAttribute(' \
                         f'"readonly");'
            self.run_script(js_script1)
            time.sleep(2)
            js_script2 = f'document.querySelector(".data-oprt .control-group:nth-child(1) > input").value="{start_date}";'
            self.run_script(js_script2)
            js_script3 = f'document.querySelector(".data-oprt .control-group:nth-child(2) > input").removeAttribute(' \
                         f'"readonly");'
            self.run_script(js_script3)
            time.sleep(2)
            js_script4 = f'document.querySelector(".data-oprt .control-group:nth-child(2) > input").value="{start_time}";'
            self.run_script(js_script4)
        # 设置结束日期时间
        js_script5 = f'document.querySelector(".data-oprt .control-group:nth-child(5) > input").removeAttribute(' \
                     f'"readonly");'
        self.run_script(js_script5)
        time.sleep(2)
        js_script6 = f'document.querySelector(".data-oprt .control-group:nth-child(5) > input").value="{end_date}";'
        self.run_script(js_script6)
        js_script7 = f'document.querySelector(".data-oprt .control-group:nth-child(6) > input").removeAttribute(' \
                     f'"readonly");'
        self.run_script(js_script7)
        time.sleep(2)
        js_script8 = f'document.querySelector(".data-oprt .control-group:nth-child(6) > input").value="{end_time}";'
        self.run_script(js_script8)

    def set_resume_option(self, number=False, native=False, political=False):
        """
        设置简历字段要求
        :param number:证件号码
        :param native:籍贯
        :param political:政治面貌
        :return:
        """
        number_ele = (By.XPATH, '//*[@id="jsCpn_173_checkbox_73"]')
        native_ele = (By.XPATH, '//*[@id="jsCpn_174_checkbox_74"]')
        political_ele = (By.XPATH, '//*[@id="jsCpn_175_checkbox_75"]')
        if number:
            self.find_element(number_ele).click()
        if native:
            self.find_element(native_ele).click()
        if political:
            self.find_element(political_ele).click()

    def set_done_click(self):
        """点击设置完毕"""
        save = (By.XPATH, '//*[@id="jsCpn_119_component_0"]/a')
        self.find_element(save).click()
