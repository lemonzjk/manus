"""管理所有的路由"""

from fastapi import APIRouter
from . import status_routes

def create_api_routes() -> APIRouter:
    """创建API路由，包含所有的子路由"""
    # 1. 创建主路由
    api_router = APIRouter()

    # 2. 导入子路由
    api_router.include_router(status_routes.router)

    # 3. 返回主路由
    return api_router

router = create_api_routes()
