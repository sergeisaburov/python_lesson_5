# Необходимо реализовать модуль divisor_master. Все функции модуля принимают на вход натуральные числа от 1 до 1000.
import random
spisok_list=list(range(1,1001))
print(type(spisok_list),spisok_list)
x=random.choice(spisok_list)
# x = random.randrange(1, 1001, 1)
print('Проверяемое чило из списка:', x)
# x=411
# print('Проверяемое чило из списка:', x)
# 1) проверка числа на простоту (простые числа - это те числа у которых делители единица и они сами);
def Proverka_na_prostoe(y):
    j=2
    if y % j == 0:
        print('перебор закончен ', y, '- число непростое, есть делитель:',j)
    else:
        while y % j != 0:
            j += 1
            if y % j == 0 and y != j:
                print('перебор закончен ', y, 'это число не простое, есть делитель:', j)
            elif y == j:
                print('перебор закончен до ', j, 'это число простое, делителей нет:')
        return j == y, print('у числа', y,' перебор закончен ')
Proverka_na_prostoe(x)
# 2) выводит список всех делителей числа;
def Vivod_vseh_del(y):
    global delitely
    delitely = []
   # print('Вывод всех делителей числа:', end=  '  ')
    print('Вывод всех делителей числа (1 способ):', end=  '  ')
    for i in range (y-1 , 1 , -1):
        if y%i==0:
            delitely.append(i)
           # print(i, end=',')
    print(type(delitely),delitely)
Vivod_vseh_del(x)
print('Вывод всех делителей числа (глобальная переменная):',type(delitely), delitely)
def Vivod_vseh_del2(y):
    print('Вывод всех делителей числа(2 способ):', end=  '  ')
    for i in range (y-1 , 1 , -1):
        if y%i==0:
            print(type(i),i, end=',')
    print('  ')
Vivod_vseh_del2(x)

#3) выводит самый большой простой делитель числа.
def Vivod_bolsh_prost_del(y):
    naib_delitel = []
    for i in range(y - 1, 1, -1):
        shet = 0  # Счётчик
        if (y % i == 0):
            for j in range(i - 1, 1, -1): #так как перебор идет от большего к меньшему
                if (i % j == 0):
                    shet = shet + 1  # Увеличиваем, если находим делитель
            if (shet == 0):  # Если делителей не было найдено, выводим
                print('Наибольший ПРОСТОЙ делитель(так как перебор идет от большего к меньшему и выводим первый результат)::',type(i),i, end=" ")
                print('  ')
            if (shet == 0):  # Если делителей не было найдено, выводим
                naib_delitel.append(i)
                print('Наибольший ПРОСТОЙ делитель(так как перебор идет от большего к меньшему и выводим первый результат):',type(naib_delitel), naib_delitel)
                return

Vivod_bolsh_prost_del(x)