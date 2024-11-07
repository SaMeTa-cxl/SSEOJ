# SSEOJ
基于DRF+Vue的OnlineJudge平台

## 部署方法
1. 在项目根目录下调用`pip install -r requirements.txt`命令，下载项目所需的依赖项
2. 修改`settings.py`配置你的数据库，建议使用MySql数据库来尽可能减少配置修改，你需要在本地创建名为`SSEOJ`的数据库，然后将数据库配置信息中的用户名和密码改成你自己的，接着执行`python manage.py migrate`，若无错误将成功在你的本地创建好数据库（**这一部分之后可能用脚本完成**）
3. 执行`python manage.py runserver`即可运行项目
