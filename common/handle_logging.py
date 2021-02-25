
import os
import logging
import logging.handlers
import time

from common.handle_config import read_config
from common.handle_path import LOG_PATH

file_path = os.path.join(LOG_PATH, str(time.strftime('%Y-%m-%d',time.localtime())) + '.log')

def logger_handler():
    """
    创建日志收集器
    :return: 定制好的日志收集器
    """
    log = logging.getLogger("test")  # 获取日志收集器对象
    log.setLevel(read_config.get("log", "level"))  # 为日志收集器对象设置收集等级

    file_output = logging.handlers.TimedRotatingFileHandler(file_path, when='D', interval=1, backupCount=0, encoding='utf8')  # 设置log文件输出
    # file_output.suffix = '%Y-%m-%d.log'
    file_output.setLevel(read_config.get("log", "file_output_level"))

    console_output= logging.StreamHandler()  # 设置控制台输出
    console_output.setLevel(read_config.get("log", "console_output_level"))

    log.addHandler(file_output)  # 把handler添加到日志收集器中
    log.addHandler(console_output)

    formatter = logging.Formatter('%(asctime)s -- [%(filename)s-->line:%(lineno)d] - %(levelname)s: %(message)s')   # 日志格式
    file_output.setFormatter(formatter)
    console_output.setFormatter(formatter)

    file_output.close()
    console_output.close()

    return log

log = logger_handler()