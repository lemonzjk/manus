# manus
Multi-Agent System

## 目录结构
```
manus：
└── api
    ├── app：项目整个代码信息
    │   ├── interfaces：接口层
    │   │   ├── endpoints/api：接口定义
    │   │   ├── errors：错误处理相关内容
    │   │   ├── middleware：中间件
    │   │   └── schemas：输入输出的数据结构
    │   ├── application：应用层
    │   │   ├── services/usercases：很薄的服务
    │   │   └── errors：错误处理相关内容
    │   ├── domain：领域层
    │   │   ├── models：实体信息
    │   │   ├── repositories：仓储信息，这里定义接口
    │   │   ├── services：领域服务
    │   │   └── external：外部工具、缓存、读写信息等，这里定义接口
    │   ├── infrastructure：基础设施层
    │   │   ├── external：外部工具、缓存、读写信息等，实现领域层接口
    │   │   ├── repositories：仓储信息，实现领域层接口
    │   │   ├── logging：日志处理
    │   │   ├── storage：存储相关内容
    │   │   │   ├── postgres.py
    │   │   │   ├── redis.py
    │   │   │   └── cos.py
    │   │   └── models：存储表信息
    │   └── main.py：项目入口文件
    ├── core：配置信息
    │   └── config.py
    ├── tests：测试
    ├── .env：环境变量
    ├── dev.sh：开发环境
    ├── run.sh：生产环境
    └── Dockerfile：docker 配置信息
```