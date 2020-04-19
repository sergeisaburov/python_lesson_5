# Необходимо реализовать модуль divisor_master. Все функции модуля принимают на вход натуральные числа от 1 до 1000.
spisok_1000 = list(range (1, 1001)) # создаем список от 1 до 1000
print ('создаем список от 1 до 1000:',type(spisok_1000),spisok_1000)
import random
proveryaemoe_number=random.randrange(1, 1001, 1)
print("Генерация случайного числа от 1 до 1000:", random.randrange(1, 1001, 1))# Генерация случайного числа в пределах заданного промежутке от 1 до 1000 с шагом 1
print("Проверяемое число:", proveryaemoe_number)# Генерация случайного числа в пределах заданного промежутке от 1 до 1000 с шагом 1
# 1) проверка числа на простоту (простые числа - это те числа у которых делители единица и они сами);
# def IsPrime(n):
#    d = 2
#    print('Пока', n , '/', d, 'перебираем:')
#    while n % d != 0:
#        print( n, '/',d,' есть остаток, поэтому +1')
#        d += 1
#        print('прибавим +1 ', n, '/',d)
#    return d == n
#
# n=proveryaemoe_number
# IsPrime(n)
#print('разделилось без остатка', n, '/',d)

def proverka_na_prost(x):
    print('Проверка на простое число')
    d=2
    while x % d != 0 :
        d+=1
        return d==x

proverka_na_prost(proveryaemoe_number)