from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.infrastructure.logging import setup_logging
from app.interfaces.endpoints.routes import router

import logging
from core.config import get_settings
from contextlib import asynccontextmanager 

# 1. 加载配置信息
settings = get_settings()
print("加载配置:", settings)

# 2. 设置日志系统
setup_logging()
logger = logging.getLogger() # 获取根日志处理器，如果传名字就会创建一个新的日志处理器

# 3. 定义 FastAPI 路由 tags 标签
openapi_tags = [
    {
        "name": "状态模型",
        "description": "包含 **状态检测** 等 API 接口，用于监测系统的运行状态。"
    }
]

@asynccontextmanager
async def lifespan(app: FastAPI):
    """FastAPI 的生命周期事件处理器，包含应用启动和关闭时的逻辑"""
    # 应用启动时的逻辑
    logger.info("Manus 正在初始化...")
    # TODO 内容：这里可以添加一些启动时需要执行的操作，比如连接数据库、初始化资源等
    try:
        yield # 这里是 FastAPI 的生命周期事件处理器的核心，yield 之前的代码在应用启动时执行，yield 之后的代码在应用关闭时执行
    except Exception as e:
        logger.error(f"应用启动时发生错误: {e}")
    finally:
        # 应用关闭时的逻辑
        logger.info("Manus 正在关闭...")

# 4. 创建 FastAPI 应用实例
app = FastAPI(
    title="Manus 通用智能体 API",
    description="Manus 是一个通用的AI Agent系统，可以完全私有部署，使用A2A+MCP连接Agent/Tool，同时支持在沙箱中运行各种内置工具和操作。",
    version="1.0.0",
    openapi_tags=openapi_tags,
    lifespan=None # FastAPI 的生命周期事件处理器
)

# 5. 配置 CORS 中间件，允许所有来源的请求，解决跨域问题
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # 允许所有来源的请求
    allow_credentials=True, # 允许携带凭证（如 cookies）
    allow_methods=["*"], # 允许所有 HTTP 方法
    allow_headers=["*"], # 允许所有 HTTP 头部
)

# 6. 导入并注册路由
app.include_router(router, prefix="/api")
