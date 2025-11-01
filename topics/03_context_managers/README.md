# Контекстные менеджеры (Context Managers)

**Почему важно**: Вы уже используете `with`, но можете создавать свои для управления ресурсами.

**Что изучать**:
- Протокол контекстных менеджеров (`__enter__`, `__exit__`)
- `contextlib.contextmanager` декоратор
- Использование с `@contextmanager`
- Обработка исключений в контекстных менеджерах

**Материалы**:
- **Real Python - Context Managers**: https://realpython.com/python-with-statement/
- **Python.org - contextlib**: https://docs.python.org/3/library/contextlib.html

---

## Задача 3.1: Контекстные менеджеры

**Описание**: Создать кастомные контекстные менеджеры для управления ресурсами.

**Технические требования**:
- Контекстный менеджер `Timer` - измеряет время выполнения блока кода
- Контекстный менеджер `ChangeDirectory(path)` - временно меняет рабочую директорию
- Контекстный менеджер `SuppressExceptions(*exceptions)` - подавляет указанные исключения

**Тест-кейсы**:
```python
# Тест 1: Измерение времени
with Timer() as t:
    time.sleep(0.1)
assert t.elapsed_time > 0.09
assert t.elapsed_time < 0.15

# Тест 2: Временная смена директории
import os
original_dir = os.getcwd()
new_dir = "/tmp"  # или другая существующая директория

with ChangeDirectory(new_dir):
    assert os.getcwd() == new_dir

assert os.getcwd() == original_dir  # вернулись обратно

# Тест 3: Подавление исключений
with SuppressExceptions(ValueError, TypeError):
    raise ValueError("This should be suppressed")

# Если исключение не подавляется, должно быть поднято
try:
    with SuppressExceptions(ValueError):
        raise KeyError("This should not be suppressed")
except KeyError:
    pass  # Ожидаемое поведение
```

**Выходной результат**:
- Файл `context_managers.py` с контекстными менеджерами
- Файл `test_context_managers.py` с тестами
- Все тест-кейсы должны проходить

---

