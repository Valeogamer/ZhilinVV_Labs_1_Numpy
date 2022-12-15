import numpy as np

mat_3_3 = np.random.random((3,3))
mat1_3_3 = np.random.random((3,3))
print("Исходные массивы: \n\n", "Первый массив: \n", mat_3_3, "\n\n Второй массив: \n", mat1_3_3, "\n")

print("Сложение \'+\'")
new_mat = mat_3_3 + mat1_3_3
print(new_mat, "\n")

print("Вычитание \'-\'")
new_mat = mat_3_3 - mat1_3_3
print(new_mat, "\n")

print("Деление \'/\'")
new_mat = mat_3_3 / mat1_3_3
print(new_mat, "\n")

print("Деление \'*\'")
new_mat = mat_3_3 * mat1_3_3
print(new_mat, "\n")

print("Скалярное произведение \'^\'")
new_mat = mat_3_3.dot(mat1_3_3)
print(new_mat, "\n")

print("Степень \'**\'")
new_mat = mat_3_3**mat1_3_3
print(new_mat, "\n")

print("Синусы \'sin\'")
new_mat = np.sin(mat_3_3)
print(new_mat, "\n")

print("Косинусы\'cos\'")
new_mat = np.cos(mat_3_3)
print(new_mat, "\n")