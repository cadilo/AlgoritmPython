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