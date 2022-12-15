#ToDo Написать Игру Жизнь
# 1 - Жив; 0 - мертв
# Проверка окрестностью Мура(фон Неймана)
# Правило игры правило Конвея
import numpy as np

def print_life(arr_size):
    """
    Метод вывода родителя. Начало жизни.
    """
    mat_lifes = life(arr_size)
    print("Исходная матрицы \n ",mat_lifes)

def life(arr_size):
    mat_life = np.random.randint(2, size=(arr_size, arr_size))
    return mat_life

def verification_conditions(arr_size):
    mat_life = life(arr_size)
    new_mat_life= mat_life.copy()
    for i in range(arr_size):
        for j in range(arr_size):
            total = int((mat_life[i, (j-1)%arr_size] + mat_life[i, (j+1)%arr_size] +
                         mat_life[(i-1)%arr_size, j] + mat_life[(i+1)%arr_size, j] +
                         mat_life[(i-1)%arr_size, (j-1)%arr_size] + mat_life[(i-1)%arr_size, (j+1)%arr_size] +
                         mat_life[(i+1)%arr_size, (j-1)%arr_size] + mat_life[(i+1)%arr_size, (j+1)%arr_size])/1)
 
            # Правило конвея
            if mat_life[i, j]  == 1:
                if (total < 2) or (total > 3):
                    new_mat_life[i, j] = 0
            else:
                if total == 3:
                    new_mat_life[i, j] = 1
 
    # обновление данных
    mat_life[:] = new_mat_life[:]
    return print(mat_life)
            
def evolution(epoch, arr_size):
    arr_size = arr_size
    for i in range(epoch):
        print(f"Эпоха - {i+1}")
        verification_conditions(arr_size)

if __name__ == "__main__":
    input_mat_size = 10
    epoch = 10
    print_life(input_mat_size)
    verification_conditions(input_mat_size)
    evolution(10, input_mat_size)
