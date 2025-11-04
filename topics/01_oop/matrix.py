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

        if isinstance(other, (int, float)):
            pass


try:
    # Тест 1: Создание матрицы
    m1 = Matrix([[1, 2], [3, 4]])
    assert str(m1) == "[[1, 2], [3, 4]]"

    # Тест 2: Сложение матриц
    m2 = Matrix([[5, 6], [7, 8]])
    m3 = m1 + m2
    assert m3.data == [[6, 8], [10, 12]]

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

except (TypeError, ValueError) as e:
    print(f"Ошибка: {e}")