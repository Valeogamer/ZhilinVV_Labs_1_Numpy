import numpy as np
import timeit
from datetime import datetime
"""
2. Выполнить генерацию:
a. линейного массива (вектора) чисел с плавающей точкой произвольного размера;
b. выполнить генерацию двумерного массива (матрицы) чисел с плавающей точкой
произвольного размера;
c. генерацию массивов выполнять с размерностью в сотни, тысячи, сотни тысяч
элементов.
d. для каждого массива выполнить оценку времени, затраченного на генерацию.
e. сравнить показатели с массивами, генерируемыми средствами стандартной 
библиотеки языка Python аналогичной размерности.
"""
def ex_1():
    print("*" * 15, "Задание 2.a", "*" * 15)
    matrix_1 = np.arange(1, 100, 1.5)
    print("Тип данных", matrix_1.dtype)
    print("Кол-во элементов: ", matrix_1.shape, "\n")
    
    print("*" * 15, "Задание 2.b", "*" * 15)
    matrix_2 = np.random.random((10,10))

    print("Тип данных", matrix_2.dtype)
    print("Кол-во элементов: ", matrix_2.shape, "\n")

    print("*" * 15, "Задание 2.c - 100", "*" * 15)
    matrix_3 = np.random.random((100,100))
    print("Тип данных", matrix_3.dtype)
    print("Кол-во элементов: ", matrix_3.shape, "\n")

    print("*" * 15, "Задание 2. - 1000", "*" * 15)
    matrix_4 = np.random.random((1000,1000))
    print("Тип данных", matrix_4.dtype)
    print("Кол-во элементов: ", matrix_4.shape, "\n")
    
    print("*" * 15, "Задание 2.c - 100000", "*" * 15)
    matrix_5 = np.random.random_sample((100000))
    print("Тип данных", matrix_5.dtype)
    print("Кол-во элементов: ", matrix_5.shape, "\n")
    

def m_1(n):
    matrix_100 = np.arange(n)
    return matrix_100

def m_2(n,k):
    matrix_10 = np.random.random((n,k))
    return matrix_10

def m_3(n,k):
    matrix_100 = np.random.random((n,k))
    return matrix_100

def m_4(n,k):
    matrix_1000 = np.random.random((n,k))
    return matrix_1000

def m_5(n):
    matrix_100000 = np.random.random_sample((n))
    return matrix_100000

#########################################################

def ms_1(n):
    matrix_100 = []
    [matrix_100.append(i) for i in range(n)]
    return matrix_100

def ms_2(n, k):
    matrix_10 = [[0] * n for i in range(k)]
    return matrix_10

def ms_3(n, k):
    matrix_100 = [[0] * n for i in range(k)]
    return matrix_100

def ms_4(n, k):
    matrix_1000 = [[0] * n for i in range(k)]
    return matrix_1000

def ms_5(n):
    matrix_100000 = []
    [matrix_100000.append(i) for i in range(n)]
    return matrix_100000

########################### Для timeit #############################

mm_1 = """
import numpy as np
matrix = np.arange(100)
"""
mm_2 = """
import numpy as np
matrix_10 = np.random.random((10,10))
"""
mm_3 = """
import numpy as np
matrix_100 = np.random.random((100,100))
"""
mm_4 = """
import numpy as np
matrix_1000 = np.random.random((1000,1000))
"""
mm_5 = """
import numpy as np
matrix_100000 = np.random.random_sample((100000))
"""

mx_1 = """
matrix_100 = []
[matrix_100.append(i) for i in range(100)]
"""
mx_2 = """
matrix_10 = [[0] * 10 for i in range(10)]
"""
mx_3 = """
matrix_100 = [[0] * 100 for i in range(100)]
"""
mx_4 = """
matrix_1000 = [[0] * 1000 for i in range(1000)]
"""
mx_5 = """
[matrix_100000.append(i) for i in range(100000)]
"""

if __name__ == "__main__":
    ex_1()
    print("Отчет времени datatime\n")
    print("---Матрицы способом arrange---")
    start_time = datetime.now()
    m_1(100)
    print("Массив из 100 элементов:", datetime.now() - start_time)
    start_time = datetime.now()
    m_2(10, 10)
    print("Матрица 10 на 10:", datetime.now() - start_time)
    start_time = datetime.now()
    m_3(100, 100)
    print("Матрица 100 на 100:", datetime.now() - start_time)
    start_time = datetime.now()
    m_4(1000, 1000)
    print("Матрица 1000 на 1000:", datetime.now() - start_time)
    start_time = datetime.now()
    m_5(100000)
    print("Матрица 100000 на 100000:", datetime.now() - start_time)
    print("---Матрицы способом range---")
    start_time = datetime.now()
    ms_1(1000)
    print("Массив из 100 элементов:", datetime.now() - start_time)
    start_time = datetime.now()
    ms_2(10, 10)
    print("Матрица 10 на 10:", datetime.now() - start_time)
    start_time = datetime.now()
    ms_3(100, 100)
    print("Матрица 100 на 100:", datetime.now() - start_time)
    start_time = datetime.now()
    ms_4(1000, 1000)
    print("Матрица 1000 на 1000:", datetime.now() - start_time)
    start_time = datetime.now()
    ms_5(100000)
    print("Матрица 100000 на 100000:", datetime.now() - start_time)
    print("\nОтчет времени timeit \n")
    print("---Матрицы способом arrange---")
    print("Массив из 100 элементов:", timeit.timeit(stmt= mm_1, number=100000))
    print("Массив на 10 на 10:", timeit.timeit(stmt= mm_2, number=100000))
    print("Массив на 100 на 100:", timeit.timeit(stmt= mm_3, number=100000))
    # print("Массив на 1000 на 1000:", timeit.timeit(stmt= mm_4, number=100000))  # ~500.0
    # print("Массив на 100000 на 100000:", timeit.timeit(stmt= mm_5, number=100000)) # ~44.59
    print("---Матрицы способом range---")
    print("Массив из 100 элементов:", timeit.timeit(stmt= mx_1, number=100000))
    print("Массив на 10 на 10:", timeit.timeit(stmt= mx_2, number=100000))
    print("Массив на 100 на 100:", timeit.timeit(stmt= mx_3, number=100000))
    # print("Массив на 1000 на 1000:", timeit.timeit(stmt= mx_4, number=100000))  # ~ 200.00
    # print("Массив на 100000 на 100000:", timeit.timeit(stmt= mx_5, number=100000)) # ~360.00
