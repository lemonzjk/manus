from .logging import setup_logging

# 定义 __all__ 列表，明确暴露的模块接口，方便其他模块导入和使用
# 这样直接就能从 app.infrastructure.logging 导入 setup_logging 函数，而不需要知道具体的 logging 模块结构
__all__ = ["setup_logging"] 