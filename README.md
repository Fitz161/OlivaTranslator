## OlivaTranslator

### 介绍
基于 [OlivOS](https://github.com/OlivOS-Team/OlivOS) 框架的多语言翻译插件

### 下载
从本项目下载源码，**进行配置后**，压缩为zip格式并将后缀名改为opk放入 `plugin/app` 目录下<br>由于本插件需手动配置，暂不发布整合包。

### 配置
- 本插件依赖requests，OlivOS默认已安装该依赖
- 本插件使用百度翻译API，请在[百度翻译开放平台](https://fanyi-api.baidu.com/doc/13)注册开发者，开启标准版API服务
- 在百度翻译控制台获取APP ID和密钥，并分别填入 `config.py` 文件中 `BAIDU_TRANS_ID `和 `BAIDU_TRANS_KEY` 字段。注意，本插件仅使用ID和密钥构造翻译请求，不会上传或发布到其它地方，储存密钥的文件请不要分享暴露给他人。

### 使用说明
- `翻译 帮助` 查看本插件使用帮助
- `翻译 语言` 查看支持翻译的语种
- `翻译成[目标语言] [待翻译文本]` 将文本翻译成指定语言，会自动识别原文本语种，只需指定目标语言。 例 `翻译成英语 你好`
- 本插件限制最大发送字数为200,可在 `config.py` 文件中 `MAX_SEND_LENGTH` 字段中修改
  
### 指令扩展
本插件具有方便的指令扩展功能<br>
在`msgReply.py`文件中使用以下格式即可定义新指令
```
@add_command('新命令')
def func_name(plugin_event, _):
    ...
    return '待发送的消息'
```
使用 `翻译 新命令` 方式调用指令<br>
**注意**：在编写新指令的过程中一定要知道自己在做什么，否则可能会导致无法意料的后果
