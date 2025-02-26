'''Преобраование строку ввода в число (float или complex).'''

def parse_input_to_number(input_str: str):
    input_str = " ".join(input_str.split())

    if " " in input_str:
        real, imag = map(float, input_str.split())
        return complex(real, imag)
    return float(input_str)

'''Вычисление определителя матрицы'''

def calculate_determinant(matrix): 
    size = len(matrix)
    if size == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    determinant = 0
    for column in range(size):
        submatrix = [row[:column] + row[column + 1:] for row in matrix[1:]]
        sign = 1 if column % 2 == 0 else -1
        determinant += sign * matrix[0][column] * calculate_determinant(submatrix)
    
    return determinant

'''Решение системы уравнений методом Крамера.'''

def solve(coefficient_matrix, free_terms):
    det = calculate_determinant(coefficient_matrix)

    if det == 0:
        print("Решения нет, определитель равен 0")
        return
    
    print("Решение:")
    size = len(coefficient_matrix)
    for i in range(size):
        modified_matrix = [row[:i] + [free_terms[j]] + row[i + 1:] for j, row in enumerate(coefficient_matrix)]
        modified_det = calculate_determinant(modified_matrix)
        print(f"x{i + 1} = {modified_det / det}")
        
def main():
    matrix_size = int(input("Введите размерность расширенной матрицы n x (n + 1): "))
    
    print("Комплексные числа вводите через пробел.")
    coefficient_matrix = []
    free_terms = []
    
    for i in range(matrix_size):
        row = []
        for j in range(matrix_size):
            user_input = input(f"Строка {i + 1}, столбец {j + 1}: ").strip()
            row.append(parse_input_to_number(user_input))
        coefficient_matrix.append(row)
        
        free_term_input = input(f"Свободный член матрицы {i + 1}: ").strip()
        free_terms.append(parse_input_to_number(free_term_input))

    print("\nМатрица:")
    for i in range(matrix_size):
        print(coefficient_matrix[i], end=" ")
        print(f"| {free_terms[i]}")

    solve(coefficient_matrix, free_terms)

if __name__ == "__main__":
    main()


