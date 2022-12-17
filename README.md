# cqhttp-based-bot
#### 基于cqhttp的自动回复机器人Aki-demo
#### 用于个人学习尝试，可部署在服务器上，其他参数文件就不介绍了
#### ubuntu server 上借助screen使用如下命令：
#### 创建名为cqhttp的screen窗口，运行go-cqhttp
`screen -S cqhttp`
#### 切换路径至该项目
`cd cqhttp-based-bot`
#### 授予文件权限
`sudo chmod 777 ./go-cqhttp`
#### 运行go-cqhttp
`./go-cqhttp`
#### Ctrl+D切出cqhttp窗口
#### 创建名为python的screen窗口，运行listen.py
`sceen -S python`
`python3 listen.py`
#### Ctrl+D切出python窗口
#### 至此已部署完毕
