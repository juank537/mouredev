### Tuples ###

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (35, 1.77, "Brais", "Moure", "Brais")
my_other_tuple =  (35, 60, 30)
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])
# print(my_tuple[4]) IndexError
# print(my_tuple[-5]) IndexError


print(f'Brais aparece {str(my_tuple.count("Brais"))} veces.')
print(f'Moure aparece en el índice {str(my_tuple.index("Moure"))}.')

# Las tuplas son inmutables, no se pueden modificar sus valores
# my_tuple[1] = 1.80 'tuple' object does not support item assignment

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

print(my_sum_tuple[3:6])