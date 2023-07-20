# bardchat
- 基于[acheong08/Bard](https://github.com/acheong08/Bard)使用谷歌Bard接口，实现简单HTML网页版在线聊天（支持连续对话及会话隔离）
- 更多问题可参考官方[FAQ](https://bard.google.com/faq)
### 部署
#### 获取COOKIE
- 打开https://bard.google.com
  + F12打开浏览器控制台
  + 打开`应用程序`-`Cookie`，在对应上方网址的COOKIE里找到`__Secure-1PSID`及`__Secure-1PSIDTS`字段，复制其`value`值备用
#### 使用Docker Compose配置
- 新建`docker-compose.yml`文件，粘贴以下内容并保存
```bash
services:
  chatgpt:
    image: sheepgreen/bard-web
    container_name: bardchat
    environment:
      - BARD__Secure_1PSID=上方获取到的value值
      - BARD__Secure_1PSIDTS=上方获取到的value值
    ports:
      - "9898:8088" #8088为容器内端口，不可更换；9898为外部端口，可自行更换
    restart: always
```
- 输入`docker-compose up -d`即启动成功
### 注意事项
- 访问地址为http://ip:port
