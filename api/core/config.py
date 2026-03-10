from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache

class Settings(BaseSettings):
    """应用配置类，使用 pydantic_settings 进行管理，从 .env 文件或者环境变量中加载配置"""
    
    # 基础配置
    env: str = "development" # 环境，默认为 development
    log_level: str = "INFO" # 日志级别，默认为 INFO

    # 数据库配置
    sqlalchemy_database_url: str = "" # SQLAlchemy 数据库连接 URL

    # Redis 配置
    redis_host: str = "localhost" # Redis 主机地址
    redis_port: int = 6379 # Redis 端口
    redis_db: int = 0 # Redis 数据库索引
    redis_password: str | None = None # Redis 密码

    # 使用 pydantic v2 的写法来完成环境变量信息的告知
    model_config = SettingsConfigDict(
        env_file=".env", # 指定环境变量文件
        env_file_encoding="utf-8", # 环境变量文件编码
        extra="ignore" # 忽略未定义的环境变量
    )

@lru_cache()
def get_settings() -> Settings:
    """获取应用配置实例，使用 lru_cache 来缓存实例，避免重复创建"""
    return Settings()