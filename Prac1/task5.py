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


