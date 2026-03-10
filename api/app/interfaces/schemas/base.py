from typing import TypeVar, Generic, Optional
from pydantic import BaseModel, Field

T = TypeVar('T')

class Response(BaseModel, Generic[T]):
    code: int = 200 # 业务状态码，和HTTP状态码保持一致
    message: str = "success" # 业务状态信息
    data: Optional[T] = Field(default_factory=dict, description="响应数据")

    @staticmethod
    def success(data: Optional[T] = None, message: str = "success") -> 'Response[T]':
        """创建一个成功的响应对象"""
        return Response(code=200, message=message, data=data)
    
    @staticmethod
    def fail(code: int, message: str, data: Optional[T] = None) -> 'Response[T]':
        """创建一个失败的响应对象"""
        return Response(code=code, message=message, data=data if data is not None else {})