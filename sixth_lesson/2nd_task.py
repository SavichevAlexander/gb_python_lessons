# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

import random

mas = [random.randint(-50, 50) for i in range(random.randint(10,20))]
print("Array elements: ")
print(*mas)
maxi = int(input("max = "))
mini = int(input("min = "))
masi = []
if maxi >= mini:
   for i in range(len(mas)):
      if maxi >= mas[i] and mini <= mas[i]:
          masi.append(i)
   print("Quantity:", len(masi))
   print("Indices:", masi)
