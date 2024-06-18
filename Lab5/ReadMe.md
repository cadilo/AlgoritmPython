# Практика 1
## Задание 1

Сгенерировать, используя модуль псевдослучайных чисел `random`, или ввести с клавиатуры список целых чисел. Вывести в консоль, затем перевернуть его и снова вывести в консоль.

```python
import random

num = []

for i in range(0, 10):
    num.append(random.randint(1,10))

print(num)
num.reverse()
print(num)
```

## Задание 2

Сгенерировать, используя модуль псевдослучайных чисел `random`, или ввести с клавиатуры два списка целых чисел. Вывести их в консоль. Создать новый пустой список. Добавить в него все четные (по индексу) элементы первого списка и все нечетные (по индексу) элементы второго списка. Вывести третий список в консоль.

```python
import random

list1 = []
list2 = []
list3 = []

for i in range(0, 10):
    list1.append(random.randint(1,10))
    list2.append(random.randint(1, 10))

print("Список 1: ", list1)
print("Список 2: ", list2)

for i in range(0, len(list1)):
    if list1[i]%2 == 0:
        list3.append(list1[i])


for i in range(0, len(list2)):
    if list2[i]%2 != 0:
        list3.append(list2[i])

print("Список 3: ", list3)
```

## Задание 3

Сгенерировать, используя модуль псевдослучайных чисел `random`, или ввести с клавиатуры список произвольных элементов (целые числа, числа с плавающей точкой, строки). Вывести в консоль. Убрать из него все дубликаты через приведение типов. Вывести в консоль.

```python
import random


mass_str = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
list1 = []
list2 = []
list3 = []
list_2d = []

for i in range(0, 100):
    list1.append(random.randint(1,100))

for i in range(0, 100):
    list2.append(random.uniform(10.5, 25.5))

list_2d.append(list1)
list_2d.append(list2)
list_2d.append(mass_str)

for i in range(0, 210):
    list3.append(random.choice(random.choice(list_2d)))

print(list3)
ints_list1 = list(set(list3))
print(ints_list1)
```
## Задание 4

Сгенерировать, используя модуль псевдослучайных чисел `random`, или ввести с клавиатуры словарь, где ключом является строка, значением — целое число или число с плавающей точкой. Вывести в консоль. Для всех уникальных значений создать кортеж, где первым элементом будет значение, вторым — список связанных с ним ключей. Собрать эти кортежи в список, вывести его в консоль.

```python
import random, string

dictionary = {}
tuple = ()
list_tuple = []
new_list_tuple = []


def randomword(length): #Функция для генерации строк
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for i in range(length))

for i in range(0, 20):
    dictionary[randomword(5)] = random.randint(1, 10)   #Заполнили словарь парами ключ-значение

print(dictionary)

for value in dictionary.values():       #Добавили в список все значения из словаря
    list_tuple.append(value)

ints_list1 = list(set(list_tuple))      # Убрали дубликаты

for value in range(0, len(ints_list1)):

    list_key = []
    for keys in dictionary.keys():
        if ints_list1[value] == dictionary.get(keys):
            list_key.append(keys)
            tuple = (ints_list1[value], list_key)

    new_list_tuple.append(tuple)


print(new_list_tuple)
```

## Задание 5

Сгенерировать, используя модуль псевдослучайных чисел `random`, или ввести с клавиатуры два словаря, где ключом является строка, значением — целое число или число с плавающей точкой. Вывести в консоль. Найти пересечения множеств значений словарей. Создать новый словарь, содержащий только те пары ключ-значение, значения из которых входит в пересечение. Вывести в консоль.


```python
import random, string

dictionary1 = {}
dictionary2 = {}
dictionary3 = {}
flag = False

def randomword(length): #Функция для генерации строк
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for i in range(length))

for i in range(0, 10):
    dictionary1[randomword(5)] = random.randint(1, 10)   #Заполнили словарь 1 парами ключ-значение
    dictionary2[randomword(5)] = random.randint(1, 10)   #Заполнили словарь 2 парами ключ-значение

print("Словарь 1: ", dictionary1)
print("Словарь 2: ", dictionary2)

for key1, value1 in dictionary1.items():
    flag = False
    for key2, value2 in dictionary2.items():
        if value1 == value2:
            flag = True
            # Добавляем в 3 словарь, пару из 2 словаря
            dictionary3.update({key2: value2})


    if flag == True:
        #Добавляем в 3 словарь, пару из 1 словаря
        dictionary3.update({key1: value1})

print("Словарь 3: ", dictionary3)
```


