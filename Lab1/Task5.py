import math


class Sphere:
    def __init__(self, latitude, longitude):
        self.latitude = math.radians(latitude)  # Переводим градусы в радианы
        self.longitude = math.radians(longitude)  # Переводим градусы в радианы


class Point(Sphere):
    def __init__(self, latitude1, longitude1, latitude2, longitude2):
        super().__init__(latitude1, longitude1)
        self.point2 = Sphere(latitude2, longitude2)

    def calculate_distance(self):
        delta_longitude = self.point2.longitude - self.longitude
        central_angle = math.acos(math.sin(self.latitude) * math.sin(self.point2.latitude) +
                                  math.cos(self.latitude) * math.cos(self.point2.latitude) * math.cos(delta_longitude))
        distance = central_angle  # Расстояние на сфере (в радианах)
        return math.degrees(distance) * 60  # Преобразуем в морские мили (1 морская миля ≈ 1 минута широты)


if __name__ == '__main__':
    point = Point(56.2291, 58.0104, 48.8566, 2.3522)
    distance = point.calculate_distance()

    print(f"Расстояние между точками: {distance} морских миль")