# Алгоритм 5

# 1. Напишите алгоритм быстрой сортировки (quick sort)
# Рассмотрите, как алгоритм работает в отладчике (debug)
# список для сортировки 
import random

lst = [3, 14, 1, 7, 9, 8, 11, 6, 4, 2]

def quick_sort(lst):
    if len(lst) <= 1: 
        return lst
    else:
        number = random.choice(lst)
    Left = []
    Middle = []
    Right = []
    for i in lst:
        if i < number:
            Left.append(i)
        elif i > number:
            Right.append(i)
        else:
            Middle.append(i)
    return quick_sort(Left) + Middle + quick_sort(Right)


#print(quick_sort(lst))


# Дополнительно
# 2. Создайте функцию min/max, которая использует алгоритм сортировки написанный выше 

def min(lst):
    quick_sort(lst) 
    return quick_sort(lst)[0]

print(min(lst))

def max(lst): 
    quick_sort(lst)
    return quick_sort(lst)[-1] 

print(max(lst))