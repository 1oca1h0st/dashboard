# dashboard [个人渗透测试工作台]

## 背景

 - 安全行业小工具太多太杂，完全套用第三方工具，用起来要么是脚本小子，要么用起来各有各的优点和缺点。
 - SOAR的模式使用起来总是不如直接上手写代码快，详情可参考：[一次失败的SOAR产品体验](https://blog.mrtblogs.net/soar/)
 - 行业内也有很多优秀的产品，例如巡风/Kunpeng/ARL/EasyPen等，但都侧重在PoC上或很久没有维护更新了
 - 这个系统的目的是为了整合这些优秀的产品，同时提供尽量灵活的配置模式和使用体验

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

- MySQL / MongoDB(建议)
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


- workers 命令执行模块 *使用celery对接*
  - assets 资产扫描模块
  - pocs
  - tests 自动化测试文件夹


## 部署方法

### docker 部署

``docker-compose up -d``

目前添加了 mongodb 和 redis 镜像

### 直接部署

python -m venv venv && source venv/bin/activate && python -m pip install -r requirements.txt