"""
报告处理模块，生成报告文档。
"""
from common.obtain import Reply


class Fence(object):
    level = {
        0: "完全相同",
        1: "值不同",
        2: "keys不同",
        3: "类型不同",
    }

    def __init__(self, floor, t_name):
        self.type = t_name
        self.floor = floor
        self.assess = None


class Result(object):
    def __init__(self, name):
        self.name = name
        self.fences = []
        self.polymerization = None

    def _append(self, fence: Fence, level):
        fence.assess = level
        self.fences.append(fence)

    def one_fence(self, floor, exm, rsp):
        """
        一条报告。
        """

        t_exm = type(exm)
        t_rsp = type(rsp)
        fence = Fence(floor, t_exm.__name__)
        if t_exm != t_rsp:
            self._append(fence, 3)
        elif t_rsp == dict:
            if exm.keys() == rsp.keys():
                self._append(fence, 0)
                for key in exm.keys():
                    self.one_fence(floor + 1, exm[key], rsp[key])
            else:
                self._append(fence, 2)
        elif t_rsp == list:
            if len(exm) == len(rsp):
                self._append(fence, 0)
                for index in range(len(exm)):
                    self.one_fence(floor + 1, exm[index], rsp[index])
            else:
                self._append(fence, 1)
        elif exm is None:
            self._append(fence, 0)
        else:
            fence.assess = 0 if exm == rsp else 1
            self.fences.append(fence)

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
