import random
print('подсчет количества символов:', len("п.р,и-в=ет_111;:")) #подсчет количества символов
print('случайное число от 0 до 1:', random.random()) #случайное число от 0 до 1

city_list = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Philadelphia']
print("Выбор случайного города из списка - ", random.choice(city_list))

print("Генерация случайного числа в пределах заданного промежутка", random.randrange(10, 50, 3))

print("random.choice используется для выбора случайного элемента из списка - ", random.choice([55, 66, 77, 88, 99]))
list = [47, 4567, 345, 789, 9344]
print("random.choice используется для выбора случайного элемента из списка - ", random.choice(list))

list = [2, 5, 8, 9, 12, 55, 68, 79, 712]
print ("random.sample() три случайных элемента ", random.sample(list,3))

# Выборка с заменой
list = [20, 30, 40, 50, 60, 70, 80, 90]
sampling = random.choices(list, k=8)
print("Выборка с методом choices ", sampling)

list = [2, 5, 8, 9, 12]
random.shuffle(list)
print("Вывод перемешанного списка ", list)

print("Число с плавающей точкой в пределах заданного промежутка, сгенерировать случайно вещественное число в промежутке между 10.5 и 25.5.")
print(random.uniform(10.5, 25.5))