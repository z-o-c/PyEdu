class Matrix:
    def __init__(self, matrix):
        """Сохраняет переданную матрицу (список списков) в атрибуте self.data"""
        self.data = matrix
    
    def __str__(self) -> str:
        """Возвращает строковое представление матрицы в формате списка списков"""
        return f"{self.data}"

    def __repr__(self) -> str:
        """Возвращает строку, которую можно использовать для воссоздания объекта"""
        return f"Matrix({self.data})"
    
    def __eq__(self, value: object) -> bool:
        pass

    def __add__(self, other):
        """Реализует операцию сложения матриц: matrix1 + matrix2"""

        # проверка на разную длину матриц
        if len(self.data) != len(other.data):
            raise TypeError(f"матрицы разной длины")
        
        else:
            # создание новой матрицы, где будем хранить новые значения
            row, cols = len(self.data), len(self.data[0])
            result = [[0 for i in range(cols)] for i in range(row)]

            # запись данных в новую матрицу
            for index, numbers in enumerate(self.data):
                for ind, num in enumerate(numbers):
                    result[index][ind] = self.data[index][ind] + other.data[index][ind]
            
            return Matrix(result)
    
    def __sub__(self, other):
        """Реализует операцию вычитания матриц: matrix1 - matrix2"""

        if len(self.data) != len(other.data):
            raise TypeError(f"матрицы разной длины")
        
        else:
            # создание новой матрицы, где будем хранить новые значения
            row, cols = len(self.data), len(self.data[0])
            result = [[0 for i in range(cols)] for i in range(row)]

            # запись данных в новую матрицу
            for index, numbers in enumerate(self.data):
                for ind, num in enumerate(numbers):
                    result[index][ind] = self.data[index][ind] - other.data[index][ind]
            
            return Matrix(result)


    def __mul__(self, other):
        """Реализует операцию умножения: matrix * number или matrix * matrix"""

        # создание новой матрицы, где будем хранить новые значения
        row, cols = len(self.data), len(self.data[0])
        result = [[0 for i in range(cols)] for i in range(row)]

        # если число то умножаем не него
        if isinstance(other, (int, float)):

            # создание новой матрицы, где будем хранить новые значения
            row, cols = len(self.data), len(self.data[0])
            result = [[0 for i in range(cols)] for i in range(row)]

            # скалярное умножение
            for index, numbers in enumerate(self.data):
                for ind, num in enumerate(numbers):
                    result[index][ind] = self.data[index][ind] * other
        
            return Matrix(result)
        
        # если матрица то умножаем не нее
        elif isinstance(other, Matrix):
            # матричное умножение: (m x n) * (n x k)
            
            # перед циклами: row_self, cols_self, cols_other
            row_self, cols_self, cols_other = len(self.data), len(self.data[0]), len(other.data[0])
            # создание новой матрицы, где будем хранить новые значения
            result = [[0 for _ in range(cols_other)] for _ in range(row_self)]

            for i, _ in enumerate(self.data):          # строки self
                for j in range(cols_other):                     # столбцы other
                    s = 0
                    for k in range(cols_self):                 # общее измерение
                        s += self.data[i][k] * other.data[k][j]
                    result[i][j] = s

            return Matrix(result)

        else:
            raise TypeError("умножение поддерживается только на число или Matrix")    

    
    def __eq__(self, other) -> bool:
        """Реализует операцию сравнения: matrix1 == matrix2"""

        if isinstance(other, Matrix):
            return self.data == other.data
        
        else:
            raise TypeError("сравнение поддерживается только на Matrix")

try:
    # Тест 1: Создание матрицы
    m1 = Matrix([[1, 2], [3, 4]])
    assert str(m1) == "[[1, 2], [3, 4]]"

    # Тест 2: Сложение матриц
    m2 = Matrix([[5, 6], [7, 8]])
    m3 = m1 + m2
    assert m3.data == [[6, 8], [10, 12]]

    # Тест 3: Умножение на число
    m4 = m1 * 2
    assert m4.data == [[2, 4], [6, 8]]

    # Тест 4: Матричное умножение
    m5 = Matrix([[1, 2], [3, 4]])
    m6 = Matrix([[5, 6], [7, 8]])
    m7 = m5 * m6
    assert m7.data == [[19, 22], [43, 50]]

    # Тест 7: Сравнение матриц
    m11 = Matrix([[1, 2], [3, 4]])
    assert m1 == m11

    # Тест 8: __str__ - проверка формата вывода
    m12 = Matrix([[1, 2, 3], [4, 5, 6]])
    assert str(m12) == "[[1, 2, 3], [4, 5, 6]]"
    assert str(Matrix([[1]])) == "[[1]]"

    # Тест 9: __repr__ - проверка формата представления
    m13 = Matrix([[1, 2], [3, 4]])
    assert "Matrix" in repr(m13)
    assert "[[1, 2], [3, 4]]" in repr(m13)

    # Тест 10: __add__ - сложение разных размеров (дополнительно)
    m14 = Matrix([[1, 2, 3], [4, 5, 6]])
    m15 = Matrix([[7, 8, 9], [10, 11, 12]])
    m16 = m14 + m15
    assert m16.data == [[8, 10, 12], [14, 16, 18]]

    # Тест 11: __sub__ - вычитание матриц
    m17 = Matrix([[10, 20], [30, 40]])
    m18 = Matrix([[1, 2], [3, 4]])
    m19 = m17 - m18
    assert m19.data == [[9, 18], [27, 36]]
    assert (m1 - m1).data == [[0, 0], [0, 0]]  # Вычитание самой себя = нулевая матрица

    # Тест 12: __mul__ - умножение на число (дополнительные случаи)
    m20 = Matrix([[1, 2], [3, 4]])
    assert (m20 * 0).data == [[0, 0], [0, 0]]  # Умножение на ноль
    assert (m20 * -1).data == [[-1, -2], [-3, -4]]  # Умножение на отрицательное число
    assert (m20 * 0.5).data == [[0.5, 1.0], [1.5, 2.0]]  # Умножение на float

    # Тест 13: __mul__ - матричное умножение (разные размеры)
    m21 = Matrix([[1, 2], [3, 4], [5, 6]])  # 3x2
    m22 = Matrix([[1, 2, 3], [4, 5, 6]])    # 2x3
    m23 = m21 * m22  # Результат должен быть 3x3
    assert m23.data == [[9, 12, 15], [19, 26, 33], [29, 40, 51]]

    # Тест 14: __eq__ - проверка неравенства
    m24 = Matrix([[1, 2], [3, 4]])
    m25 = Matrix([[1, 2], [3, 5]])  # Один элемент отличается
    assert m24 != m25
    m26 = Matrix([[1, 2]])  # Разные размеры
    assert m24 != m26

    # Тест 15: Комбинация операций
    m27 = Matrix([[1, 1], [1, 1]])
    m28 = Matrix([[2, 2], [2, 2]])
    result = (m27 * 3) + m28  # ([[3, 3], [3, 3]] + [[2, 2], [2, 2]])
    assert result.data == [[5, 5], [5, 5]]

except (TypeError, ValueError) as e:
    print(f"Ошибка: {e}")