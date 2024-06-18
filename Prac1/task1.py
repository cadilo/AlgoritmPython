import random

num = []

for i in range(0, 10):
    num.append(random.randint(1,10))

print(num)
num.reverse()
print(num)
