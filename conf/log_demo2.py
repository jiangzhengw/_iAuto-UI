# Time: 2021/6/2 20:42
# Author: jiangzhw
# FileName: log_demo2.py
import logging


def log():
    # 创建logger，如果参数为空则返回root logger
    logger = logging.getLogger("nick")
    logger.setLevel(logging.DEBUG)  # 设置logger日志等级
    # 这里进行判断，如果logger.handlers列表为空，则添加，否则，直接去写日志
    if not logger.handlers:
        # 创建两个handler
        fh = logging.FileHandler("test.log", encoding="utf-8")
        ch = logging.StreamHandler()

        # 设置输出日志格式
        formatter = logging.Formatter(
            fmt="%(asctime)s %(name)s %(filename)s %(message)s",
            datefmt="%Y/%m/%d %X"
        )

        # 为两个handler指定输出格式
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 为logger添加的日志处理器
        logger.addHandler(fh)
        logger.addHandler(ch)
    return logger  # 直接返回logger


logger = log()
logger.warning("泰拳警告")
logger.info("提示")
logger.error("错误")
logger.debug("查错")
