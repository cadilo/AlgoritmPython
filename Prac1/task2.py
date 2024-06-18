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
