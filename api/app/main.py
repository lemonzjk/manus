from fastapi import FastAPI
from core.config import get_settings

# 1. 加载配置信息
settings = get_settings()
print("加载配置:", settings)

# 2. 创建 FastAPI 应用实例
app = FastAPI()
