#Задание "Раз, два, три, четыре, пять .... Это не всё?"
def calculate_structure_sum(*args):
    sum_num = 0
    sum_len_str = 0
    count = 0

    while count < len(args):
        vol = args[count]

        if isinstance(vol, (list, tuple, set)):             # Если это список, кортеж или множество
            num, len_str = calculate_structure_sum(*vol)
            sum_num += num
            sum_len_str += len_str
        elif isinstance(vol, dict):                         # Если это словарь
            for key, value in vol.items():
                if isinstance(key, (int, str)):             # Ключи словаря
                    sum_num += 0                            # не включаем к сумме чисел
                    sum_len_str += len(key)                 # Складываем длину ключей
                if isinstance(value, (int, str, list, tuple, set, dict)):
                    args = args + (value,)                  # Записываем значения в список
        elif isinstance(vol, int):                          # Если это число, включаем его в сумму чисел
            sum_num += vol
        elif isinstance(vol, str):                          # Если это строка, включаем ее длину к длине всех строк
            sum_len_str += len(vol)

        count += 1
    return sum_num, sum_len_str

data_structure = [[1, 2, 3],{'a': 4, 'b': 5},(6, {'cube': 7, 'drum': 8}),"Hello",((), [{(2, 'Urban', ('Urban2', 35))}])]
result = sum(calculate_structure_sum(data_structure))
print (result)
