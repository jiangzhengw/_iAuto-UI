# Time: 2021/6/3 16:46
# Author: jiangzhw
# FileName: run.py
import os

import pytest

from common.log import Logger


def main():
    """运行pytest用例集"""
    # -v :打印详细log日志 -s 输出case中print的内容
    cmd = ['-vs', 'case/', '--alluredir', 'output/results']
    pytest.main(cmd)
    os.popen('allure generate output/results -o output/reports/ --clean')
    # os.popen('allure open -h 127.0.0.1 -p 8083 output/reports/')


if __name__ == "__main__":
    log = Logger().log("Main")  # 初始化log配置
    main()  # 运行pytest测试集
