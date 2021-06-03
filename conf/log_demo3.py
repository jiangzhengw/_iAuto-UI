# Time: 2021/6/2 20:53
# Author: jiangzhw
# FileName: log_demo3.py
import logging.config

# 配置 root logger
logging.config.fileConfig(fname='./logger.ini', disable_existing_loggers=False)
# 获取logger 对象
logger = logging.getLogger("sampleLogger")
# 创建日志信息
logging.debug("debug")
logging.info("info")
logging.warning("warning")
logging.error("error")
logging.critical("critical")
logging.exception("exception 自定义", exc_info=False)
