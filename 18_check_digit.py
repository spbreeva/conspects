# Дано:
# * number          – число, 
# * index1, index2  – два индекса 
# * digit           – цифра, которую нужно искать в заднном числе.
 
# Задача состоит в том, чтобы проверить, существует ли цифра в числе в пределах заданных индексов.

# Будьте внимательны! index2 не обязательно больше index1.

# Например:
#     Есть ли цифра 1 в числе 1234567 между индексами 1 и 0? True
#     Есть ли цифра 1 в числе 1234567 между индексами 0 и 1? True
#     Есть ли цифра 4 в числе 67845123654 между индексами 0 и 0? True
#     Есть ли цифра 1 в числе 9999999999 между индексами 2 и 5? False


def find_number_in_range(number, digit, index1, index2):
    if index1 == 0 and index2 == 0:
        digit2 = digit[:]
    elif index1 == 0:
        digit2 = digit[:index2]
    elif index2 == 0: 
        digit2 = digit[:index1]
    elif index1 > index2:
        digit2 = digit[index1:index2]
    else: 
        digit2 = digit[index2:index1]
    
    counter_true = 0
    for i in range(len(digit2)):
        if int(digit2[i]) == number:
            counter_true += 1 
        i += 1 

    if counter_true > 0:
        return True
    else:
        return False
