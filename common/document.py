"""
文档处理模块，
处理依据文档。
"""
import json
from docs import doc


class Event(object):
    def __init__(self, name, url, method, rsp, body=None):
        self.name = name
        self.url = url
        self.method = method
        self.rsp = json.loads(rsp)
        self.body = body


def output_event():
    """
    输出一个个待测试对象。
    """
    base = doc.BASE_URL
    for eve in doc.TEST_LIST:
        event = Event(
            eve['name'],
            base + eve['url'],
            eve['method'],
            eve['response'],
            eve.get('body')
        )
        yield event
