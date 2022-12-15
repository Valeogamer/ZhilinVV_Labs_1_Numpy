import numpy as np

"""
Способы создания массивов в NumPy
"""

# №1
print("*"*15, "№1", "*"*15)
data = []
[data.append(i) for i in range(1, 100000)]
#print("List: ", data)
arr1 = np.array(data)
print("Массив: ", arr1)
print("Кол-во элементов: ",arr1.shape)
print("Тип данных: ",arr1.dtype)
print("Размерность массива: ",arr1.ndim, "\n")

# №2
print("*"*15, "№2", "*"*15)
arr2 = np.array([1, 2, 3, 4, 5])
print("Массив: ", arr2)
print("Кол-во элементов: ",arr2.shape)
print("Тип данных: ",arr2.dtype)
print("Размерность массива: ",arr2.ndim, "\n")

# №3
print("*"*15, "№3", "*"*15)
arr3 = np.array([1, 2, 3, 4, 5], dtype=float)  # явно задаем тип данных
print("Массив: ", arr3)
print("Кол-во элементов: ",arr3.shape)
print("Тип данных: ",arr3.dtype)
print("Размерность массива: ",arr3.ndim)
arr3 = arr3.astype(np.int64)  # приводим все элементы к типу int 64
print("Массив: ",arr3)
print("Тип данных: ", arr3.dtype, "\n")

# №4
"""
С помощью аналога range
np.arange(start, stop, step)
в отличие от range, arange умеет работать с дробными числами
"""
print("*"*15, "№4", "*"*15)
arr4 = np.arange(1, 21)
print(arr4, "\n")

# №5
"""
np.linspace(start, stop, cnt_value)
"""
print("*"*15, "№5", "*"*15)
arr5 = np.linspace(0, 10, 100000)  # 100000 чисел от 0 до 10 
print(arr5)
print("Кол-во элементов", arr5.shape, "\n")

# №6
"""
Заполнение рандомными числами
np.random.random((5,))
"""
print("*"*15, "№6", "*"*15)
arr6 = np.random.random((100000,))  # кол-во элементов
print("Кол-во элементов: ", arr6.shape)
print("Массив срез от 0 до 10: ", arr6[0:11], "\n")

# №7
"""
Заполнение рандомными числами
np.random.random_sample((5,))
"""
print("*"*15, "№7", "*"*15)
arr7 = np.random.random_sample((100000,))  # кол-во элементов
print("Кол-во элементов: ", arr7.shape)
print("Массив срез от 0 до 10: ", arr7[0:11], "\n")

# №8
"""
Заполнение рандомными числами с диапазоном
от - 5 до 10
"""
print("*"*15, "№8", "*"*15)
arr8 = (10 - -5) * np.random.random_sample((100000,)) - 5  # кол-во элементов
print("Кол-во элементов: ", arr8.shape)
print("Массив срез от 0 до 10: ", arr8[0:11], "\n")

# №9
"""
Заполнение рандомными числами с диапазоном
от - 5 до 10
"""
print("*"*15, "№9", "*"*15)
arr9 = np.random.randint(-5, 10, 10) # кол-во элементов
print("Кол-во элементов: ", arr9.shape)
print("Массив: ", arr9, "\n")