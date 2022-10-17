# 16). Задайте список из n чисел последовательности 〖(1+1/n)〗^n и выведите на экран их сумму.
# LC + Map + lambda
import math
n = int(input ( "Введите число: "))
my_list = [x for x in range ( 1, n + 1 )]
my_list = list(map(lambda x: round((1 + 1 / x ) ** x,2 ), my_list))
print (f"Сумма элементов последовательности 〖(1+1/n)〗^n равна {round(sum(my_list),2)}" ) 