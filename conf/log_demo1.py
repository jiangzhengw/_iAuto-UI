# Time: 2021/6/2 20:22
# Author: jiangzhw
# FileName: log_demo1.py

import logging

LOG_FORMAT = "%(asctime)s %(name)s %(filename)s %(funcName)s %(levelname)s %(pathname)s %(message)s "  # 配置输出日志格式
DATE_FORMAT = '【 %Y-%m-%d  %H:%M:%S 】 %a '  # 配置输出时间的格式，注意月份和天数不要搞乱了
logging.basicConfig(level=logging.DEBUG,
                    format=LOG_FORMAT,
                    datefmt=DATE_FORMAT,
                    filename=r"log.txt"  # 有了filename参数就不会直接输出显示到控制台，而是直接写入文件
                    )
# 创建log 日志信息

logging.debug("debug")
logging.info("info")
logging.warning("warning")
logging.error("error")
logging.critical("critical")
logging.exception("exception 自定义")