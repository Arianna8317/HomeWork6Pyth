# программа проверяет истинность выражний
# (!x & !y & !z) и ! ( x | y | z) для всех значений предикатов
# ZIP

L1 =[0, 0, 0, 0, 1, 1, 1 ,1]
L2 =[0, 0, 1, 1, 0, 0, 1 ,1]
L3 =[0, 1, 0, 1, 0, 1, 0 ,1]
print (list(zip(L1, L2, L3)))
for (x, y, z) in zip(L1, L2, L3):
        print(f" {int(( not x ) and ( not y ) and ( not z))} : {int ( ( not x ) and ( not y ) and ( not z) )} ", end = '    ' )


# Flag = True
# print('x y z F1  x y z F2')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             f1 = int ( not ( x or y or z ))
#             print(f"{x} {y} {z} {f1}", end = '   ')
#             f2 = int ( ( not x ) and ( not y ) and ( not z) )
#             print( x, y, z, f2)
#             if f1 != f2:
#                 Flag = False
# print (f"Выражения (!x & !y & !z) и ! ( x | y | z)", end = " ")
# if  not Flag :
#     print ("НЕ ", end = " ")
# print ("тождественны ")    
                    