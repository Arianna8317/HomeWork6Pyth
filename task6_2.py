# определить, входит ли указанное число хотя бы в одну из строк списка
# Filter + lambda
my_list = ["er567","iu5","rtu456t","ffg567" ]
print(my_list)
n = input("Введите число: ")
F = list(filter ( lambda x :   x.find(n)!=-1, my_list ))
if len(F) > 0 :
    print("Ваше число входит в список ") 
else :
    print("Числа нет в списке")  
     