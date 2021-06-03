# Time: 2021/6/2 21:10
# Author: jiangzhw
# FileName: log_demo4.py
import logging.config
# 读取配置文件 # 采用配置文件
logging.config.fileConfig("logger.conf")
# 创建logger
logger = logging.getLogger('main')
# 日志生成
logging.debug("debug")
logging.info("info")
logging.warning("warning")
logging.error("error")
logging.critical("critical")
logging.exception("exception 自定义", exc_info=False)
