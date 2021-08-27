# Time: 2021/6/4 15:32
# Author: jiangzhw
# FileName: log.py
import logging.config
import os

path_file = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

print(path_file)
# 读取配置文件 # 采用配置文件
logging.config.fileConfig(f"{path_file}\config\logger.conf")
# 创建logger
LOG = logging.getLogger("AutoUI")
