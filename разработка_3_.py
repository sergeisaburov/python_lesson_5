# Необходимо реализовать модуль divisor_master. Все функции модуля принимают на вход натуральные числа от 1 до 1000.
# Модуль содержит функции:
# 1) проверка числа на простоту (простые числа - это те числа у которых делители единица и они сами);
import random
def IsPrimeNumber(number):
   divisor = 2
   while number % divisor!= 0:
       divisor += 1
   return divisor == number
# global sequence_num
# диапазон натуральных числе от 1 до 1000
sequence_num =list( range(1, 1001))
# проверка
# print(sequence_num)
# случайное число в диапазоне от 1 до 1000
# global x
x=random.choice(sequence_num)
print("число для анализа:",x)
print(IsPrimeNumber(x))

# 2) выводит список всех делителей числа;
def GetDiv(number):
    """Разложить число на множители"""
    #result = [1]
    listnum = []
    stepnum = 2
    while stepnum*stepnum <= number:
        if number % stepnum == 0:
            number//= stepnum
            listnum.append(stepnum)
        else:
            stepnum += 1
    if number > 1:
        listnum .append(number)
    return listnum
print (GetDiv(x))

# 3) выводит самый большой простой делитель числа.

def PrimeDiv(number):
    numlist = GetDiv(number)
    max = 0
    for index in numlist:
        if index > max:
            max = index
    return (max)
print(PrimeDiv(x))