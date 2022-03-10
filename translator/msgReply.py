# -*- encoding=utf8 -*-

import random
import hashlib
import requests


from translator.config import *

command_dict = {}


def add_command(command):
    """ 命令的装饰器 """
    def add_func(func):
        command_dict[command] = func
    return add_func


@add_command('帮助')
def help_doc(plugin_event, _):
    return HELP_DOC


@add_command('help')
def help(plugin_event, _):
    return HELP_DOC


@add_command('语言')
def language_doc(plugin_event, _):
    reply_msg = '已支持语言:\n' + ' '.join(LANGUAGE_DICT.keys())
    return reply_msg


@add_command('成')
def get_translate_result(plugin_event, _):
    message = plugin_event.data.message[3:].strip()
    type, text = message[:message.find(' ')], message[message.find(' ')+1:]
    dst_type = LANGUAGE_DICT.get(type)
    if not text or not dst_type:
        return ERROR_MSG

    data = concat_post_data(text, dst_type)
    result = request_post(data)
    if isinstance(result, str):
        return '请求错误\n' + result
    if result.get('error_code') in ERROR_CODE:
        # 翻译结果返回错误码
        return '请求错误 \nerror_code:' + str(result.get("error_code"))

    reply_msg = ''
    trans_result = result.get('trans_result')
    for item in trans_result:
        reply_msg += item.get('dst') + '\n'
    reply_msg = text[:10] + '...翻译成'+ type + ':\n' + reply_msg[:-1]
    return reply_msg


@add_command('为')
def get_translate_result_dup(plugin_event, _):
    get_translate_result(plugin_event, _)


def concat_post_data(text, dst_type):
    """ 构造百度翻译api的请求参数 """
    salt = str(random.randint(1000000000, 9999999999))
    md5 = hashlib.md5()
    md5.update((BAIDU_TRANS_ID + text + salt + BAIDU_TRANS_KEY).encode('utf8'))
    sign = md5.hexdigest()
    data = {
        'q': text,
        'from': 'auto',
        'to': dst_type,
        'appid': BAIDU_TRANS_ID,
        'salt': salt,
        'sign': sign
    }
    return data


def request_post(data, type='json'):
    """使用post请求访问指定url"""
    headers = {
        "User-Agent": USER_AGENT,
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    try:
        response = requests.post(REQUEST_API, data, headers=headers, timeout=8)
        if response.status_code == 200 or response.status_code == 304:
            response.encoding = 'utf-8'
            if type == 'text':
                return response.text
            elif type == 'json':
                return response.json()
            elif type == 'content':
                return response.content
        else:
            return "request failed"
    except requests.RequestException:
        return "time out"
    except ValueError:
        return 'jsonify failed'


def unity_init(plugin_event, Proc):
    if not BAIDU_TRANS_ID or not BAIDU_TRANS_KEY:
        Proc.log(
            log_level=2,
            log_message='translator初始化失败，请手动前往config.py配置翻译API',
            log_segment=[
                ('translator', 'default'),
                ('Init', 'default')
            ]
        )
    else:
        Proc.log(
            log_level=2,
            log_message='translator初始化完成',
            log_segment=[
                ('translator', 'default'),
                ('Init', 'default')
            ]
        )


def unity_reply(plugin_event, Proc):
    message = plugin_event.data.message
    if message[:2] not in ['翻译'] or len(message) < 3: return
    if not BAIDU_TRANS_ID or not BAIDU_TRANS_KEY: return
    if message[2] in ['成', '为']:
        reply_msg = command_dict.get(message[2])(plugin_event, Proc)
        plugin_event.reply(reply_msg[:MAX_SEND_LENGTH])
        return
    if message[3:].strip() in command_dict.keys():
        reply_msg = command_dict.get(message[3:].strip())(plugin_event, Proc)
        plugin_event.reply(reply_msg[:MAX_SEND_LENGTH])
        return
