from microbit import *
from enum import *


class ASR(object):
    """基本描述

    语音识别传感器

    Returns:
        value: 识别到的语音条目
    """

    def __init__(self, RJ_pin):
        pass

    def get_ASR(self):
        """基本描述

        获取一氧化碳值

        """
        t = i2c.read(0x0B, 1)
        return t[0]


if __name__ == '__main__':
    asr = ASR()
    while True:
        print(asr.get_ASR())
