class RoboticManipulator:
    def __init__(self, name):
        self.name = name
        self.position = [0, 0, 0]  # x, y, z координаты манипулятора

    def __str__(self):
        return f"{self.name} at position {self.position}"

    def __add__(self, other):
        if isinstance(other, list) and len(other) == 3:
            self.position = [self.position[i] + other[i] for i in range(3)]
            return self
        else:
            return NotImplemented


class ServoDrive:
    def __init__(self, name, angle=0):
        self.name = name
        self.angle = angle

    def __str__(self):
        return f"{self.name} at angle {self.angle}"

    def __add__(self, degree):
        if isinstance(degree, (int, float)):
            self.angle += degree
            return self
        else:
            return NotImplemented


# Пример использования
if __name__ == "__main__":
    manipulator = RoboticManipulator("Six-Axis Robotic Manipulator")
    servo1 = ServoDrive("Servo1")
    servo2 = ServoDrive("Servo2")

    print(manipulator)
    print(servo1)
    print(servo2)

    manipulator + [10, 20, 30]  # перемещение манипулятора на вектор [10, 20, 30]
    print(manipulator)

    servo1 + 45  # поворот первого сервопривода на 45 градусов
    print(servo1)