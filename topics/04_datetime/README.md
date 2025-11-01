# Работа с датами и временем

**Почему важно**: Часто требуется в реальных проектах для логирования, анализа данных, планирования задач.

**Что изучать**:
- Модуль `datetime`
- Форматирование дат и времени (`strftime`, `strptime`)
- Работа с временными зонами (`pytz` или `zoneinfo`)
- `timedelta` для арифметики с датами
- Парсинг дат из различных форматов

**Материалы**:
- **Real Python - DateTime**: https://realpython.com/python-datetime/
- **Python.org - datetime**: https://docs.python.org/3/library/datetime.html

---

## Задача 4.1: Работа с датами и временем

**Описание**: Создать утилиты для работы с датами и временем.

**Технические требования**:
- Функция `parse_date(date_string)` - парсит дату из различных форматов
- Функция `date_range(start_date, end_date)` - генерирует даты в диапазоне
- Функция `format_date(date, format_string)` - форматирует дату
- Класс `DateCalculator` - вычисляет разницу между датами, добавляет дни/месяцы/годы

**Тест-кейсы**:
```python
from datetime import datetime

# Тест 1: Парсинг даты
date1 = parse_date("2024-01-15")
date2 = parse_date("15/01/2024")
date3 = parse_date("January 15, 2024")
assert all(isinstance(d, datetime) for d in [date1, date2, date3])

# Тест 2: Диапазон дат
start = datetime(2024, 1, 1)
end = datetime(2024, 1, 5)
dates = list(date_range(start, end))
assert len(dates) == 5
assert dates[0] == start
assert dates[-1] == end

# Тест 3: Форматирование даты
date = datetime(2024, 1, 15)
formatted = format_date(date, "%Y-%m-%d")
assert formatted == "2024-01-15"

# Тест 4: Калькулятор дат
calc = DateCalculator()
date = datetime(2024, 1, 15)
new_date = calc.add_days(date, 10)
assert new_date.day == 25

diff = calc.difference_days(date, new_date)
assert diff == 10

# Тест 5: Добавление месяцев (учитывать разную длину месяцев)
date = datetime(2024, 1, 31)
new_date = calc.add_months(date, 1)
assert new_date.month == 2
# 31 января + 1 месяц = 29 февраля (2024 - високосный)
```

**Выходной результат**:
- Файл `date_utils.py` с функциями и классом
- Файл `test_date_utils.py` с тестами
- Все тест-кейсы должны проходить
- CLI-скрипт `date_tool.py` для демонстрации работы

---

