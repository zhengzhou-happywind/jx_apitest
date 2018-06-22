"""
控制模块，程序入口。
"""
from common.document import output_event
from common.obtain import get_reply
from common.report import generate_report


def main():
    events = output_event()
    f = open('report.txt', 'w')
    try:
        while True:
            event = next(events)
            reply = get_reply(event)
            result = generate_report(reply, f)
    except StopIteration:
        pass
    f.close()


if __name__ == "__main__":
    main()
