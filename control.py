"""
控制模块，程序入口。
"""
from common.document import output_event


def main():
    events = output_event()
    try:
        while True:
            event = next(events)

    except StopIteration:
        pass


if __name__ == "__main__":
    main()
