immutable_var = 28,9,24,'september', True, [1,2,4]
print(immutable_var)
# immutable_var[1] = 10 - значения в кортеже неизменяемы, но можно изменить список в кортеже
immutable_var[5][2] = 3
print(immutable_var)
mutable_list = [1,2,3,'little',False]
print(mutable_list)
mutable_list[4] = True
mutable_list[3] = 'big'
print(mutable_list)