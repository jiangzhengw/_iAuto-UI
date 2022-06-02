# Time: 2021/9/3 18:30
# Author: jiangzhw
# FileName: setting.py
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)

# 配置文件
CONFIG_DIR = os.path.join(BASE_DIR, "config")
# db配置文件
DB_CONFIG_DIR = os.path.join(BASE_DIR, "database", "user.ini")
# 测试用例目录
TEST_DIR = os.path.join(BASE_DIR, "case")
# 测试报告目录
TEST_REPORT = os.path.join(BASE_DIR, "output", "reports")
# 日志目录
LOG_DIR = os.path.join(BASE_DIR, "log")
# 测试数据文件
TEST_DATA_YAML = os.path.join(BASE_DIR, "data")
