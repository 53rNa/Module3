# Задача "Счётчик вызовов":

calls = 0                                           # Переменная для ссчетчика вызовов функций
def count_calls() :                                 # Функция для сподсчета
    global calls
    calls += 1
    return calls

def string_info(string) :                           # Функция получает параметр в виде строки
    count_calls()                                   # и возвращает сформированный кортеж из длинны этой строки
    lenght = int(len(string))                       # и двух строк в разных регистрах:(10, 'ARMAGEDDON', 'armageddon')
    UppCase = string.upper()
    LowCase = string.lower()
    values = tuple([lenght, UppCase, LowCase])
    return (values)

def is_contains(string, list_to_search) :           # Функция is_contains принимает два аргумента: строку и список,
    count_calls()                                   # и возвращает True, если строка находится в этом списке,
    for item in list_to_search:                     # False - если отсутствует. Регистр пренебрегается
        if string.upper() == item.upper():
            return True
        else :
            return False

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))

#print(f"Функции string_info и is_contains были вызваны {calls} раз(а)")
print (calls)


