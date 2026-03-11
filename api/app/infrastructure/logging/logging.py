from core.config import get_settings
import logging
import sys

def setup_logging():
    """设置日志配置，使用 Python 内置的 logging 模块，涵盖日志等级、输出格式、输出渠道等"""
    # 1. 获取配置信息
    settings = get_settings()

    # 2. 获取根日志处理器
    root_logger = logging.getLogger() # 这里是可以传文件名字的，传了就会创建一个新的日志处理器，不传就获取根日志处理器

    # 3. 设置根日志处理器等级
    log_level = getattr(logging, settings.log_level.upper(), logging.INFO) # 从配置中获取日志等级，默认为 INFO
    root_logger.setLevel(log_level)

    # 4. 创建日志格式器
    log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s" # 日志输出格式
    date_format = "%Y-%m-%d %H:%M:%S" # 日期时间格式
    formatter = logging.Formatter(log_format, date_format)

    # 5. 创建控制台日志处理器
    console_handler = logging.StreamHandler(sys.stdout) # 创建控制台日志处理器， 流式输出到标准输出
    console_handler.setLevel(log_level) # 设置控制台日志处理器等级
    console_handler.setFormatter(formatter) # 设置控制台日志处理器格式

    # 6. 将控制台日志处理器添加到根日志处理器
    root_logger.addHandler(console_handler)

    root_logger.info("日志系统已初始化，日志等级: %s", settings.log_level)