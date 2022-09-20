class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = bool(is_police)

    def go(self):
        return f'{self.name} поехал'

    def stop(self):
        return f'{self.name} остановился'

    def turn_right(self):
        return f'{self.name} повернул направо'

    def turn_left(self):
        return f'{self.name} повернул налево'

    def show_speed(self):
        return f'Текущая скорость автомобиля {self.name} - {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость автомобиля {self.name} - {self.speed}')
        if self.speed > 60:
            print(f'Превышение скорости!')


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость автомобиля {self.name} - {self.speed}')
        if self.speed > 40:
            print(f'Превышение скорости!')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        self.is_police = True


t1 = TownCar(80, 'чёрный', 'Audi', False)
t2 = TownCar(60, 'серебристый', 'Mitsubishi', False)
s1 = SportCar(100, 'красный', 'McLaren', False)
s2 = SportCar(50, 'зелёный', 'Mersedes', False)
w1 = WorkCar(10, 'серый', 'Погрузчик', False)
w2 = WorkCar(45, 'жёлтый', 'Экскаватор', False)
p1 = PoliceCar(110, 'голубой', 'Ford', True)
p2 = PoliceCar(50, 'белый', 'Lada', True)

print(t1.name, t1.color, t1.is_police)
print(t1.go(), t1.turn_left())
t1.show_speed()
print(t2.color, t2.name, t2.speed)
print(t2.turn_right())
print(t2.show_speed())
print(s1.color, s1.name, t1.is_police)
print(s2.go(), s2.show_speed(), s2.stop())
print(f'{w1.color} {w1.go()}, на перекрёстке {w1.turn_right()}')
print(w2.show_speed())
print(f'{p1.name} - это полицейская машина? {p1.is_police}. {t1.show_speed()}, он гонится за преступником.')
print(p2.go())
