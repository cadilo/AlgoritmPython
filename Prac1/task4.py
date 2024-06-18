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

