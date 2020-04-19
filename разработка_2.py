import math
# 1) проверка числа на простоту (простые числа - это те числа у которых делители единица и они сами)

def IsPrime(n):
   d = 2
   print('Пока', n , '/', d, 'без остатка, то')
   while n % d != 0:
       print( n, '/',d,'без остатка')
       d += 1
       print('на что делим 2 раз', n, '/',d)
   return d == n

print('проверяем на простоту',type(IsPrime(7)) , IsPrime(7))

#2) выводит список всех делителей числа;
def get_ls(n):
    """Разложить число на множители"""
    #result = [1]
    result = []
    i = 2
    while i*i <= n:
        if n % i == 0:
            n //= i
            result.append(i)
        else:
            i += 1
    if n > 1:
        result.append(n)
    return result
print (get_ls(16))

#3) выводит самый большой простой делитель числа

def issimple(a):
    prime_num = get_ls(a)
    max_num = 0
    for i in prime_num:
        if i > max_num:
            max_num = i
    return (max_num)
print(issimple(48))