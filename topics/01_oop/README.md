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

---

## Задача 1.1: Класс для работы с матрицами

**Описание**: Создать класс `Matrix` для работы с матрицами с поддержкой основных операций.

**Технические требования**:
- Класс должен хранить матрицу в виде списка списков в атрибуте `data`
- Конструктор принимает список списков или создает матрицу заданного размера
- Методы: `__add__`, `__sub__`, `__mul__` (умножение на число и матричное умножение)
- Методы: `__str__`, `__repr__`, `__eq__`
- Метод `transpose()` для транспонирования
- Метод `determinant()` для вычисления определителя (для квадратных матриц)

**Подробные инструкции по реализации методов**:

### `__init__(self, matrix)`
- Сохраняет переданную матрицу (список списков) в атрибуте `self.data`
- Пример: `Matrix([[1, 2], [3, 4]])` → `self.data = [[1, 2], [3, 4]]`

### `__str__(self) -> str`
- Возвращает строковое представление матрицы в формате списка списков
- Формат: точно такой же, как у Python списка - `"[[1, 2], [3, 4]]"`
- Используется функцией `str()` и при выводе через `print()`

### `__repr__(self) -> str`
- Возвращает строку, которую можно использовать для воссоздания объекта
- Рекомендуемый формат: `"Matrix([[1, 2], [3, 4]])"`
- Используется при выводе в интерактивном режиме и `repr()`

### `__add__(self, other) -> Matrix`
- Реализует операцию сложения матриц: `matrix1 + matrix2`
- **Логика**: поэлементное сложение двух матриц одинакового размера
- Формула: `result[i][j] = self.data[i][j] + other.data[i][j]`
- Возвращает новый объект `Matrix` с результатом
- Матрицы должны иметь одинаковые размеры (rows и cols)
- Пример: `[[1, 2], [3, 4]] + [[5, 6], [7, 8]] = [[6, 8], [10, 12]]`

### `__sub__(self, other) -> Matrix`
- Реализует операцию вычитания матриц: `matrix1 - matrix2`
- **Логика**: поэлементное вычитание двух матриц одинакового размера
- Формула: `result[i][j] = self.data[i][j] - other.data[i][j]`
- Возвращает новый объект `Matrix` с результатом
- Матрицы должны иметь одинаковые размеры
- Пример: `[[1, 2], [3, 4]] - [[5, 6], [7, 8]] = [[-4, -4], [-4, -4]]`

### `__mul__(self, other) -> Matrix`
- Реализует операцию умножения: `matrix * number` или `matrix * matrix`
- **Важно**: должен работать с двумя типами операндов:
  1. **Умножение на число** (`int` или `float`):
     - Умножает каждый элемент матрицы на число
     - Формула: `result[i][j] = self.data[i][j] * other`
     - Пример: `[[1, 2], [3, 4]] * 2 = [[2, 4], [6, 8]]`
  2. **Матричное умножение** (если `other` - объект `Matrix`):
     - Классическое матричное умножение
     - Формула: `result[i][j] = sum(self.data[i][k] * other.data[k][j] for k in range(кол-во столбцов в self))`
     - Количество столбцов первой матрицы должно равняться количеству строк второй
     - Пример: `[[1, 2], [3, 4]] * [[5, 6], [7, 8]] = [[19, 22], [43, 50]]`
- Определяйте тип `other` через `isinstance(other, (int, float))` или `isinstance(other, Matrix)`
- Возвращает новый объект `Matrix` с результатом

### `__eq__(self, other) -> bool`
- Реализует операцию сравнения: `matrix1 == matrix2`
- **Логика**: две матрицы равны, если они имеют одинаковые размеры и все элементы совпадают
- Сравнивает `self.data` с `other.data` поэлементно
- Возвращает `True` если матрицы равны, `False` в противном случае
- Пример: `Matrix([[1, 2], [3, 4]]) == Matrix([[1, 2], [3, 4]])` → `True`

### `transpose(self) -> Matrix`
- Возвращает транспонированную матрицу (строки становятся столбцами).
- Размер `m×n` превращается в `n×m`.
- Исходную матрицу не изменяет — возвращает новый объект `Matrix`.
- Пример: `Matrix([[1, 2, 3], [4, 5, 6]]).transpose().data == [[1, 4], [2, 5], [3, 6]]`.

