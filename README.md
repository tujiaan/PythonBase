# Python基础架构
## 基本信息
* /admin为管理系统
* /api/v1/为相关接口文档
* 配置文件在intance/config
* 初始化数据库 python init_database.py
## 部署启动
### 普通部署
#### 部署步骤
1. 进入程序目录
1. 安装基础依赖```pip install virtualenv```
1. 创建虚拟运行环境```virtualenv venv```
1. 使用虚拟运行环境```source venv/bin/activate``
1. 安装程序依赖```pip install -r requirements.txt```
1. 启动程序```gunicorn -w 2 -b 0.0.0.0:80 run:application -D```

#### Daemon 文件
```
[Unit]
Description=web
After=network.target

[Service]
Type=simple
User=root
ExecStart=/gunicorn -w 2 -b 0.0.0.0:80 run:application

[Install]
WantedBy=multi-user.target
```
### Docker部署
#### 普通Docker部署
建立镜像

```docker build -t kaive/yiyiwei_backend .```

运行docker

```
docker run -p 8080:80  \
            -v $(pwd):/usr/src/app \
            -d kaive/wangguan
docker run --name yiyiwei-db \
            -d --env MYSQL_ROOT_PASSWORD=yangjiawei \
            --env MYSQL_DATABASE=yiyiwei \
            --env MYSQL_USER=yiyiwei \
            --env MYSQL_PASSWORD=yiyiwei \
            -p 3306:3306 \
            mariadb:10.2 \
            --character-set-server=utf8mb4 \
            --collation-server=utf8mb4_unicode_ci
```


#### Docker Compose 部署
修改docker-compose.yml对应文件

```docker-compose run -d --service-ports  backend```