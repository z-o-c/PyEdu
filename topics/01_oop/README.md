# Объектно-ориентированное программирование (ООП)

**Почему важно**: Вы уже используете типы данных, но не создавали свои классы. ООП - фундамент для больших проектов.

**Что изучать**:
- Классы и объекты
- Инкапсуляция (приватные/публичные атрибуты)
- Наследование
- Полиморфизм
- Методы классов и статические методы
- Специальные методы (`__init__`, `__str__`, `__repr__`, `__len__`, etc.)
- Дескрипторы и свойства (properties)

**Материалы**:
- **Официальная документация**: https://docs.python.org/3/tutorial/classes.html
- **Real Python - OOP**: https://realpython.com/python3-object-oriented-programming/
- **"Python Tricks"** by Dan Bader (главы об ООП)
- **"Fluent Python"** by Luciano Ramalho (главы 1-6)

---

## Задача 1.1: Класс для работы с матрицами

**Описание**: Создать класс `Matrix` для работы с матрицами с поддержкой основных операций.

**Технические требования**:
- Класс должен хранить матрицу в виде списка списков
- Конструктор принимает список списков или создает матрицу заданного размера
- Методы: `__add__`, `__sub__`, `__mul__` (умножение на число и матричное умножение)
- Методы: `__str__`, `__repr__`, `__eq__`
- Метод `transpose()` для транспонирования
- Метод `determinant()` для вычисления определителя (для квадратных матриц)

**Тест-кейсы**:
```python
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

# Тест 5: Транспонирование
m8 = Matrix([[1, 2, 3], [4, 5, 6]])
m9 = m8.transpose()
assert m9.data == [[1, 4], [2, 5], [3, 6]]

# Тест 6: Определитель
m10 = Matrix([[1, 2], [3, 4]])
assert m10.determinant() == -2

# Тест 7: Сравнение матриц
m11 = Matrix([[1, 2], [3, 4]])
assert m1 == m11
```

**Выходной результат**:
- Файл `matrix.py` с классом `Matrix`
- Все тест-кейсы должны проходить успешно
- Код должен содержать docstrings для всех методов

---

## Задача 1.2: Иерархия классов для анализа текста

**Описание**: Создать иерархию классов для анализа текста с использованием наследования и полиморфизма.

**Технические требования**:
- Базовый класс `TextAnalyzer` с методом `analyze(text: str) -> dict`
- Класс `WordFrequencyAnalyzer(TextAnalyzer)` - подсчет частоты слов
- Класс `CharacterFrequencyAnalyzer(TextAnalyzer)` - подсчет частоты символов
- Класс `SentenceAnalyzer(TextAnalyzer)` - анализ предложений (количество, средняя длина)
- Все классы должны иметь метод `analyze()` с разной реализацией (полиморфизм)

**Тест-кейсы**:
```python
# Тест 1: Анализ частоты слов
text = "Python is great. Python is powerful. Python is easy."
analyzer1 = WordFrequencyAnalyzer()
result1 = analyzer1.analyze(text)
assert result1['python'] == 3
assert result1['is'] == 3
assert result1['great'] == 1

# Тест 2: Анализ частоты символов
analyzer2 = CharacterFrequencyAnalyzer()
result2 = analyzer2.analyze(text)
assert result2['p'] > 0
assert result2[' '] > 0  # пробелы

# Тест 3: Анализ предложений
analyzer3 = SentenceAnalyzer()
result3 = analyzer3.analyze(text)
assert result3['sentence_count'] == 3
assert result3['avg_sentence_length'] > 0

# Тест 4: Полиморфизм - работа через базовый класс
analyzers = [WordFrequencyAnalyzer(), CharacterFrequencyAnalyzer(), SentenceAnalyzer()]
results = [a.analyze(text) for a in analyzers]
assert len(results) == 3
assert all(isinstance(r, dict) for r in results)
```

**Выходной результат**:
- Файл `text_analyzers.py` с классами
- Все тест-кейсы должны проходить
- Демонстрация полиморфизма в отдельном файле `demo.py`

---