### `determinant(self) -> int | float`
- Возвращает определитель квадратной матрицы.
- Допустимо только для квадратных матриц `n×n`; иначе — `ValueError`.
- База: для `1×1` — `a`; для `2×2` — `ad - bc`.
- Пример: `Matrix([[1, 2], [3, 4]]).determinant() == -2`.

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
```

**Выходной результат**:
- Файл `matrix.py` с классом `Matrix`
- Все тест-кейсы должны проходить успешно
- Код должен содержать docstrings для всех методов

---

## Задача 1.2: Иерархия классов для анализа текста

**Описание**: Создать иерархию классов для анализа текста с использованием наследования и полиморфизма. Базовый класс определяет общий интерфейс, а дочерние классы реализуют специфичные алгоритмы анализа.

**Технические требования**:
- Базовый класс `TextAnalyzer` с абстрактным методом `analyze(text: str) -> dict`
- Класс `WordFrequencyAnalyzer(TextAnalyzer)` - подсчет частоты слов (регистронезависимо)
- Класс `CharacterFrequencyAnalyzer(TextAnalyzer)` - подсчет частоты символов
- Класс `SentenceAnalyzer(TextAnalyzer)` - анализ предложений (количество, средняя длина)
- Все классы должны иметь метод `analyze()` с разной реализацией (полиморфизм)
- Использовать наследование для переиспользования кода
- Применить нормализацию текста (приведение к нижнему регистру, удаление знаков препинания где необходимо)

**Подробные инструкции по реализации классов**:

### Базовый класс `TextAnalyzer`

#### `__init__(self)`
- Конструктор базового класса (может быть пустым или содержать общие атрибуты)
- Пример: `analyzer = TextAnalyzer()`

#### `analyze(self, text: str) -> dict`
- **Абстрактный метод** - должен быть определен в базовом классе, но выбрасывать `NotImplementedError`
- Или можно использовать `abc.ABC` и `@abstractmethod` для создания абстрактного класса
- Метод принимает строку текста и возвращает словарь с результатами анализа
- Формат возвращаемого значения зависит от конкретной реализации дочернего класса
- Пример реализации в базовом классе:
  ```python
  def analyze(self, text: str) -> dict:
      raise NotImplementedError("Subclasses must implement analyze method")
  ```

### Класс `WordFrequencyAnalyzer(TextAnalyzer)`

#### `analyze(self, text: str) -> dict`
- **Логика**: Подсчитывает частоту встречаемости каждого слова в тексте
- **Обработка текста**:
  1. Привести весь текст к нижнему регистру (`.lower()`)
  2. Разделить текст на слова по пробелам и знакам препинания
  3. Удалить пустые строки из списка слов
  4. Можно использовать `re.findall(r'\b\w+\b', text.lower())` для извлечения слов
- **Возвращаемое значение**: словарь `dict[str, int]`, где ключ - слово (в нижнем регистре), значение - количество вхождений
- **Пример**:
  - Вход: `"Python is great. Python is powerful."`
  - Выход: `{'python': 2, 'is': 2, 'great': 1, 'powerful': 1}`
- **Особенности**:
  - Регистронезависимый подсчет (Python = python = PYTHON)
  - Игнорирует знаки препинания при подсчете слов
  - Слова разделяются пробелами и знаками препинания

#### Дополнительные методы (опционально):
- `_normalize_text(self, text: str) -> str` - нормализация текста (приведение к нижнему регистру)
- `_extract_words(self, text: str) -> list[str]` - извлечение списка слов из текста

### Класс `CharacterFrequencyAnalyzer(TextAnalyzer)`

#### `analyze(self, text: str) -> dict`
- **Логика**: Подсчитывает частоту встречаемости каждого символа в тексте
- **Обработка текста**:
  1. Учитывать все символы, включая пробелы, знаки препинания, цифры
  2. Можно привести к нижнему регистру (опционально, но рекомендуется для согласованности)
  3. Итерация по каждому символу в строке
- **Возвращаемое значение**: словарь `dict[str, int]`, где ключ - символ, значение - количество вхождений
- **Пример**:
  - Вход: `"Hello, world!"`
  - Выход: `{'h': 1, 'e': 1, 'l': 3, 'o': 2, ',': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1, '!': 1}`
- **Особенности**:
  - Учитывает все символы, включая пробелы и знаки препинания
  - Регистронезависимый подсчет (рекомендуется)
  - Можно использовать `collections.Counter` для упрощения

#### Дополнительные методы (опционально):
- `_normalize_character(self, char: str) -> str` - нормализация символа

### Класс `SentenceAnalyzer(TextAnalyzer)`

#### `analyze(self, text: str) -> dict`
- **Логика**: Анализирует предложения в тексте (количество и среднюю длину)
- **Обработка текста**:
  1. Разделить текст на предложения по знакам окончания (`.`, `!`, `?`)
  2. Удалить пустые предложения
  3. Для каждого предложения посчитать количество символов (или слов)
  4. Вычислить среднюю длину предложения
- **Возвращаемое значение**: словарь с ключами:
  - `'sentence_count'` (int) - количество предложений
  - `'avg_sentence_length'` (float) - средняя длина предложения в символах
  - Опционально: `'avg_words_per_sentence'` (float) - среднее количество слов в предложении
- **Пример**:
  - Вход: `"Python is great. Python is powerful. Python is easy."`
  - Выход: `{'sentence_count': 3, 'avg_sentence_length': 16.67}` (примерно)
- **Особенности**:
  - Предложения разделяются по `.`, `!`, `?`
  - Учитывать, что точка может быть частью числа или сокращения (упрощенная версия)
  - Длина предложения = количество символов в предложении (включая пробелы)
  - Если предложений нет, вернуть `{'sentence_count': 0, 'avg_sentence_length': 0.0}`

#### Дополнительные методы (опционально):
- `_split_sentences(self, text: str) -> list[str]` - разделение текста на предложения
- `_calculate_avg_length(self, sentences: list[str]) -> float` - вычисление средней длины

**Примеры использования**:

```python
# Пример 1: Анализ частоты слов
text = "Python is great. Python is powerful. Python is easy."
analyzer1 = WordFrequencyAnalyzer()
result1 = analyzer1.analyze(text)
# result1 = {'python': 3, 'is': 3, 'great': 1, 'powerful': 1, 'easy': 1}

