# Асинхронное программирование (Async/Await)

**Почему важно**: Для эффективной работы с I/O операциями (файлы, сеть, API).

**Что изучать**:
- `asyncio` модуль
- `async def` и `await`
- Асинхронные контекстные менеджеры
- Асинхронные генераторы
- `asyncio.gather()` и конкурентность

**Материалы**:
- **Real Python - Async**: https://realpython.com/async-io-python/
- **"Python Async"** - документация: https://docs.python.org/3/library/asyncio.html

---

## Задача 9.1: Асинхронная обработка файлов

**Описание**: Создать асинхронные утилиты для работы с файлами и сетью.

**Технические требования**:
- Асинхронная функция для чтения нескольких файлов параллельно
- Асинхронная функция для обработки CSV/JSON файлов
- Асинхронный контекстный менеджер для работы с файлами
- Использование `asyncio.gather()` для параллельного выполнения

**Тест-кейсы**:
```python
import asyncio
from async_utils import async_read_files, async_process_csv

# Тест 1: Параллельное чтение файлов
async def test_async_read_files():
    file_paths = ["file1.txt", "file2.txt", "file3.txt"]
    results = await async_read_files(file_paths)
    assert len(results) == 3
    assert all(isinstance(r, str) for r in results)

# Тест 2: Асинхронная обработка CSV
async def test_async_process_csv():
    csv_file = "data.csv"
    results = await async_process_csv(csv_file)
    assert isinstance(results, list)

# Тест 3: Асинхронный контекстный менеджер
async def test_async_file_manager():
    async with AsyncFileManager("test.txt", "w") as f:
        await f.write("Test content")
    
    async with AsyncFileManager("test.txt", "r") as f:
        content = await f.read()
        assert content == "Test content"

# Тест 4: Параллельное выполнение задач
async def test_gather():
    tasks = [
        async_read_files(["file1.txt"]),
        async_read_files(["file2.txt"]),
        async_read_files(["file3.txt"])
    ]
    results = await asyncio.gather(*tasks)
    assert len(results) == 3
```

**Выходной результат**:
- Файл `async_utils.py` с асинхронными функциями
- Файл `test_async.py` с тестами
- Все тесты должны проходить
- Продемонстрировать ускорение при параллельной обработке

---