# Практика 2

## Задание 1

Скопировать из Википедии данные по кодам аэропортов (например, отсюда [https://en.wikipedia.org/wiki/List_of_airports_by_IATA_airport_code:\_P](https://en.wikipedia.org/wiki/List_of_airports_by_IATA_airport_code:_P)). Сохранить их в JSON-подобном формате с использованием словарей. Реализовать функцию получения кода по названию аэропорта. Реализовать и русское, и английское название. Предусмотреть, что аэропорта может не существовать.

```python 
#import pandas as pd
from langdetect import detect
import json

# df = pd.read_html('https://en.wikipedia.org/wiki/List_of_airports_by_IATA_airport_code:_P')
#
# # Удаляем лишние столбцы
# df[0].drop([('Location\xa0served', '-PA-')], axis=1, inplace=True)
# df[0].drop([('Time', '-PA-')], axis=1, inplace=True)
# df[0].drop([('DST', '-PA-')], axis=1, inplace=True)
#
# # Удаляем ссылки
# df[0].replace({'\[[0-9]+\]': ''}, regex=True, inplace=True)
#
# # Упаковываем в json
# df[0].to_json("package.json")

str = input()
lang = detect(str)

with open('package.json', encoding='utf-8') as f:
    templates = json.load(f)

def get_key(templates, value):
    for k, v in templates.items():
            if v == value:
                # print("Есть совпадение")
                return k

def main():
    if lang == "ru":
        result = get_key(templates["Airport_name_RUS"], str)
        if result is None:
            print("Такого аэропорта нет")
    else:
        result = get_key(templates["Airport_name_EN"], str)
        if result is None:
            print("Такого аэропорта нет")


    if result is not None:
        print("Код этого аэропорта по IATA: ", templates["IATA"].get(result))
        print("Код этого аэропорта по ICAO: ", templates["ICAO"].get(result))

if __name__ == '__main__':
    main()

```

## Задание 2

Реализовать в консоли таск-трекер. Данные хранить в словаре во время работы программы, выгружать список задач в JSON-файл, при запуске загружать файл (используя модуль `json`). Реализовать возможность ввода произвольной строки с описанием задачи, возможность отметки задания выполненным, возможность ввода произвольных категорий. *Бонус: поиск по задачам; вывод всех задач в категории.*
```
- [x] Задание выполнено #pstu
- [ ] Еще задача #work
- [ ] И еще задача #pstu
```

```python
import json

with open('Tasks.json', 'r', encoding='utf-8') as json_file:
    data_load = json.load(json_file)


def add_task(name_task, tag_task):
    data = {"status": "[ ]", "name": name_task, "tags": tag_task}
    data_load['tasks'].append(data)

    with open('Tasks.json', 'w', encoding='utf-8') as outfile:
        json.dump(data_load, outfile, ensure_ascii=False, indent=2)

    print("Задача", name_task, "добавлена")


def delete_task(name_task):
    index_dict = 0
    for i in data_load['tasks']:
        if i['name'] == name_task:
            del data_load['tasks'][index_dict]
        index_dict += 1

    with open('Tasks.json', 'w', encoding='utf-8') as outfile:
        json.dump(data_load, outfile, ensure_ascii=False, indent=2)


def view_all_task(templates):
    for i in templates['tasks']:
        print(i['status'], i['name'], i['tags'])


def change_task(name_task):
    for i in data_load['tasks']:
        if name_task == i['name']:
            print(i['status'], i['name'], i['tags'])
            command = input('Введите название изменяемоного объекта(status, name, tag): ')
            match command:
                case 'status':
                    i['status'] = '[x]'
                    print('Статус задачи изменен')

                case 'name':
                    new_name = input('Введите новое название задачи: ')
                    i['name'] = new_name

                case 'tag':
                    new_tag = input('Введите новое название категории')
                    i['tags'] = new_tag
    with open('Tasks.json', 'w', encoding='utf-8') as outfile:
        json.dump(data_load, outfile, ensure_ascii=False, indent=2)


def view_task(name_task):
    for i in data_load['tasks']:
        if name_task == i['name']:
            print(i['status'], i['name'], i['tags'])
            break


def view_tag_task(name_tag):
    flag = False
    for i in data_load['tasks']:
        if name_tag == i['tags']:
            flag = True
            print(i['status'], i['name'], i['tags'])

    if flag == False: print('Задач с такой категорией нет')


def main():
    with open('Tasks.json', encoding='utf-8') as f:
        templates = json.load(f)
    while True:
        command = input('Enter command: ')
        match command:
            case "help":
                print('''
                        help                                - вывод всех команд
                        add_task                            - добавление задачи
                        delete_task                         - удаление задачи по названию
                        change_task                         - изменение задачи по названию
                        view_all_task                       - вывод всех имеющихся задач
                        view_task                           - вывод задачи по названию
                        view_tag_task                       - вывод всех задач в категории
                        exit                                - выйти из приложения
                ''')

            case "add_task":
                name_task = input('Введите название задачи: ')
                tag_task = input('Введите категорию задачи: ')
                add_task(name_task, tag_task)

            case "delete_task":
                name_delete_task = input("Введите название задачи: ")
                delete_task(name_delete_task)

            case "change_task":
                name_change_task = input("Введите название изменяемой задачи: ")
                change_task(name_change_task)

            case "view_all_task":
                view_all_task(templates)

            case "view_task":
                name_view_task = input("Введите название задачи: ")
                view_task(name_view_task)

            case "view_tag_task":
                name_view_tag = input("Введите название категории: ")
                view_tag_task(name_view_tag)

            case "exit":
                break

            case _:
                print("Такой команды нет")


if __name__ == '__main__':
    main()
```
## Задание 3

Реализовать в консоли трекер бюджета. Данные хранить в словаре во время работы программы, выгружать список задач в JSON-файл, при запуске загружать файл (используя модуль `json`). Реализовать возможность ввода произвольной строки с описанием операции и суммой расхода/дохода, возможность ввода произвольных категорий. *Бонус: аналитика трат/доходов по категориям (например, сколько потратили в сумме за заказ еды); установка лимитов на категории.*


```python
import json

with open('budget.json', 'r', encoding='utf-8') as json_file:
    data_load = json.load(json_file)


def test():
    #tag_opr1 = input("Введите категорию 1: ")
    tag_opr2 = input("Введите категорию 2: ")
    #print(data_load["current"][0].setdefault("tag", tag_opr1))
    #print(data_load["current"][1].setdefault("tag", tag_opr2))
    for i in data_load["current"]:
        if i['tag'] == tag_opr2:
            print("True")
            break
        else:
            print("False")


def add_opr(name_opr, amount_opr, tag_opr, type_opr):
    data = {"name": name_opr, "amount": amount_opr, "tag": tag_opr, "type": type_opr}

    k = 0

    flag = False
    for i in data_load["current"]:
        if i['tag'] == tag_opr:
            print("True")
            flag = True
            if type_opr == "расход":
                k = int(i['current']) + int(amount_opr)

            elif type_opr == "доход":
                k = int(i['current']) - int(amount_opr)
            i['current'] = str(k)
            break
        else:
            flag = False

    if not flag:
        data_current = {"tag": tag_opr, "current": amount_opr}
        data_load['current'].append(data_current)

    flag_on_lim = False
    for i in data_load["limits"]:
        if tag_opr == i["tag"]:
            print("Найден предел на категорию")
            if k > int(i["limit"]):
                print("Превышен предел на категорию")
                flag_on_lim = True
            else:
                print("Предел на категорию не превышен")
                flag_on_lim = False
            break
        else:
            flag_on_lim = False
            print("Предел на категорию не найден")

    if flag_on_lim:
        print("Операция", name_opr, "не добавлена")
    else:
        data_load['operations'].append(data)
        with open('budget.json', 'w', encoding='utf-8') as outfile:
            json.dump(data_load, outfile, ensure_ascii=False, indent=2)
        print("Операция", name_opr, "добавлена")


def view_all_opr():
    for i in data_load['operations']:
        print(i['name'], i['amount'], i['tag'], i['type'])

def view_opr(name_opr):
    for i in data_load['operations']:
        if name_opr == i['name']:
            print(i['name'], i['amount'], i['tag'], i['type'])


def view_tag_opr(name_tag):
    flag = False
    for i in data_load['operations']:
        if name_tag == i['tag']:
            flag = True
            print(i['name'], i['amount'], i['tag'], i['type'])

    if flag == False: print('Операций с такой категорией нет')


def add_lim(tag_lim, amount_lim):
    data_limit = {"tag": tag_lim, "limit": amount_lim}
    data_load['limits'].append(data_limit)
    with open('budget.json', 'w', encoding='utf-8') as outfile:
        json.dump(data_load, outfile, ensure_ascii=False, indent=2)


def view_all_lim():
    for i in data_load['limits']:
        print(i['tag'], i['limit'])


def view_lim(name_lim):
    for i in data_load['limits']:
        if i['tag'] == name_lim:
            print(i['tag'], i['limit'])


def delete_lim(tag_lim):
    index_dict = 0
    for i in data_load['limits']:
        if i['tag'] == tag_lim:
            del data_load['limits'][index_dict]
        index_dict += 1
    with open('budget.json', 'w', encoding='utf-8') as outfile:
        json.dump(data_load, outfile, ensure_ascii=False, indent=2)


def change_lim(name_tag, new_lim):
    for i in data_load['limits']:
        if name_tag == i['tag']:
            i['limit'] = str(new_lim)
            print(i['tag'], i['limit'])

    with open('budget.json', 'w', encoding='utf-8') as outfile:
        json.dump(data_load, outfile, ensure_ascii=False, indent=2)


def view_all_cur():
    for i in data_load['current']:
        print(i['tag'], i['current'])


def view_cur(name_tag):
    for i in data_load['current']:
        if i['tag'] == name_tag:
            print(i['tag'], i['current'])


def main():
    while True:
        command = input('Enter command: ')
        match command:
            case "help":
                print('''
                        help                                - вывод всех команд
                        +limit                               - вкладка с лимитами
                        current                             - вкладка с тратами
                        +add_opr                             - добавление операции
                        view_all_opr                        - вывод всех имеющихся операций
                        view_opr                            - вывод операции по названию
                        view_amount                         - вывод всех операций с заданной суммой
                        view_tag_opr                        - вывод всех операций в категории
                        exit                                - выйти из приложения
                ''')

            case "add_opr":
                name_opr = input('Введите название операции: ')
                amount_opr = input('Введите сумму: ')
                tag_opt = input('Введите категорию операции: ')
                type_opr = input('Введите тип операции(доход/расход): ')
                add_opr(name_opr, amount_opr, tag_opt, type_opr)

            case "limit":
                command_limit = input('Enter command limit: ')

                match command_limit:
                    case "help":
                        print('''
                        help                - Вывод всех команд во вкладке limit
                        add_limit           - Добавить новый предел на категорию
                                            (Если такой категории нет, то предел все равно создастся)
                        delete_limit        - Удалить лимит по названию
                        change_limit        - Изменить лимит по названию
                        view_all_limits     - Вывести все пределы
                        view_limits         - Вывести предел по названию
                        
                        ''')
                    case "add_limit":
                        name_tag = input('Введите название категории: ')
                        amount_limit = input('Введите лимит на категорию: ')
                        add_lim(name_tag, amount_limit)
                    case "delete_limit":
                        tag_lim = input("Введите название категорию лимита: ")
                        delete_lim(tag_lim)
                    case "view_all_lim":
                        view_all_lim()
                    case "view_lim":
                        name_tag = input("Введите категорию лимита: ")
                        view_lim(name_tag)
                    case "change_lim":
                        name_tag = input("Введите категорию лимита: ")
                        new_lim = int(input("Введите новый лимит: "))
                        change_lim(name_tag, new_lim)

            case "current":
                command_current = input('Enter command current: ')

                match command_current:
                    case 'help':
                        print('''
                        help            - Вывод всех комманд во вкладке current
                        view_all_cur    - Вывод всех трат по категориям
                        view_cur        - Вывод трат по категории
                        ''')
                    case 'view_all_cur':
                        view_all_cur()
                    case 'view_cur':
                        name_tag = input('Введите название категории: ')
                        view_cur(name_tag)

            case "test":
                test()

            #case "current":

            case "view_all_opr":
                view_all_opr()

            case "view_opr":
                name_opr = input('Введите название операции: ')
                view_opr(name_opr)

            case "view_tag_opr":
                name_tag = input('Введите название категории: ')
                view_tag_opr(name_tag)

            case "exit":
                break

            case _:
                print("Такой команды нет")


if __name__ == '__main__':
    main()
```


# Практика 3

На основе классов из лабораторной работы №2 (основы ООП) создать набор классов данных, добившись паритета по функциональности — т.е. для, например, Сферы и Точки должен быть также доступен расчет расстояния.

```python 
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
```

# Лабораторная работа 1

## Задание 1

Реализовать структуру данных «очередь» (первый пришел, первый ушел) с помощью класса с возможностью просмотра, добавления и удаления элементов.

```python

class Queue():
    def __init__(self):
        self.queue = []

    def push(self, item):
        self.queue.append(item)

    def pop(self):
        if len(self.queue) == 0:
            return None
        removed = self.queue.pop(0)
        return removed



def main():
    q1 = Queue()
    q1.push(1)
    q1.push(23)
    q1.push(732)
    q1.push(34)
    #q1.pop()
    q1.push("str")
    q1.pop()
    print(q1.queue)


if __name__ == '__main__':
    main()
```

## Задание 2

Реализовать структуру данных «стек» (последний пришел, первый ушел) с помощью класса с возможностью просмотра, добавления и удаления элементов.

```python
class Stack:
    def __init__(self):
        self.stack = []
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        if len(self.stack) == 0:
            return None
        removed = self.stack.pop()
        return removed


def main():
    s1 = Stack()
    s1.push(1)
    s1.push(2)
    s1.push(3)
    s1.pop()
    print(s1.stack)

if __name__ == '__main__':
    main()
```

## Задание 3

Реализовать иерархию классов, описывающих разные виды объектов одного типа (например, сервоприводов (синхронный/асинхронный/линейный и т.п.). Реализовать минимум 3 уровня иерархии. Реализовать возможность задания характеристик (например, для двигателя это угол поворота, скорость вращения, ускорение и т.п.). Реализовать строковое представление классов «магическими» методами `__str__()` и `__repr__()`, быть готовым пояснить различия этих методов. Перегрузить условные операторы (см. магические методы `__eq__()`, `__ne__()`, `__lt__()`, `__gt__()`, `__le__()`, `__ge__()`) для реализации возможности сравнения экземпляров класса.

```python
class Human:
    def __init__(self, Name, Age):
        self.Name = Name
        self.Age = Age

    def __str__(self):
        return f"Class Name: {self.__class__}, Name Human: {self.Name}, Age Human: {self.Age}"

    def __repr__(self):
        return f"{self.__class__}, {self.Name}, {self.Age}"

    def show_name(self):
        print(self.Name)


class Gender(Human):
    def __init__(self, Name, Age, Gender):
        super().__init__(Name, Age)
        self.Gender = Gender

    def __eq__(self, other):
        if self.Gender == other.Gender:
            return True
        else:
            return False

    def __ne__(self, other):
        if self.Gender != other.Gender:
            return True
        else:
            return False


class Student(Gender):
    def __init__(self, Name, Age, Gender, StudentId):
            super().__init__(Name, Age, Gender)
            self.StudentId = StudentId


m1 = Student("Mikle", 20, "Man", 1)
m2 = Student("Jeny", 30, "Woman", 2)

if m1 == m2:
    print("Гендеры равны")
elif m1 != m2:
    print("Гендеры не равны")

```

## Задание 4

Реализовать упрощенную модель некоего объекта (например, шестизвенного манипулятора с сервоприводами) при помощи иерархии классов. Реализовать функции объекта (например, перемещение манипулятора в пространстве) через перегрузку арифметических операторов (`__add__()` и т.д.).

```python
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
```

## Задание 5

 Расчет расстояния между точками на сфере по их широте и долготе (взять любые GPS-координаты) при помощи иерархии классов: как минимум, Точка и Сфера (к ней относятся Точки). https://en.wikipedia.org/wiki/Haversine_formula
 
```python
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
```

# Лабораторная работа 3

## Блок 1

1. Загрузите список стран из `countries.json`
2. С помощью `map()` создайте новый список, изменив сделав название каждой страны прописным в списке стран.
3. С помощью `filter()`, чтобы отфильтровать страны, содержащие `'land'`.
4. С помощью `filter()`, чтобы отфильтровать страны, содержащие ровно шесть символов.
5. С помощью `filter()`, чтобы отфильтровать страны, содержащие шесть и более букв в списке стран.
6. С помощью `filter()` для отсеивания стран, начинающихся с буквы `'E'`.
7. С помощью `reduce()` объедините все страны и получите данное предложение на английском языке: Финляндия, Швеция, Дания, Норвегия и Исландия являются странами Северной Европы.
8. Решите предыдущие задачи, объединив две или более функций высшего порядка методов
9. Используя сначала каррирование, а затем замыкания, объявите функцию `categorize_countries()`, которая возвращает список стран с некоторым общим шаблоном (например, `'land', 'ia', 'island', 'stan'`), который можно менять.
10. Используя файл `countries-data.json`, выполните приведенные ниже задания в функциональной парадигме:
    1. Отсортировать страны:
        1. по названию, 
        2. по столице, 
        3. по численности населения
    2. Выявить произвольное число (начать с 10) наиболее распространенных языков и где их используют.
    3. Выявить произвольное число (начать с 10) наиболее населенных стран.

## Блок 2

1. Сгенерировать список из 50 числовых элементов. Используя списковые включения, вычислить 4, 5 и 6 степени каждого элемента.
2. Сгенерировать матрицу в виде списка списков (например, `[ [1, 2], [3, 4], [5, 6], [7, 8], [1, 2], [3, 4], [5, 6], [7,8] ]`). Используя списковые включения, транспонировать матрицу ([https://ru.wikipedia.org/wiki/Транспонированная_матрица)](https://ru.wikipedia.org/wiki/%D0%A2%D1%80%D0%B0%D0%BD%D1%81%D0%BF%D0%BE%D0%BD%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%BD%D0%B0%D1%8F_%D0%BC%D0%B0%D1%82%D1%80%D0%B8%D1%86%D0%B0))
3. Взять полный диапазон числовых элементов от -9999 до 9999. Используя анонимную функцию и функцию `filter()`, вывести список, содержащий все элементы, которые без остатка делятся на 36.
4. Используя `map()` и анонимные функции (а также любые вспомогательные методы `str`), написать функцию редактирования заголовков в англоязычном стиле (`Каждое Слово Длиной Более 3 Букв Должно Быть с Большой Буквы`), принимающую на вход исходную строку, возвращающую отредактированную строку.
5. Используя иерархию классов из лаб. работы № 1, встроенные коллекции, анонимные функции и `reduce()`, вернуть максимальную длину, на которую может вытянуться шестизвенный манипулятор. Классы в иерархии можно расширять при необходимости.
6. Используя частичное выполнение функции, заменить указанную функцию с 4 аргументами на функцию с 1 аргументом так, чтобы результат был равен:
    1. 60
    2. 120
    3. 180

```python
def foo(a:int, b:int, c:int, d:int) -> int:
    return a*4 + b*3 + c*2 + d
```

7. Используя 2 генератора и `sum()`, вернуть сумму квадратов первых 10, 20, 30, 40 и 50 чисел Фибоначчи.
8. Написать генератор, последовательно возвращающий **все** аэропорты из списка IATA. Каждый аэропорты должен быть выведен в виде словаря, где ключами являются параметры из списка на Википедии (например, заголовки колонок таблицы здесь [https://en.wikipedia.org/wiki/List_of_airports_by_IATA_airport_code:\_A)](https://en.wikipedia.org/wiki/List_of_airports_by_IATA_airport_code:_A)) значениями — данные самого аэропорта.
9. Используя генератор из п. 8, сохранить в текстовый файл список IATA-кодов аэропортов и их англоязычные названия, разделенные табуляцией (`\t`).


```python
import json
from functools import reduce
from functools import partial
#====== Блок 1 ======

def block1():
    with open('countries.json', 'r', encoding='utf-8') as file:
        data_load = json.load(file)

    # list_upper = map(lambda x: x.upper(), data_load)
    #
    # print(list(list_upper))

    #list_two = list(filter(lambda x: x.find('land') != -1, data_load))
    # print(list_two)

    #list_tree = list(filter(lambda x: len(x) == 6, data_load))
    #print(list_tree)

    #list_four = list(filter(lambda x: x[0] != 'E', data_load))
    #print(list_four)

    #NorthCountry = ['Финляндия', 'Швеция', 'Дания', 'Норвегия', 'Исландия']
    #print(reduce(lambda x, y: x + ", " + y, NorthCountry) + " являются странами Северной Европы.")

    #print(list(filter(lambda x: "land" in x, list(map(lambda x: x.lower(), data_load)))))

    # def categorize_countries(sample):
    #     def print_countries(countries):
    #         return list(filter(lambda x: sample in x, countries))
    #
    #     return print_countries
    #
    #
    # print(categorize_countries("ia")(data_load))

    # with open("countries-data.json", "r", encoding="utf-8") as file:
    #     countries_data = json.load(file)
    #
    # sortedName = sorted(countries_data, key=lambda x: x['name'])
    # sortedCapital = sorted(countries_data, key=lambda x: x['capital'])
    # sortedPopulation = sorted(countries_data, key=lambda x: x['population'])
    #
    # all_languages = [language for country in countries_data for language in country['languages']]
    # language_count = [(language, all_languages.count(language)) for language in set(all_languages)]
    # topLanguages = sorted(language_count, key=lambda x: x[1], reverse=True)[:10]
    #
    # sorted_population_desc = sorted(countries_data, key=lambda x: x['population'], reverse=True)
    # top_populated_countries = sorted_population_desc[:10]


def block2():
    numbers = list(range(1, 51))
    power = [(x ** 4, x ** 5, x ** 6) for x in numbers]
    #print(power)

    matrix = [[1, 2], [3, 4], [5, 6], [7, 8], [1, 2], [3, 4], [5, 6], [7, 8]]
    transposed_matrix = [[x[i] for x in matrix] for i in range(len(matrix[0]))]
    #print(transposed_matrix)

    numbers = list(range(-9999, 9999))
    #print(list(filter(lambda x: x % 36 == 0, numbers)))

    def edit_title(title):
        words = title.split()
        filter__ = map(lambda word: word.capitalize() if len(word) > 3 else word.lower(), words)
        result = ' '.join(filter__)
        return result

    original_title = "каждое слово длиной БОЛЕЕ 3 букв должно БЫТЬ с БОЛЬШОЙ буквы"
    edited_title = edit_title(original_title)

    # print(edited_title)

    def foo(a: int, b: int, c: int, d: int) -> int:
        return a * 4 + b * 3 + c * 2 + d

    par3 = partial(foo, 2, 4, 20)

    #print(par3(0))
    #print(par3(60))
    #print(par3(120))

    fib = [0, 1]

    def fibonacci(n):
        while len(fib) < n:
            fib.append(fib[-1] + fib[-2])
        return fib[:n]

    def fibonacci_squared(n):
        fib = fibonacci(n)
        return (x**2 for x in fib)

    print(sum(fibonacci_squared(10)), sum(fibonacci_squared(20)), sum(fibonacci_squared(30)),
          sum(fibonacci_squared(40)),sum(fibonacci_squared(50)))

    def airports_generator(file_path):
        with open(file_path, 'r') as file:
            for line in file:
                data = eval(line)
                yield data

    file_path = "/Users/volod/PycharmProjects/Lab3_Yar/.venv/airport.txt"

    for airport in airports_generator(file_path):
        print(airport)

        


if __name__ == '__main__':
    block1()
    block2()
```

# Лабораторная работа 4


1. Предоставлен набор данных — наблюдения за погодой. Данные включают в себя время, описание, тип осадков, температуру, ощущаемую температуру, влажность, скорость ветра, направление ветра, видимость, давление.
2. Загрузить данные в DataFrame при помощи библиотеки `pandas`. Проследить за корректными `dtypes (df.info())`
3. Построить регрессионную модель, которая принимает на вход сведения о температуре и влажности, выдает ощущаемую температуру. Для этого использовать класс `LinearRegression` из `Scikit-learn`. При обучении модели использовать `train_test_split` из `Scikit-learn`
4. Необходимо визуализировать данные по каждой паре параметров и линию регрессии при помощи диаграммы рассеяния. Использовать `seaborn` при построении диаграмм (например, [https://seaborn.pydata.org/generated/seaborn.pairplot.html)](https://seaborn.pydata.org/generated/seaborn.pairplot.html))
5. Усложнить модель, добавив большее число параметров, например, параметр скорости ветра. На выходе по-прежнему дать ощущаемую температуру.
6. Собрать веб-интерфейс: вывести визуализацию модели, организовать пользовательский интерфейс при помощи HTML-форм. Пользователь вводит температуру, сведения о влажности и иные параметры модели, получает ощущаемую температуру. Можно брать любой фреймворк, например, Flask.


```python
from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.metrics import mean_squared_error

app = Flask(__name__)

@app.route('/')
def home():
    file_path = ('C:/Users/volod/PycharmProjects/Lab4_Yar/.venv/weatherHistory.csv')
    data = pd.read_csv(file_path)

    x = data[['Temperature (C)', 'Humidity', 'Wind Speed (km/h)']]
    y = data['Apparent Temperature (C)']
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

    model = linear_model.LinearRegression()
    model.fit(x_train, y_train)

    y_pred = model.predict(x_test)

    mse = mean_squared_error(y_test, y_pred)

    data_visual = x_test.copy()
    data_visual['Predicted Apparent Temperature (C)'] = y_pred

    plt.switch_backend('agg')
    sns.pairplot(data_visual, x_vars=['Temperature (C)', 'Humidity', 'Wind Speed (km/h)'],
                 y_vars=['Predicted Apparent Temperature (C)'], kind='reg', plot_kws={'line_kws': {'color': 'black'}})
    plt.savefig('static/output.png')

    return render_template('index.html', mse=mse)


@app.route('/predict', methods=['POST'])
def predict():
    file_path = "C:/Users/volod/PycharmProjects/Lab4_Yar/.venv/weatherHistory.csv"
    data = pd.read_csv(file_path)

    x = data[['Temperature (C)', 'Humidity', 'Wind Speed (km/h)']]
    y = data['Apparent Temperature (C)']
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

    model = linear_model.LinearRegression()
    model.fit(x_train, y_train)

    temperature = float(request.form.get('temperature'))
    humidity = float(request.form.get('humidity'))
    windspeed = float(request.form.get('windspeed'))

    prediction = model.predict([[temperature, humidity, windspeed]])

    return render_template('index.html', prediction=prediction)


if __name__ == '__main__':
    app.run(debug=True)
```

# Лабораторная работа 5

## Фигура А

![[Pasted image 20240618210611.png]]

```python
import bpy
import math

if __name__ == '__main__':
    mat = bpy.data.materials.get('Material')
    cubes = list()
    scene = bpy.context.scene
    frame_num = 0
    

    for i in range(-50, 50):
        bpy.ops.mesh.primitive_cube_add(size=0.1, location=(0, 0, i*.25))
        bpy.context.active_object.data.materials.append(mat)

        base = 15 - (i**2)*0.05
       
        bpy.ops.transform.resize(value=(base, base, 0.5))
        bpy.context.active_object.rotation_euler[2] = math.degrees(i*25)
        
        cubes.append(bpy.context.active_object)
        
    for cube in cubes:
        scene.frame_set(frame_num)
        cube.keyframe_insert(data_path="rotation_euler", index=-1)
        frame_num += 1
        scene.frame_set(frame_num)
        cube.rotation_euler[2] = 0
        cube.keyframe_insert(data_path="rotation_euler", index=-1)
```
## Фигура Б

![[Pasted image 20240618210725.png]]

```python
import bpy
import math

if __name__ == '__main__':
    mat = bpy.data.materials.get('Material')
    cubes = list()
    scene = bpy.context.scene
    frame_num = 0
    
    
    for i in range(-55, 55):
        bpy.ops.mesh.primitive_cube_add(size=0.1, location=(0, 0, i*.25))
        bpy.context.active_object.data.materials.append(mat)

        base = 150 - (i**2)*0.05
        
        bpy.ops.transform.resize(value=(base, base, 0.5))
        bpy.context.active_object.rotation_euler[2] = math.degrees(i*25)
        
        cubes.append(bpy.context.active_object)
        
    for cube in cubes:
        scene.frame_set(frame_num)
        cube.keyframe_insert(data_path="rotation_euler", index=-1)
        frame_num += 1
        scene.frame_set(frame_num)
        cube.rotation_euler[2] = 0
        cube.keyframe_insert(data_path="rotation_euler", index=-1)
```

## Фигура В
![[Pasted image 20240618210820.png]]
![[Pasted image 20240618210833.png]]

```python
import bpy
import math

if __name__ == '__main__':
    mat = bpy.data.materials.get('Material')
    cubes = list()
    scene = bpy.context.scene
    frame_num = 0
    
    for i in range(0, 51):
        bpy.ops.mesh.primitive_cube_add(size=0.1, location=(0, 0, i*.25))
        bpy.context.active_object.data.materials.append(mat)
        base = i + ( i**2)*0.05
        bpy.ops.transform.resize(value=(base, base, 0.5))
        bpy.context.active_object.rotation_euler[2] = math.degrees(i*25)
       
        cubes.append(bpy.context.active_object)
    for cube in cubes:
        scene.frame_set(frame_num)
        cube.keyframe_insert(data_path="rotation_euler", index=-1)
        frame_num += 1
        scene.frame_set(frame_num)
        cube.rotation_euler[2] = 0
        cube.keyframe_insert(data_path="rotation_euler", index=-1)
```