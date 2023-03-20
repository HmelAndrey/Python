"""

4. Реализуйте базовый класс Car.
у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
повернула (куда);
опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Вызовите методы и покажите результат.

"""


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f"Машина {self.name} поехала"

    def stop(self):
        return f"Машина {self.name} остановилась!"

    def turn_left(self):
        return f"Машина {self.name} повернула налево"

    def turn_right(self):
        return f"Машина {self.name} повернула направо"

    def show_speed(self):
        return f"Скорость машины {self.name}: {self.speed}"


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f"Скорость машины {self.name}: {self.speed}")

        if self.speed > 60:
            return f"Машина {self.name} нарушает скоростной режим!"


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f"Скорость  машины {self.name}: {self.speed}")
        if self.speed > 40:
            return f"Машина {self.name} нарушает скоростной режим!"


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def pol_car(self):
        if self.is_police:
            return f"Машина {self.name} полицейская"


town_car = TownCar(79, "Красный", "Hyundai", False)
sport_car = SportCar(150, "Синий", "Ferrari", False)
work_car = WorkCar(45, "Желтый", "ЗиЛ", False)
police_car = PoliceCar(59, "Белый", "Нива", True)

print(f"{town_car.go()}, цвет {town_car.name}: {town_car.color}, {town_car.turn_left()}, {town_car.stop()}")
print(f"{town_car.show_speed()}")

print(f"{police_car.go()}, {police_car.pol_car()}, цвет {police_car.name}: {police_car.color},"
      f"{police_car.turn_right()}, {town_car.stop()}")
