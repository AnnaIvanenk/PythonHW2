# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. 
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.
# 4 4 -> 2 2
# 5 6 -> 2

s = int(input())
p = int(input())
x = 1
y = 1 

while x != 1001 :
    x += 1
    while y != 1001 :
        y += 1
        if ((s == x + y) and (p == x*y)) :
           print (x, y)