# Необходимо реализовать модуль divisor_master. Все функции модуля принимают на вход натуральные числа от 1 до 1000.
# Модуль содержит функции:
# 1) проверка числа на простоту (простые числа - это те числа у которых делители единица и они сами);
import random
def IsPrimeNumber(number):
   divisor = 2
   # while number > 0:
      # divisor += 1
       if number % divisor != 0:
           print('дошли до цифры ', divisor, ' - оно НЕ является  первым делителем ')
           divisor += 1
           if number % divisor == 0:
               print('Число ', divisor, ' -  - оно является  первым делителем ')
       else: ('Число ', number, ' - НЕпростое, т.к. не имеет делитель'  , divisor, 'кроме еденицы и самого себя ')
   # return divisor == number , print('перебрали все цифры до первого делителя ', divisor, 'не нашлось ни одного делителя' )

   # divisor = 2
   # while number % divisor!= 0:
   #     divisor += 1
   #     if number % divisor == 0:
   #         print('дошли до цифры ', divisor, ' - оно является  первым делителем ')
   #         if number == 1 or number==divisor:
   #             print('Число ', number, ' - простое, т.к. не имеет делителей , кроме еденицы и самого себя ')
   #     else: ('Число ', number, ' - НЕпростое, т.к. не имеет делитель'  , divisor, 'кроме еденицы и самого себя ')
   # return divisor == number , print('перебрали все цифры до ', number, 'не нашлось ни одного делителя' )
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