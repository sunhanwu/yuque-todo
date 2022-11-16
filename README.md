# yuque-todo

本方案提供语雀内置的webhook实现将语雀文档上的待办事项自动同步到滴答清单和Apple日历、谷歌日历等

[toc]



## framework
![](https://ipic-picgo.oss-cn-beijing.aliyuncs.com/20221117010937.png)
## setup
### 1. 部署yuque-todo机器人

- 下载源码
```python
git clone git@github.com:sunhanwu/yuque-todo.git
```

- 安装环境
```bash
pip install -r requirements.txt
```

- 运行
```bash
usage: app.py [-h] [--port PORT] --fromAddr FROMADDR --password PASSWORD
              --didaAddr DIDAADDR [--smtpServer SMTPSERVER]
              [--smtpPort SMTPPORT]
app.py: error: the following arguments are required: --fromAddr, --password, --didaAddr
```

   - 必选项
      - --fromAddr: 发件地址
      - --password: 邮箱授权码
      - --didaAddr: 滴答清单专属邮箱
   - 可选项
      - --port: yuque-todo机器人运行端口, 默认5000
      - --smtpServer: 发件邮箱服务器，默认smtp.qq.com
      - --smtpPort: 发件邮箱端口, 默认465
```bash
python app.py --fromAddr=xxx@qq.com --password=xxx --didaAddr=xxx
```
### 2. 配置滴答清单

- [登录](https://dida365.com/webapp/#settings/subscribe)滴答清单网页版-->设置-->日历、邮件与集成：

![image.png](https://ipic-picgo.oss-cn-beijing.aliyuncs.com/20220627110042.png)

### 3. 获取qq邮箱授权码

- [登录](https://mail.qq.com/)qq邮箱网页版-->设置-->账户
   - 开启pop3/smtp服务
   - 生成授权码

![](https://ipic-picgo.oss-cn-beijing.aliyuncs.com/20220627110153.png)
### 4. 配置语雀webhook

- 登录[语雀网页版](https://www.yuque.com/dashboard)
- 选择想要同步的知识库
- 点击右上角三个点然后选择更多设置
- 选择消息推送
- 选择其他渠道
- 添加机器人

![](https://ipic-picgo.oss-cn-beijing.aliyuncs.com/20220627110208.png)

- 机器人名字随便设置
- webhook是上面的yuque-todo服务器地址(要公网地址)
   - eg: http://xx.xx.xx.xx:5000/
### 5. 配置日历

- 复制滴答清单订阅链接
- 设置Apple日历(以iphone为例)
   - 点击日历下方的`日历!`
   - 点击添加日历-->添加订阅日历
   - 粘贴订阅链接-->添加
   - 效果如下

![](https://ipic-picgo.oss-cn-beijing.aliyuncs.com/20220627110221.png)

- 设置Google日历
   - 登录[Google日历网页版](https://calendar.google.com/calendar/u/0/r?pli=1)
   - 点击左下角添加日历-->订阅日历
   - 粘贴订阅链接
## usage

1. 打开语雀文档(在配置了webhook的知识库内)
1. 新建待办事项。格式如下
   1. 时间: 内容滴答
> 后面的滴答是语雀的状态，用于控制待办事项是否需要同步

![](https://ipic-picgo.oss-cn-beijing.aliyuncs.com/20220627110243.png)

3. 点击发布文档
4. 然后就自动同步到滴答清单和配置了订阅链接的日历中

## todo

+ bugs fix
+ [x] 待办事项重复添加
+ [ ] 微信提醒重复
+ function
+ [ ] webhook接口无认证机制
+ [ ] 支持更加灵活的待办事项语法
+ [ ] 支持统计汇总功能
+ [ ] 完善log输出
+ future
+ [ ] 支持语雀文档自动同步到Halo作为个人博客
+ [ ] 支持Docker部署
+ [ ] 支持yuqu-todo与WeChatBot一起部署
