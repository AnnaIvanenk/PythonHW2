# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть
# 5 -> 1 0 1 1 0
# 2

monets = int(input())
count = 0
eagle = 0
tails = 0
for i in range(monets) :
    mas = int (input())
    if mas == 0 :
        eagle += 1 
    elif mas == 1 :
        tails += 1
if eagle > tails :
    print (tails)
else:
    print (eagle)
