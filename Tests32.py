# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

from random import randint

l1 = [randint(1, 50) for i in range(10)]
print(l1)

minimum = int(input('Введите начало диапазона :'))
maximum = int(input('Введите конец диапазона :'))

for i in range(len(l1)):
    if minimum <= l1[i]<= maximum :
        print(i)
