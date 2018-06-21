"""
报告处理模块，生成报告文档。
"""
from common.obtain import Reply


class Fence(object):
    def __init__(self):
        self.type = None
        self.assess = None


class Result(object):
    def __init__(self, name):
        self.name = name
        self.fences = []
        self.polymerization = None

    def one_fence(self, floor, exm, rsp):
        """
        一条报告。
        """

    def group_fences(self):
        """
        汇总每条结果。
        """


def generate_report(reply: Reply):
    """
    一个api的报告
    """
    result = Result(reply.name)
    if not reply.error:
        pass
    else:
        pass
    return result


def summary_report():
    """
    汇总报告形成总结
    :return:
    """
    pass
