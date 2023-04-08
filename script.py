#!/usr/bin/python3
#Output Kaprekar num from 4digit

getnum = input()[:4]
print("ВВЕДЕНО ЧИСЛО: " + getnum)

#получаем квадратный корень из введенного числа
sqrt = int(getnum) ** (0.5)
print("квадратный корень: " + str(int(sqrt)))

#складываем 2 числа полученных из введенного числа
s = int(getnum[:2]) + int(getnum[2:])
print("Сумма чисел: " + str(s))

#проверка условия соответствия числу Капрекара
if (int(sqrt) == s):
    print("Число капрекара найдено: " + str(int(sqrt)))
else:
    print("У числа " + str(getnum) + " число Капрекара не найдено")