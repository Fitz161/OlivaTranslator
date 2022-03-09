# -*- encoding=utf8 -*-

BAIDU_TRANS_ID = ''
BAIDU_TRANS_KEY = ''
MAX_SEND_LENGTH = 200

ERROR_MSG = '格式错误，请使用\n翻译成[目标语言] [待翻译文本]\n的格式发送消息。'
HELP_DOC = '请使用:\n翻译成[目标语言] [待翻译文本]\n的格式发送消息，原文本语种会自动识别。\n发送[翻译 语言]查看可用语言'
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 Edg/97.0.1072.62'
LANGUAGE_DICT = {'中文': 'zh', '英语': 'en', '粤语': 'yue', '文言文': 'wyw', '日语': 'jp', '韩语': 'kor', '法语': 'fra', '西班牙语': 'spa', '泰语': 'th', '阿拉伯语': 'ara', '俄语': 'ru', '葡萄牙语': 'pt', '德语': 'de', '意大利语': 'it', '希腊语': 'el', '荷兰语': 'nl', '波兰语': 'pl', '保加利亚语': 'bul', '爱沙尼亚语': 'est', '丹麦语': 'dan', '芬兰语': 'fin', '捷克语': 'cs', '罗马尼亚语': 'rom', '斯洛文尼亚语': 'slo', '瑞典语': 'swe', '匈牙利语': 'hu', '繁体中文': 'cht', '越南语': 'vie'}
REQUEST_API = 'http://fanyi-api.baidu.com/api/trans/vip/translate'
ERROR_CODE = ['52001', '52002' '52003', '54000', '54001', '54002', '540003', '54004', '54005', '58000', '58001', '58002', '90107']


