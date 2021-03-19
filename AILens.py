from microbit import *

Camera_Add = 0x14
Card = 2
Face = 6
Ball = 7
Tracking = 8
Color = 9
Learn = 10
numberCards = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
letterCards = ["A", "B", "C", "D", "E"]
otherCards = ["Mouse", "micro:bit", "Ruler", "Cat", "Peer", "Ship", "Apple", "Car", "Pan", "Dog", "Umbrella",
              "Airplane", "Clock", "Grape", "Cup", "Turn left", "Turn right", "Forward", "Stop", "Back"]
colorList = ["Green", "Blue", "Yellow", "Black", "Red", "White"]


class AILENS(object):
    """基本描述
    二郎神AI摄像头(AI-Lens)
    """

    def __init__(self):
        self.recursion_depth = 0
        self.__Data_buff = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.__Temp_Data_buff = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        i2c.init()
        sleep(5000)
        try:
            i2c.read(Camera_Add, 1)
        except:
            display.scroll("Init AILens Error!")

    def switch_function(self, func):
        """基本描述
        选择摄像头功能
        Args:
            :param func: 选择功能号
        """
        i2c.write(Camera_Add, bytearray([0x20, func]))

    def get_image(self):
        """基本描述
        获取一帧画面
        :return: 当前画面数据
        """
        self.__Temp_Data_buff = i2c.read(Camera_Add, 9)
        print(self.__Temp_Data_buff)
        if self.__Temp_Data_buff == self.__Data_buff:
            sleep(100)
            if self.recursion_depth < 5:
                self.recursion_depth = self.recursion_depth + 1
                self.get_image()
            
        else:
            self.__Data_buff = self.__Temp_Data_buff
        

    def get_ball_color(self):
        """基本描述
        检测画面中的小球颜色
        :return: 颜色
        """
        if self.__Data_buff[0] == 7:
            if self.__Data_buff[1] == 1:
                return "Blue"
            elif self.__Data_buff[1] == 2:
                return "Red"
        else:
            return "No Ball"

    def get_ball_data(self):
        """基本描述
        返回画面中小球的信息
        :return: BallData [x,y,w,h,confidence,total,order]
        """
        BallData = []
        for i in range(7):
            BallData.append(self.__Data_buff[i + 2])
        return BallData

    def get_face(self):
        """基本描述
        判断画面中是否存在人脸
        :return:
        """
        return self.__Data_buff[0] == 6

    def get_face_data(self):
        """基本描述
        返回画面中人脸的信息
        :return: FaceData [x,y,w,h,confidence,total,order]
        """
        FaceData = []
        for i in range(7):
            FaceData.append(self.__Data_buff[i + 2])
        return FaceData

    def get_card_content(self):
        """基本描述
        返回卡片内容
        :return: 卡片内容
        """
        if self.__Data_buff[0] == 2:
            return numberCards[self.__Data_buff[1] - 1]
        elif self.__Data_buff[0] == 4:
            return letterCards[self.__Data_buff[1] - 1]
        elif self.__Data_buff[0] == 3 and self.__Data_buff[1] < 21:
            return otherCards[self.__Data_buff[1] - 1]
        else:
            return "No Card"

    def get_card_data(self):
        """基本描述
        返回画面中卡片的信息
        :return: CardData [x,y,w,h,confidence,total,order]
        """
        CardData = []
        for i in range(7):
            CardData.append(self.__Data_buff[i + 2])
        return CardData

    def get_color_type(self):
        """基本描述
        返回卡片颜色
        :return: 颜色
        """
        if self.__Data_buff[0] == 9:
            return colorList[self.__Data_buff[1] - 1]
        else:
            return "No Color"

    def get_color_data(self):
        """基本描述
        返回画面中颜色的信息
        :return: ColorData [x,y,w,h,confidence,total,order]
        """
        ColorData = []
        for i in range(7):
            ColorData.append(self.__Data_buff[i + 2])
        return ColorData

    def get_track_data(self):
        """基本描述
        返回画面中线段的信息
        :return: LineData [angel,width,len]
        """
        LineData = []
        for i in range(3):
            LineData.append(self.__Data_buff[i + 1])
        return LineData

    def learn_object(self, learn_id):
        """基本描述
        以ID号来学习一个物品
        :param learn_id: 要学习的ID号
        """
        if learn_id > 5 or learn_id < 1:
            print("Learn id out of range")
        else:
            i2c.write(Camera_Add, bytearray([10, learn_id]))

    def get_learn_data(self):
        """基本描述
        返回画面中已学习物品的信息
        :return: LearnData [ID,confidence]
        """
        LearnData = [self.__Data_buff[1], 100 - self.__Data_buff[2]]
        return LearnData


if __name__ == '__main__':
    ai = AILENS()
    ai.switch_function(Card)
    while 1:
        ai.get_image()
    while 0:
        ai.get_image()
        print(ai.get_ball_color())
        print(ai.get_ball_data())
    while 0:
        ai.get_image()
        print(ai.get_face)
        print(ai.get_face_data())
    while 0:
        ai.get_image()
        print(ai.get_card_content())
        print(ai.get_card_data())
    while 0:
        ai.get_image()
        print(ai.get_color_type())
        print(ai.get_color_data())
    while 0:
        ai.get_image()
        print(ai.get_track_data())
    while 0:
        ai.get_image()
        if button_a.is_pressed():
            ai.learn_object(1)
        print(ai.get_learn_data())
