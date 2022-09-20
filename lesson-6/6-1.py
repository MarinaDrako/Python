from time import sleep


class TrafficLight:
    __tr_dict = {'красный': 7, 'желтый': 2, 'зелёный': 6}
    __color = ''

    def running(self):
        n = 0
        while n < 4:
            for color, tr_time in self.__tr_dict.items():
                self.__color = color
                print(f"Светофор в режиме: '{self.__color}' в течение {tr_time} секунд")
                sleep(tr_time)
            n += 1


t1 = TrafficLight()
t1.running()
