# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
# 10 -> 1 2 4 8

n = int(input())
r = 1
numberInPower = 2 
while numberInPower ** r < n :
    print(numberInPower ** r)
    r += 1