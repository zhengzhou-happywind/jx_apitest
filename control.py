"""
控制模块，程序入口。
"""
from common.document import output_event
from common.obtain import get_reply
from common.report import generate_report


def main():
    events = output_event()
    try:
        while True:
            event = next(events)
            reply = get_reply(event)
            generate_report(reply)
    except StopIteration:
        pass


if __name__ == "__main__":
    main()
