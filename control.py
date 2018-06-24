"""
控制模块，程序入口。
"""
from common.document import output_event
from common.obtain import get_reply
from common.report import generate_report, Polymerisation


def main():
    events = output_event()
    f = open('report.txt', 'w', encoding='utf-8')
    polymerisation = Polymerisation(f)
    try:
        while True:
            event = next(events)
            reply = get_reply(event)
            report_dic = generate_report(reply, f)
            polymerisation.report_append(report_dic)
    except StopIteration:
        pass
    polymerisation.output()
    f.close()


if __name__ == "__main__":
    main()
