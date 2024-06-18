import math
from dataclasses import dataclass, field

@dataclass()
class Sphere:
    def __init__(self, latitude, longitude):
        self.latitude = math.radians(latitude)  # Переводим градусы в радианы
        self.longitude = math.radians(longitude)  # Переводим градусы в радианы


@dataclass(order=True)
class Point(Sphere):
    latitude1: float
    longitude1: float
    latitude2: float
    longitude2: float

    def __post_init__(self):
        super().__init__(self.latitude1, self.longitude1)
        self.point2 = Sphere(self.latitude2, self.longitude2)

    def calculate_distance(self):
        delta_longitude = self.point2.longitude - self.longitude
        central_angle = math.acos(math.sin(self.latitude) * math.sin(self.point2.latitude) +
                                  math.cos(self.latitude) * math.cos(self.point2.latitude) * math.cos(delta_longitude))
        distance = central_angle  # Расстояние на сфере (в радианах)
        return math.degrees(distance) * 60  # Преобразуем в морские мили (1 морская миля ≈ 1 минута широты)


if __name__ == '__main__':
    point1 = Point(56.2291, 58.0104, 48.8566, 2.3522)
    point2 = Point(143.234, 13.0234, 34.8593, 2.2312)

    distance1 = point1.calculate_distance()
    distance2 = point2.calculate_distance()

    print(f"Расстояние между первыми точками: {distance1} морских миль")
    print(f"Расстояние между вторыми точками: {distance2} морских миль")

    print(point1 < point2)