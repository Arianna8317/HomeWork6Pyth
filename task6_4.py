# 24. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу
# между максимальным и минимальным значением дробной части элементов.
# Пример:
# o [1.1, 1.2, 3.1, 5, 10.01] => 0.19
# map, lambda

my_list = [1.135, 1.208, 3.723, 5.09, 10.011]
print(my_list)
fractures = list(map(lambda x : round((abs(x) % 1), 4), my_list))
print(fractures)
print(max(fractures) - min(fractures))

# def fractional_difference(list):
#     min = 1.0
#     max = 0.0
#     for i in range ( len ( list)) :
#         fruct = round ( ( abs (list[i]) % 1 ), 4 )
#         if fruct != 0.0:   # предлагается игнорировать целые числа
#             if max < fruct : 
#               max = fruct
#             if fruct < min :
#               min = fruct 
#     return  max - min 

# my_list = [1.135, 1.208, 3.723, 5, 10.011]   
# print (fractional_difference(my_list)) 
# list_1 = [round(val % 1, 2) for val in my_list]
# print(max(list_1) - min(list_1))           