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

    def __init__(self, since, t_name):
        self.type = t_name
        self.since = since
        self.assess = None


class Result(object):
    def __init__(self, name):
        self.name = name
        self.fences = []
        self.polymerization = None

    def _append(self, fence: Fence, level):
        fence.assess = level
        self.fences.append(fence)

    def one_fence(self, since, exm, rsp):
        """
        递归的得到整个结构的对比分级。
        """

        t_exm = type(exm)
        t_rsp = type(rsp)
        fence = Fence(since, t_exm.__name__)
        if t_exm != t_rsp:
            self._append(fence, 3)
        elif t_rsp == dict:
            if exm.keys() == rsp.keys():
                self._append(fence, 0)
                for key in exm.keys():
                    self.one_fence(since + "->" + key, exm[key], rsp[key])
            else:
                self._append(fence, 2)
        elif t_rsp == list:
            if len(exm) == len(rsp):
                self._append(fence, 0)
                for index in range(len(exm)):
                    self.one_fence(
                        since + "->" + str(index),
                        exm[index], rsp[index])
            else:
                self._append(fence, 1)
        elif exm is None:
            self._append(fence, 0)
        else:
            fence.assess = 0 if exm == rsp else 1
            self.fences.append(fence)

    def group_fences(self, level, f):
        """
        汇总每条结果。
        """
        for fence in self.fences:
            if fence.assess >= level:
                msg = "[%s]-{ %s }-%s\n" % (
                    fence.assess,
                    fence.since,
                    fence.level[fence.assess]
                )
                f.write(msg)


def generate_report(reply: Reply, f):
    """
    一个api的报告
    """
    result = Result(reply.name)
    f.write(reply.name + ':\n')
    if not reply.error:
        result.one_fence('root', reply.example, reply.response)
        result.group_fences(2, f)
    else:
        pass
    return result


def summary_report():
    """
    汇总报告形成总结
    :return:
    """
    pass
