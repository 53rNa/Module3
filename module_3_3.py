# Задача "Распаковка"
def print_params(a=5, b='string', c=True):
    print (a,b,c)

#print_params()
#print_params(b=25)
#print_params(c = [1,2,3])

values_list = [34, 'flag', False]
values_dict = {'a': 45, 'b': 'red', 'c': True}

#print_params(*values_list)
#print_params(**values_dict)

values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)