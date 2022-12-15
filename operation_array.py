import numpy as np

arr = np.arange(1, 11)
print("Массив: ", arr, "\n")

arr = np.sin(arr)
print("Массив sin: ", arr, "\n")

arr = np.cos(arr)
print("Массив cos: ", arr, "\n")

arr = np.log(arr)
print("Массив log: ", arr, "\n")

arr = np.exp(arr)
print("Массив exp: ", arr, "\n")


"""
Сложение
"""
print("*" * 15, "Сложение", "*" * 15)
a = np.arange(1, 11)
b = np.arange(11, 21)
res = a + b  # 1 способ
print(f"a + b = {res}")
res_1 = np.add(a, b)  # 2 способ
print(f"a + b = {res_1} \n")

"""
Вычитание
"""
print("*" * 15, "Вычитание", "*" * 15)
a = np.arange(1, 11)
b = np.arange(11, 21)
res = a - b  # 1 способ
print(f"a - b = {res}")
res_1 = np.subtract(a, b)  # 2 способ
print(f"a - b = {res_1} \n")

"""
Умножение
"""
print("*" * 15, "Умножение", "*" * 15)
a = np.arange(1, 11)
b = np.arange(11, 21)
res = a * b  # 1 способ
print(f"a * b = {res}")
res_1 = np.multiply(a, b)  # 2 способ
print(f"a * b = {res_1} \n")

"""
Деление
"""
print("*" * 15, "Деление", "*" * 15)
a = np.arange(1, 11)
b = np.arange(11, 21)
res = a / b  # 1 способ
print(f"a / b = {res}")
res_1 = np.divide(a, b)  # 2 способ
print(f"a / b = {res_1} \n")
"""
степень, с остатком, без остатка и прочее так же работают
"""

"""
Некоторые плюшки
"""
print("*" * 15, "Плюшки", "*" * 15)
a = np.arange(1, 11)
res = a * 2  # все значения умножили на 2 и многое другое так эе можно
print(res)


"""
Функции агрегаторы
"""
print("*" * 15, "Функции агрегаторы", "*" * 15)
arr = np.arange(1, 11)
print("Max: ", arr.max())
print("Min: ", arr.min())
print("Mean: ", arr.mean())
print("Sum: ", arr.sum())
print("Std: ", arr.std())
print("Median: ", np.median(arr))
print("Все что 2 < :", arr > 2, "\n")

"""
Манипуляции с массивами
"""
print("*" * 15, "Манипуляции с массивами", "*" * 15)
print("Добавление нового элемента в обозначенное место: ")
print(np.insert(arr, 2, 777))  # insert(arr, index(position), value)
print("Удаление выбранного элемента по индексу: ")
print(np.delete(arr, 2))  # insert(arr, index(position))
arr_1 = np.array([23,34, 45, 6542, -1, -432])
print("Сортировка: ")
print(np.sort(arr_1))  # Сортировка
print("Склейка: ")
print(np.concatenate((arr, arr_1)))  # скливание двух массивов
print("Разделение нашего массива на n кол-во массивов: ")
print(np.split(arr_1, 2), "\n")

"""
Работа с индексами
"""
print("*" * 15, "Работа с индексами = ", "*" * 15)
arr = np.arange(1, 11)
print("Значение нулевого индекса = ", arr[0])
arr[5] = 888
print("Ручная замена выбранного индекса: arr[5] = 888, тогда теперь arr[5] =", arr[5])
print("Срез с 0 до 5 = ", arr[0:6])
print("arr < 2 = ", arr < 2)
print("arr[(arr < 2) & (arr > 0)] = ", arr[(arr < 2) & (arr > 0)])
print("arr[(arr < 2) | (arr > 0)] = ", arr[(arr < 2) & (arr > 0)])
arr[0:4] = 5
print("Заменить на 5 с 0 до 3, arr[0:4] = ", arr[0:4], "\n")
