from fastapi import FastAPI
from core.config import get_settings
from app.infrastructure.logging import setup_logging
import logging

# 1. 加载配置信息
settings = get_settings()
print("加载配置:", settings)

# 2. 设置日志系统
setup_logging()
logger = logging.getLogger() # 获取根日志处理器，如果传名字就会创建一个新的日志处理器

# 创建 FastAPI 应用实例
app = FastAPI()
