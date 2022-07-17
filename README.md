# dashboard [个人渗透测试工作台]

## 背景

安全行业小工具太多太杂，完全套用第三方工具，用起来要么是脚本小子，要么用起来各有各的优点和缺点。

## 系统架构

后端：

- Python 3.10+
- FastAPI
- APScheduler # 处理定时任务
- SQLAlchemy
- alembic # 数据库迁移
- celery # 队列任务

前端：

- Vue 3
- Vue-Router
- [tabler](https://tabler.io/) # 页面模板

组件依赖

- MySQL
- Redis

目录结构

- app/core/ 文件夹下对应所有的 web 程序内容
  - configs/ 系统配置，部分配置从 .env 读取
  - controllers/ controller 层
  - curd/ curd 语句相关
  - db/ 数据库连接处理
  - middleware/ 系统中间件
  - models/ 所有的 models
  - requests/ 参考 laravel 的 request，对表单字段校验
  - routes/ 后端 api 端点路由入口
  - schemas/

- frontend/dashboard vue3 主入口
  - src 源文件目录
  - public 引用的第三方资源，编译时不统一打包

## 部署方法

### docker 部署

待定

### 直接部署

待定