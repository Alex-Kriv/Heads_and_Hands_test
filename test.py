import numpy as np
import random

counter = 1

def create_array(lengths_of_arrey, n): # функция создания n массивов
    arr = [0] * n  
    for i in range(n):
        arr[i] = np.random.randint(-100, 100, lengths_of_arrey[i]) # обьявления массива со случайными значениями в диапозоне от -100 до 100
        print('\n','Массив №',i+1,'до сортировки' , arr[i])
    return arr


def function(n):
    lengths_of_arrey = random.sample(range(1, n + 10), n) # обьвление уникальных длин массивов, но не более чем n + 10
    arr = create_array(lengths_of_arrey, n)
    for i in range(n): # функция сортировки по возростанию для (ч), убыванию для (н)
        if i % 2 == 0:
           arr[i].sort()
        else:
           arr[i][::-1].sort()
    return arr


n = int(input("Введите количество массивов: "))
for i in function(n):
    print('\n', 'Массив №', counter, 'после сортировки', i)
    counter += 1