# Пример 2: Анализ частоты символов
analyzer2 = CharacterFrequencyAnalyzer()
result2 = analyzer2.analyze("Hello, world!")
# result2 = {'h': 1, 'e': 1, 'l': 3, 'o': 2, ',': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1, '!': 1}

# Пример 3: Анализ предложений
analyzer3 = SentenceAnalyzer()
result3 = analyzer3.analyze("First sentence. Second sentence! Third sentence?")
# result3 = {'sentence_count': 3, 'avg_sentence_length': 17.0}

# Пример 4: Полиморфизм - работа через базовый класс
analyzers: list[TextAnalyzer] = [
    WordFrequencyAnalyzer(),
    CharacterFrequencyAnalyzer(),
    SentenceAnalyzer()
]
text = "Python is great. Python is powerful."
for analyzer in analyzers:
    result = analyzer.analyze(text)
    print(f"{analyzer.__class__.__name__}: {result}")
```

**Тест-кейсы**:
```python
# Тест 1: Создание базового класса
try:
    analyzer = TextAnalyzer()
    analyzer.analyze("test")
    assert False, "Should raise NotImplementedError"
except NotImplementedError:
    pass  # Ожидаемое поведение

# Тест 2: Анализ частоты слов - базовый случай
text = "Python is great. Python is powerful. Python is easy."
analyzer1 = WordFrequencyAnalyzer()
result1 = analyzer1.analyze(text)
assert result1['python'] == 3
assert result1['is'] == 3
assert result1['great'] == 1
assert result1['powerful'] == 1
assert result1['easy'] == 1

# Тест 3: Анализ частоты слов - регистронезависимость
text2 = "Python PYTHON python"
result2 = analyzer1.analyze(text2)
assert result2['python'] == 3

# Тест 4: Анализ частоты слов - знаки препинания
text3 = "Hello, world! Hello; world."
result3 = analyzer1.analyze(text3)
assert result3['hello'] == 2
assert result3['world'] == 2

# Тест 5: Анализ частоты слов - пустой текст
result4 = analyzer1.analyze("")
assert result4 == {}

# Тест 6: Анализ частоты символов - базовый случай
analyzer2 = CharacterFrequencyAnalyzer()
text4 = "Hello, world!"
result5 = analyzer2.analyze(text4)
assert result5['h'] > 0
assert result5['e'] > 0
assert result5['l'] == 3
assert result5['o'] == 2
assert result5[','] == 1
assert result5[' '] == 1
assert result5['!'] == 1

