from microbit import *

HT16K33_ADDRESS = 0x70

HT16K33_BLINK_CMD = 0x80

HT16K33_BLINK_DISPLAYON = 0x01

HT16K33_CMD_BRIGHTNESS = 0xE0


class MATRIX(object):
    """基本描述

    8x16 点阵显示屏

    """

    def __init__(self):
        i2c.init()
        self.__initmodule()
        self.__matBuf = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    def __i2cwrite_matrix(self, addr, reg):
        i2c.write(addr, bytearray([reg]))

    def __initmodule(self):
        self.__i2cwrite_matrix(HT16K33_ADDRESS, 0x21)
        self.__i2cwrite_matrix(HT16K33_ADDRESS, HT16K33_BLINK_CMD | HT16K33_BLINK_DISPLAYON | (0 << 1))
        self.__i2cwrite_matrix(HT16K33_ADDRESS, HT16K33_CMD_BRIGHTNESS | 0xF)

    def __matrix_show(self):
        self.__matBuf[0] = 0x00
        i2c.write(HT16K33_ADDRESS, bytearray([
            self.__matBuf[0], self.__matBuf[1], self.__matBuf[2], self.__matBuf[3], self.__matBuf[4], self.__matBuf[5],
            self.__matBuf[6], self.__matBuf[7], self.__matBuf[8], self.__matBuf[9], self.__matBuf[10],
            self.__matBuf[11],
            self.__matBuf[12], self.__matBuf[13], self.__matBuf[14], self.__matBuf[15], self.__matBuf[16]]))

    def set_matrix_clear(self):
        """

        清空点阵显示屏

        """
        for i in range(17):
            self.__matBuf[i] = 0
        self.__matrix_show()

    def set_matrix_draw(self, x, y):
        """

        点亮个像素点

        Args:
            x (number): X 轴  0-15
            y (number): Y 轴  0-7

        Returns:
            NONE
        """
        idx = int(y) * 2 + int(x) // 8
        tmp = self.__matBuf[idx + 1]
        tmp |= (1 << (x % 8))
        self.__matBuf[idx + 1] = tmp
        self.__matrix_show()

    def set_matrix_expression(self, expression):
        """

        显示一个emoji表情

        Args:
            expression (str): 表情，字符串

        Returns:
            NONE
        """
        if expression == "Neutral":
            point = [[2, 1], [3, 1], [13, 1], [12, 1],
                     [2, 2], [3, 2], [13, 2], [12, 2],
                     [2, 3], [3, 3], [13, 3], [12, 3],
                     [5, 5], [6, 5], [7, 5], [8, 5], [9, 5], [10, 5],
                     [5, 6], [6, 6], [7, 6], [8, 6], [9, 6], [10, 6]
                     ]
        elif expression == "Sad":
            point = [[1, 2], [5, 2], [10, 2], [14, 2],
                     [1, 3], [2, 3], [3, 3], [4, 3], [5, 3], [10, 3], [11, 3], [12, 3], [13, 3], [14, 3],
                     [2, 4], [3, 4], [4, 4], [11, 4], [12, 4], [13, 4],
                     [6, 6], [7, 6], [8, 6], [9, 6],
                     [5, 7], [10, 7]
                     ]
        elif expression == "Smile":
            point = [[2, 1], [3, 1], [13, 1], [12, 1],
                     [2, 2], [3, 2], [13, 2], [12, 2],
                     [2, 3], [3, 3], [13, 3], [12, 3],
                     [5, 5], [10, 5],
                     [6, 6], [7, 6], [8, 6], [9, 6]
                     ]
        elif expression == "Angry":
            point = [[2, 0], [13, 0],
                     [3, 1], [12, 1],
                     [3, 2], [4, 2], [11, 2], [12, 2],
                     [3, 3], [4, 3], [11, 3], [12, 3],
                     [6, 6], [7, 6], [8, 6], [9, 6],
                     [5, 7], [10, 7]
                     ]
        else:
            pass
        self.set_matrix_clear()
        for i in range(len(point)):
            self.set_matrix_draw(point[i][0], point[i][1])


if __name__ == '__main__':
    dis = MATRIX()
    x, y = 0, 0

    for y in range(8):
        for x in range(16):
            dis.set_matrix_draw(x, y)
    dis.set_matrix_clear()
    dis.set_matrix_expression("Angry")
    sleep(500)
    dis.set_matrix_expression("Sad")
    sleep(500)
    dis.set_matrix_expression("Smile")
