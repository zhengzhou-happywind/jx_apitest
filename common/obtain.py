"""
获取响应模块。
"""
import json
import requests
from requests.exceptions import ConnectionError
from common.document import Event


class Reply(object):
    """
    将示例响应和真实响应组织到一起。
    """

    def __init__(self, name, example):
        self.name = name
        self.example = example
        self.response = None
        self.error = None


def get_reply(event: Event):
    reply = Reply(event.name, event.rsp)
    try:
        re = requests.request(event.method, event.url, data=event.body)
        response = json.loads(re.text)
        reply.response = response
    except ConnectionError:
        reply.error = "404未能连接"
    return reply
