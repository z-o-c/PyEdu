# Структурирование проекта и пакеты

**Почему важно**: Ваши лабораторные разбросаны. Нужно учиться создавать структурированные проекты.

**Что изучать**:
- Структура Python пакетов (`__init__.py`)
- `setup.py` / `pyproject.toml`
- Установка пакетов в режиме разработки (`pip install -e .`)
- Управление зависимостями (`requirements.txt`, `poetry`, `pipenv`)
- Виртуальные окружения (venv)
- Относительные и абсолютные импорты

**Материалы**:
- **Real Python - Packages**: https://realpython.com/python-application-layouts/
- **Python Packaging Guide**: https://packaging.python.org/

---

## Задача 12.1: Структурированный Python пакет

**Описание**: Организовать все предыдущие задачи в структурированный Python пакет.

**Технические требования**:
- Создать структуру пакета с `__init__.py`
- Файл `setup.py` или `pyproject.toml` для установки пакета
- Файл `requirements.txt` с зависимостями
- Настроить импорты для работы как пакет
- Создать CLI команды через `entry_points`

**Структура проекта**:
```
pyedu/
├── pyedu/
│   ├── __init__.py
│   ├── matrix/
│   │   ├── __init__.py
│   │   └── matrix.py
│   ├── analyzers/
│   │   ├── __init__.py
│   │   └── text_analyzers.py
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── decorators.py
│   │   └── generators.py
│   └── ...
├── tests/
├── setup.py
├── requirements.txt
└── README.md
```

**Тест-кейсы**:
```python
# Тест 1: Установка пакета
# pip install -e .
# Должен установиться без ошибок

# Тест 2: Импорт модулей
from pyedu.matrix import Matrix
from pyedu.analyzers import WordFrequencyAnalyzer
# Импорты должны работать

# Тест 3: CLI команды
# pyedu-analyze --text "Hello world"
# Должна выполниться команда

# Тест 4: Структура пакета
import pyedu
assert hasattr(pyedu, '__version__')
```

**Выходной результат**:
- Полная структура пакета
- Файл `setup.py` с метаданными
- Файл `requirements.txt`
- Установка через `pip install -e .` работает
- Все CLI команды доступны
- Документация в README.md

---

