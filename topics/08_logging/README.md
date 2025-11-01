# Логирование (Logging)

**Почему важно**: `print()` не подходит для продакшена. Нужна система логирования.

**Что изучать**:
- Модуль `logging` (стандартная библиотека)
- Уровни логирования (DEBUG, INFO, WARNING, ERROR, CRITICAL)
- Форматирование логов
- Обработчики (handlers) - файлы, консоль
- Логирование в приложениях

**Материалы**:
- **Real Python - Logging**: https://realpython.com/python-logging/
- **Python.org - logging**: https://docs.python.org/3/library/logging.html

---

## Задача 8.1: Система логирования

**Описание**: Интегрировать систему логирования во все предыдущие модули.

**Технические требования**:
- Настроить логирование с разными уровнями (DEBUG, INFO, WARNING, ERROR)
- Создать отдельные логгеры для разных модулей
- Настроить ротацию логов (RotatingFileHandler)
- Форматирование логов с временными метками и уровнями

**Тест-кейсы**:
```python
import logging
from logging_utils import setup_logger

# Тест 1: Настройка логгера
logger = setup_logger("test_module", "test.log", level=logging.DEBUG)
logger.debug("Debug message")
logger.info("Info message")
logger.warning("Warning message")
logger.error("Error message")

# Проверить наличие записей в файле
with open("test.log", "r") as f:
    log_content = f.read()
    assert "Debug message" in log_content
    assert "Info message" in log_content
    assert "ERROR" in log_content

# Тест 2: Ротация логов (создать большой лог и проверить ротацию)
for i in range(1000):
    logger.info(f"Message {i}")

# Должны быть созданы файлы: test.log, test.log.1 и т.д.

# Тест 3: Разные логгеры для разных модулей
db_logger = setup_logger("database", "db.log")
api_logger = setup_logger("api", "api.log")

db_logger.info("Database operation")
api_logger.info("API request")

# Проверить, что сообщения идут в правильные файлы
```

**Выходной результат**:
- Файл `logging_utils.py` с функцией настройки логирования
- Обновленные предыдущие модули с логированием
- Файл `test_logging.py` с тестами
- Демонстрационный скрипт с примерами логов
- Все тесты должны проходить

---

