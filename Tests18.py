# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
#  В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5

from random import randint
N = int(input('Введите количество элементов в массиве: '))
A = []

for i in range(N):
    A.append(randint(1, 10))
print(A)

x = int(input('Введите число до 10: '))

mi = 0
B = min (A)
B1 = B
ma = 0
C = max(A)
C1 = C
for i in range(len(A)):
    if x >= A[i]:
        B = A[i]
    else:
        C = A[i]
    print(B, C)
    if B1 <= B:
        B1 = B
    if C1 >= C:
        C1 = C
mi = x-B1
ma = C1-x
if mi > ma:
    print("Ближайшее",C1 )
else:
    print("Ближайшее", B1)
