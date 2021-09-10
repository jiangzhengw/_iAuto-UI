# Time: 2021/8/26 14:51
# Author: jiangzhw
# FileName: video_interview.py
from selenium.webdriver.common.by import By

from HR.common.common import get_ini_config
from HR.page.base_page import BasePage
from HR.page.interview_list import InterviewList


class VideoInterview(BasePage):
    """视频面试 page"""
    _base_url = get_ini_config('video_interview')

    def interview_sys_click(self):
        """点击面试系统"""
        a_title = (By.CSS_SELECTOR, '[title="面试系统设置"]')
        interview_sys = (By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div/div/div[1]/div[2]/a')
        self.find_element(interview_sys).click()
        assert "面试系统设置" == self.get_text(a_title)

    def add_button_click(self):
        """点击新建面试项目按钮"""
        add_toast_title = (By.CSS_SELECTOR, '.flex-auto.hide-txt.flex-row span')
        add_button = (By.CSS_SELECTOR, '.add-project-box')
        self.find_element(add_button).click()
        assert "新建面试项目" == self.get_text(add_toast_title)

    def archived_button_click(self):
        """点击已归档按钮"""
        archive_button = (By.CSS_SELECTOR, '.file-wrap')
        self.find_element(archive_button).click()

    def search(self, content, is_anyway=False):
        """
        搜索框
        :param is_anyway:是否开启任意关键词
        :param content:搜索内容
        :return:null
        """
        search = (By.CSS_SELECTOR, 'input.el-input__inner')
        is_all_ele = (By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div/div/div[2]/div[1]/label')
        if is_anyway:
            self.find_element(is_all_ele).click()
        self.input(search, content)
        self.search_icon_click()

    def search_icon_click(self):
        """点击查询icon"""
        search_icon = (By.CSS_SELECTOR, 'i.el-icon-search')
        self.find_element(search_icon).click()

    # done:如何精准选择面试项目待解决,目前想到的解决办法是遍历项目列表，然后校验控件属性的text=id/pro_name,等于则点击，但是执行效率比较低
    # 采用jq contains 语法实现
    def open_interview_pro(self, pro_name):
        """
        打开指定的面试项目
        :return:项目清单page
        """
        # 直接使用执行jq表达式识别text内容，解决无id及class等标签情况的定位
        jq_script = f"$('span.el-tooltip:contains(\"{pro_name}\")').click()"
        self.run_script(jq_script)
        return InterviewList(driver=self.driver)

    def star_pro(self, project):
        """
        收藏置顶项目
        :param project:项目
        :return: null
        """
        pass

    def archive_pro(self, project):
        """
        归档项目
        :param project:项目
        :return:null
        """
        pass

    def to_site_manager(self, project):
        """
        跳转项目现场管理
        :param project:
        :return:
        """
        pass

    def modify_pro(self, project):
        """
        修改面试项目
        :param project:项目
        :return: null
        """
        pass

    def get_pro_name(self):
        """
        获取项目名称
        :return: str --> 项目名称
        """
        pass
