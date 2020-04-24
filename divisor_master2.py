# Необходимо реализовать модуль divisor_master. Все функции модуля принимают на вход натуральные числа от 1 до 1000.
import random
spisok_list=list(range(1,1001))
print(type(spisok_list),spisok_list)
x=random.choice(spisok_list)
# x = random.randrange(1, 1001, 1)
print('Проверяемое чило из списка:', x)
x=113
print('Проверяемое чило из списка:', x)
# 1) проверка числа на простоту (простые числа - это те числа у которых делители единица и они сами);


