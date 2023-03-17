# Задача №9.
# По данному целому неотрицательному n вычислите значение n!. 
# N! = 1 * 2 * 3 * … * N (произведение всех чисел от 1 до N) 0! = 1 
# Решить задачу используя цикл while
# Input: 5
# Output: 120

# # ВАРИАНТ УРОКА
# while True:
#     number = input('Введите число: ')
#     if number.isdigit():
#      number = int(number)
#      break
#     else:
#        print('Введите целое неотрицательное число!:')
# factorial = 1
# while number > 1:
#     factorial *= number
#     number -= 1
# print(factorial)


# # ВАРИАНТ 1 с циклом WHILE
# n = int(input('Введите число: '))
# factorial = 1
# i = 0
# while (i <= n ):
#     if i == n :
#          break
#     i = i + 1
#     factorial = factorial * i
#     print(i)
# print(n, '!', '=', factorial)


# ВАРИАНТ 2 с циклом FOR
# n = int(input('Введите число: '))
# factorial = 1
# if n == 0:
#     print('0! = 1')
# else:
#     factorial = 1
#     for i in range(1, n + 1):
#         # factorial = factorial * i 
#         factorial *=i
#         print(i)
# # print(n, '!', '=', factorial)
# print(factorial)



# Задача №11.
# Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является,
# то есть выведите такое число n, что φ(n)=A. Если А не является числом Фибоначчи, 
# выведите число -1.
# Input: 5
# Output: 6

# # ВАРИАНТ 1 СТОУНс (обмен переменными)
# number = int(input('Введите число: '))
# fibo_1, fibo_2, index = 0, 1, 1

# while fibo_2 < number:
#     fibo_1, fibo_2 = fibo_2, fibo_1 + fibo_2
#     index += 1
# if fibo_2 == number:
#     print(index)
# else:
#     print(-1)



# # ВАРИАНТ 2
# a = int(input('Введите число Финабоччи: '))
# fib_prev = 0
# fib_curr = 1
# n = 1
# while fib_curr < a:
#     fib_next = fib_prev + fib_curr
#     fib_prev = fib_curr
#     fib_curr = fib_next
#     n += 1
# if fib_curr == a:
#     print(n)
# else:
#     print(-1)   

# # ВАРИАНТ 3
# import os
# os.system('cls')
# n = int(input('Введите число А: '))
# number_1 = 0
# number_2 = 1
# a = 2
# while True:
#     sum = number_1 + number_2
#     number_1 = number_2
#     number_2 = sum
#     a += 1
#     if sum == n:
#         print(a)
#         break 
#     elif sum > n:
#         print(-1)
#         break
    
    

# Задача №13.
# Уставшие от необычно теплой зимы, жители решили узнать,действительно ли это самая
# длинная оттепель за всю историю наблюдений за погодой. Они обратились к синоптикам,
# а те, в свою очередь, занялись исследованиями статистики запрошлые годы. Их интересует,
# сколько дней длилась самая длинная оттепель. Оттепелью они называют период, вкоторый
# среднесуточная температура ежедневно превышала 0 градусов Цельсия. Напишите программу, 
# помогающую синоптикам в работе.
# Пользователь вводит число N – общее количество рассматриваемых дней (1 ≤ N ≤ 100). 
# В следующих строках располагается N целых чисел.Каждое число – среднесуточная температура в
# соответствующий день. Температуры – целые числа и лежат в диапазоне от –50 до 50
# Input: 6 -> -20 30 -40 50 10 -10
# Output: 2

# # ВАРИАНТ 1
# import random
# days = int(input('Введите количество дней: '))
# today = 0
# warm_count = 0
# max_warm = 0

# for _ in range(days):
#     today += random.randint(-3,3)
#     print(today, end=' ')
#     if today >0:
#         warm_count += 1
#     else:
#         if max_warm < warm_count:
#             max_warm = warm_count
#         warm_count = 0
# else:  
#     if max_warm < warm_count:
#         max_warm = warm_count
#     warm_count = 0
# print(f'\nСамая долгая оттепель была {max_warm} дней')

  
# # ВАРИАНТ2 В КЛАССЕ

# import random
# days = int(input('Введите кол-во дней: '))
# today = 0 #температура сегодня 0 градусов
# warm_days = 0
# warm_period = 0

# for _ in range(days):
#     print(today, end=' ')
#     today += random.randint(-3,3)
#     if today > 0:
#         warm_days += 1
#         if warm_period < warm_days:
#             warm_period = warm_days
#     if today <= 0:
#         warm_days = 0
# print('Самая долгая оттепель равна ', warm_period)                



# Задача №15. 
# Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, 
# а другой для тещи. Понятно, что для себя нужно выбрать арбуз потяжелей, а для тещи полегче.
# Но вот незадача: арбузов слишком много и он не знает как же выбрать самый легкий и самый 
# тяжелый арбуз? Помогите ему! Пользователь вводит одно число N – количество арбузов. 
# Вторая строка содержит N чисел,записанных на новой строчке каждое. Здесь каждое число – 
# это масса соответствующего арбуза
# Input: 5 -> 5 1 6 5 9
# Output: 1 9

# #  ВАРИАНТ 1
# from random import randint
# count = int(input('Введите количество арбузов: '))

# i = 0
# min_weight = 30000
# max_weight = 1000
# while i < count:
#     current_weight = randint(1000, 30000)
#     print(current_weight, end=' ')
#     if min_weight > current_weight:
#         min_weight = current_weight
#     if max_weight < current_weight:
#         max_weight = current_weight
#         i += 1
# print(f'\nСебе {max_weight}кг, а тёще {min_weight}кг')

# # ВАРИАНТ 2a через FOR

# from random import randint
# count = int(input('Введите количество арбузов: '))

# min_weight = 30000
# max_weight = 1000
# for i in range(count):
#         print(i)
#         current_weight = randint(1000, 30000)
#         print(current_weight, end=' ')
#         if min_weight > current_weight:
#             min_weight = current_weight
#         if max_weight < current_weight:
#             max_weight = current_weight
        
# print(f'\nСебе {max_weight}кг, а тёще {min_weight}кг')

# # ВАРИАНТ САВЕЛИЯ СПИСКОМ 
# cmealons = int(input('Введите кол-во арбузов: '))
# mealons = []
# for e in range(0, cmealons):
#     mealons.append(int(input('Введите вес арбуза: ')))    #randint(2,9)
# print(mealons)
# tyoshya=min(mealons)
# myself=max(mealons)
# print(tyoshya)
# print(myself)



# # ВАРИАНТ 3

# from random import randint
# n = int(input('Введите количество арбузов: '))
# ar_max = 1000
# ar_min = 30000
# while n!=0:
#     ves = randint(1000,30000)
#     print(ves, end=' ')
#     if ves > ar_max:
#         ar_max = ves
#     if ves < ar_min:
#         ar_min = ves
#         n -= 1
# print()  
# print(f'Самый тяжёлый арбуз {ar_max} кг.')  
# print(f'Самый лёгкий арбуз {ar_min} кг.')  

