# Декораторы и генераторы

**Почему важно**: Это мощные инструменты Python для расширения функциональности и работы с большими данными.

**Что изучать**:
- Функции как объекты первого класса
- Замыкания (closures)
- Декораторы (простые и с параметрами)
- Декораторы классов
- Генераторы и генераторные выражения
- Итераторы (протокол итерации)
- `yield` vs `return`

**Материалы**:
- **Real Python - Decorators**: https://realpython.com/primer-on-python-decorators/
- **Real Python - Generators**: https://realpython.com/introduction-to-python-generators/
- **Python.org - Iterator Protocol**: https://docs.python.org/3/glossary.html#term-iterator

---

## Задача 2.1: Декораторы для логирования и кэширования

**Описание**: Создать декораторы для измерения времени выполнения и кэширования результатов функций.

**Технические требования**:
- Декоратор `@timing` - выводит время выполнения функции
- Декоратор `@cache_result` - кэширует результаты функции (мемоизация)
- Декоратор `@retry(max_attempts=3)` - повторяет выполнение при ошибке

**Тест-кейсы**:
```python
# Тест 1: Декоратор времени выполнения
@timing
def slow_function(n):
    time.sleep(0.1)
    return n * 2

result = slow_function(5)
# Должен вывести время выполнения
assert result == 10

# Тест 2: Кэширование результатов
call_count = 0

@cache_result
def expensive_calculation(n):
    global call_count
    call_count += 1
    return n ** 2

result1 = expensive_calculation(5)
result2 = expensive_calculation(5)
assert result1 == result2 == 25
assert call_count == 1  # функция вызвана только один раз

# Тест 3: Повтор при ошибке
attempts = 0

@retry(max_attempts=3)
def unreliable_function():
    global attempts
    attempts += 1
    if attempts < 3:
        raise ValueError("Error")
    return "Success"

result = unreliable_function()
assert result == "Success"
assert attempts == 3
```

**Выходной результат**:
- Файл `decorators.py` с тремя декораторами
- Файл `test_decorators.py` с тестами
- Все тест-кейсы должны проходить

---

## Задача 2.2: Генераторы для обработки данных

**Описание**: Создать генераторы для обработки больших объемов данных без загрузки в память.

**Технические требования**:
- Генератор `number_range(start, stop, step)` - генерирует числа в диапазоне
- Генератор `fibonacci(n)` - первые n чисел Фибоначчи
- Генератор `read_large_file(filepath, chunk_size=1024)` - читает файл по частям
- Генератор `filter_even(numbers)` - фильтрует четные числа из итерируемого объекта

**Тест-кейсы**:
```python
# Тест 1: Генератор диапазона
numbers = list(number_range(1, 10, 2))
assert numbers == [1, 3, 5, 7, 9]

# Тест 2: Генератор Фибоначчи
fib = list(fibonacci(10))
assert fib == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# Тест 3: Фильтр четных чисел
input_nums = [1, 2, 3, 4, 5, 6, 7, 8]
even_nums = list(filter_even(input_nums))
assert even_nums == [2, 4, 6, 8]

# Тест 4: Чтение большого файла по частям (создать временный файл)
import tempfile
with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
    f.write("A" * 5000)  # 5000 символов
    temp_path = f.name

chunks = list(read_large_file(temp_path, chunk_size=1000))
assert len(chunks) == 5  # 5 частей по 1000 символов
assert sum(len(chunk) for chunk in chunks) == 5000
```

**Выходной результат**:
- Файл `generators.py` с генераторами
- Файл `test_generators.py` с тестами
- Все тест-кейсы должны проходить
- Продемонстрировать экономию памяти на большом файле

---

