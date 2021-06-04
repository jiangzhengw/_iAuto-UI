# Time: 2021/6/4 15:32
# Author: jiangzhw
# FileName: log.py
import logging
import logging.config
import os

path_file = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))


class Logger:
    """log封装"""

    def log(self, logger):
        print(path_file)
        # 读取配置文件 # 采用配置文件
        logging.config.fileConfig(f"{path_file}\conf\logger.conf")
        # 创建logger
        logger = logging.getLogger(logger)
        return logger
