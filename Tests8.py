# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# *Пример:*
# 3 2 4 -> yes
# 3 2 1 -> no

n = int(input('Введите количество долек шоколодки n: '))
m = int(input('Введите количество долек шоколодки m: '))
k = int(input('Введите сколько нужно отломить долек : '))
l = n*m

if k < l:
    if k % n == 0 or k % m == 0:
        print("Да")
    else:
        print("Нет")
else:
    print("Неверное количество долек")
