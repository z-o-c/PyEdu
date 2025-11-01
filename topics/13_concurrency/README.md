# Многопоточность и многопроцессность

**Почему важно**: Для параллельной обработки данных и CPU-интенсивных задач.

**Что изучать**:
- Модуль `threading` (GIL ограничения)
- Модуль `multiprocessing`
- Очереди (`Queue`)
- Пул процессов и потоков
- Когда использовать threading vs multiprocessing vs asyncio

**Материалы**:
- **Real Python - Concurrency**: https://realpython.com/python-concurrency/
- **Python.org - threading/multiprocessing**: https://docs.python.org/3/library/threading.html

---

## Задача 13.1: Параллельная обработка данных

**Описание**: Создать систему для параллельной обработки файлов и данных.

**Технические требования**:
- Класс для многопоточной обработки файлов
- Класс для многопроцессорной обработки CSV/JSON файлов
- Использование очередей для обмена данными между процессами
- Пул процессов для параллельного выполнения задач

**Тест-кейсы**:
```python
from multiprocessing import Queue, Pool
from parallel_utils import process_files_parallel, process_data_multiprocess

# Тест 1: Многопоточная обработка файлов
def test_threading():
    file_paths = ["file1.txt", "file2.txt", "file3.txt"]
    results = process_files_parallel(file_paths, num_threads=3)
    assert len(results) == 3
    assert all(r is not None for r in results)

# Тест 2: Многопроцессорная обработка
def test_multiprocessing():
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    results = process_data_multiprocess(data, num_processes=4)
    assert len(results) == 10

# Тест 3: Использование очереди
def test_queue():
    queue = Queue()
    queue.put("item1")
    queue.put("item2")
    assert queue.get() == "item1"
    assert queue.get() == "item2"

# Тест 4: Пул процессов
def test_pool():
    def square(x):
        return x ** 2
    
    with Pool(processes=4) as pool:
        results = pool.map(square, [1, 2, 3, 4, 5])
        assert results == [1, 4, 9, 16, 25]
```

**Выходной результат**:
- Файл `parallel_utils.py` с классами для параллельной обработки
- Файл `test_parallel.py` с тестами
- Все тесты должны проходить
- Продемонстрировать ускорение при параллельной обработке

---