# Тест 7: Анализ частоты символов - регистронезависимость
text5 = "Aa"
result6 = analyzer2.analyze(text5)
assert result6['a'] == 2

# Тест 8: Анализ частоты символов - все символы
text6 = "a b c 1 2 3 ! @ #"
result7 = analyzer2.analyze(text6)
assert 'a' in result7
assert '1' in result7
assert '!' in result7
assert ' ' in result7

# Тест 9: Анализ предложений - базовый случай
analyzer3 = SentenceAnalyzer()
text7 = "Python is great. Python is powerful. Python is easy."
result8 = analyzer3.analyze(text7)
assert result8['sentence_count'] == 3
assert result8['avg_sentence_length'] > 0
assert isinstance(result8['avg_sentence_length'], float)

# Тест 10: Анализ предложений - разные знаки окончания
text8 = "First sentence. Second sentence! Third sentence?"
result9 = analyzer3.analyze(text8)
assert result9['sentence_count'] == 3

# Тест 11: Анализ предложений - пустой текст
result10 = analyzer3.analyze("")
assert result10['sentence_count'] == 0
assert result10['avg_sentence_length'] == 0.0

# Тест 12: Анализ предложений - текст без предложений
result11 = analyzer3.analyze("No sentence here")
# Может быть 0 или 1 в зависимости от реализации (текст без точки)
assert 'sentence_count' in result11
assert 'avg_sentence_length' in result11

# Тест 13: Полиморфизм - работа через базовый класс
analyzers = [WordFrequencyAnalyzer(), CharacterFrequencyAnalyzer(), SentenceAnalyzer()]
text9 = "Python is great. Python is powerful."
results = [a.analyze(text9) for a in analyzers]
assert len(results) == 3
assert all(isinstance(r, dict) for r in results)

# Тест 14: Полиморфизм - проверка типов результатов
word_result = results[0]
char_result = results[1]
sentence_result = results[2]
assert 'python' in word_result  # Словарь частоты слов
assert 'p' in char_result  # Словарь частоты символов
assert 'sentence_count' in sentence_result  # Словарь с метриками предложений

# Тест 15: Наследование - проверка isinstance
analyzer = WordFrequencyAnalyzer()
assert isinstance(analyzer, TextAnalyzer)
assert isinstance(analyzer, WordFrequencyAnalyzer)

# Тест 16: Комплексный тест - все анализаторы на одном тексте
text10 = "The quick brown fox. The quick brown fox jumps. The quick brown fox jumps over the lazy dog."
word_analyzer = WordFrequencyAnalyzer()
char_analyzer = CharacterFrequencyAnalyzer()
sentence_analyzer = SentenceAnalyzer()

word_result = word_analyzer.analyze(text10)
char_result = char_analyzer.analyze(text10)
sentence_result = sentence_analyzer.analyze(text10)

assert word_result['the'] == 3
assert word_result['quick'] == 3
assert 't' in char_result
assert sentence_result['sentence_count'] == 3
assert sentence_result['avg_sentence_length'] > 0

# Тест 17: Граничный случай - одно слово
text11 = "Python"
result12 = analyzer1.analyze(text11)
assert result12['python'] == 1
assert len(result12) == 1

# Тест 18: Граничный случай - одно предложение
text12 = "One sentence."
result13 = analyzer3.analyze(text12)
assert result13['sentence_count'] == 1
assert result13['avg_sentence_length'] > 0

# Тест 19: Граничный случай - только знаки препинания
text13 = "!!! ??? ..."
result14 = analyzer1.analyze(text13)
# Результат зависит от реализации (может быть пустым словарем)
assert isinstance(result14, dict)

# Тест 20: Проверка, что результаты не изменяют исходный текст
text14 = "Original text"
analyzer1.analyze(text14)
assert text14 == "Original text"  # Исходный текст не должен измениться
```

**Выходной результат**:
- Файл `text_analyzers.py` с классами `TextAnalyzer`, `WordFrequencyAnalyzer`, `CharacterFrequencyAnalyzer`, `SentenceAnalyzer`
- Все тест-кейсы должны проходить успешно
- Код должен содержать docstrings для всех классов и методов
- Демонстрация полиморфизма в отдельном файле `demo.py` (опционально)
- Использовать аннотации типов (type hints) для всех методов

---

