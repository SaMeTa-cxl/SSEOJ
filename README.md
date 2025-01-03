# SSEOJ
基于DRF+Vue的OnlineJudge平台

## 部署方法
1. 在项目根目录下调用`pip install -r requirements.txt`命令，下载项目所需的依赖项
2. 修改`settings.py`配置你的数据库，建议使用MySql数据库来尽可能减少配置修改，你需要在本地创建名为`SSEOJ`的数据库，然后将数据库配置信息中的用户名和密码改成你自己的，接着执行`python manage.py migrate`，若无错误将成功在你的本地创建好数据库（**这一部分之后可能用脚本完成**）
3. 执行`python manage.py runserver`运行项目本体
4. 安装并启动redis，windows下建议使用docker运行redis：运行命令为`docker run --name redis -p 6379:6379 -d redis`
这将会自动拉取redis镜像并运行
5. 接下来需要启动判题服务器，在JudgeServer项目目录下使用`docker-compose up -d`即可
6. 最后需要启动**dramatiq worker**， 只需要在本项目目录下执行`python manage.py rundramatiq`即可
