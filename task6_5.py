# найти в списке неповторяющиеся элементы
my_list = [1, 4, 65, 77, 8, 4, 1, 65, 34, 109]
print(my_list)
result = list (filter(lambda i: my_list.count(i) == 1, my_list))
print (result)