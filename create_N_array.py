import numpy as np

"""
Матрицы и многомерные массивы
"""
print("*" * 15, "Матрицы", "*" * 15)
matrix = np.array([(1, 2, 3), (4, 5, 6)], dtype=np.int64)
print("Матрица: \n", matrix, "\n")

matrix = np.array([(1, 2, 3), (4, 5, 6), (7, 8, 9)], dtype=np.float64)
print("Матрица: \n", matrix, "\n")

arr_3D = np.array([[[1, 2], [3, 4], [5, 6]]])
print("Трехмерный массив: \n", arr_3D)

print("Колво элементов: ", matrix.shape)
print("Размерность: ", matrix.ndim)
print("Тип данных: ", matrix.dtype, "\n")

matrix_1 = np.array([(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12)], dtype=np.int64)
print("Было: \n", matrix_1)
print("Сделали из 4 строк 2 строки")
print("Стало: \n", matrix_1.reshape(2, 6), "\n")

matrix_2 = np.random.random((2,2))
print("Случайная двумерная матрица размером 2 на 2: \n", matrix_2, "\n")

print("Срез матрицы")
print("Было: \n", matrix_1)
print("Стало: \n", np.resize(matrix_1, (2,2)), "\n")


print("Arange для матриц")
new_matrix = np.arange(16).reshape(2,8)
print("Матрица созданная с помощью arange, reshape: \n", new_matrix, "\n")


"""
Создание специальных матриц
"""
print("Матрица заполненная нулями")
zeros_matrix = np.zeros((5, 3))  # строк столбцов
print("Матрица с нулями: \n", zeros_matrix, "\n")

print("Матрица заполненная еденицами")
ones_matrix = np.ones((5, 3))  # строк столбцов
print("Матрица с  еденицами: \n", ones_matrix, "\n")

print("Еденичная матрица = все ноль, кроме главной диагонали")
diag_matrix = np.eye(5)
print("Диагональная матрица \n", diag_matrix, "\n")

print("Заполнение матрицы выбранным числом")
full_matrix = np.full((5, 5), 9)
print("Заполненная матрица\n", full_matrix, "\n")

print("Пустая матрица")
empty_matrix = np.empty((3,3))
print("Пустая матрица \n", empty_matrix, "\n")

"""
Операции над матрицами аналогичны(+,-,*,/, **, *3, <>= , sin, log, cos, sum)
но есть и другие фишечки у многомерных матриц
"""
matrix_11 = np.array([(1, 2), (4, 5)])
matrix_22 = np.array([(7, 8), (10, 11)])
print("Скалярное произведение")
dot_matrix = matrix_11.dot(matrix_22)
print("Скалярное произведение двух матриц  \n", dot_matrix, "\n")

print("axis=0 - Это ось строк")
print("axis=1 - Это ось столбцов")
matrix_33 = np.array([(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12)])
print("Было \n", matrix_33)
del_matrix_33 = np.delete(matrix_33, 1, axis=0)
print("Удаляем 1 мтрочку матрицы_33 так выбрали axis=0 -> delete(matrix_33, 1, axis=0)")
print("Стало \n", del_matrix_33, "\n")

print("Исходная матрица, \n", matrix_33)
print("Найдем max каждой строки(axis=0) и столбца(axis=1) ")
print("Max value axis = 0:", matrix_33.max(axis = 0))
print("Max value axis = 1:", matrix_33.max(axis = 1))
print("Найдем min каждой строки(axis=0) и столбца(axis=1) ")
print("Min value axis = 0:", matrix_33.min(axis = 0))
print("Min value axis = 1:", matrix_33.min(axis = 1))
print("Найдем mean каждой строки(axis=0) и столбца(axis=1) ")
print("Mean value axis = 0:", np.mean(matrix_33, axis = 0))
print("Mean value axis = 1:", np.mean(matrix_33, axis = 1))


"""
Индексация
"""
id_matrix = np.array([(1, 2, 3), (4, 5, 6), (7, 8, 9)])
print("Матрица \n", id_matrix)
print("3 строка 3 элемент = ", id_matrix[2, 2])
print("3 строка  = ", id_matrix[2])
print("3 строка  = ", id_matrix[2])
print("3 столбец  = ", id_matrix[:,2])
print("0 и 1 столбец, 1 и 2 строки = ", id_matrix[1:3, 0:2])
print(" > 2 = ", id_matrix[id_matrix > 2], "\n")

"""
Специальные операции
"""
spec_matrix = np.array([(1, 2, 3), (4, 5, 6), (7, 8, 9)])
print("Исходная матрица \n", spec_matrix, "\n")
print("Транспонирование матрицы \n", spec_matrix.T, "\n")
print("Матрицу -> в массив \n", spec_matrix.flatten(), "\n")
#print("Обратная матрица \n", np.linalg.inv(spec_matrix), "\n")
print("След матрицы =", np.trace(spec_matrix))
print("Определитель матрицы = ", np.linalg.det(spec_matrix))
print("Ранг матрицы = ", np.linalg.matrix_rank(spec_matrix))

"""
Дополнитлеьно
"""
#print("Информация = ", np.info(np.linalg))
# print("Загрузка из txt", np.loadtxt('file.txt'))
# print("Загрузка из csv", np.loadtxt('file.csv', delimiter=','))
# print("Save в txt", np.savetxt(file.txt, spec_matrix, delimiter=','))
# print("Save в csv", np.savetxt(file.csv, spec_matrix, delimiter=','))