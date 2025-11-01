# Работа с базами данных

**Почему важно**: Большинство приложений работают с базами данных. SQLite - отличный старт.

**Что изучать**:
- SQL основы (SELECT, INSERT, UPDATE, DELETE, JOIN)
- Модуль `sqlite3` (встроенная БД)
- ORM: SQLAlchemy или Peewee
- Миграции баз данных
- Работа с транзакциями

**Материалы**:
- **Real Python - SQLite**: https://realpython.com/python-sqlite-sqlalchemy/
- **SQLAlchemy Tutorial**: https://docs.sqlalchemy.org/en/20/tutorial/
- **SQLite Tutorial**: https://www.sqlitetutorial.net/

---

## Задача 6.1: Система хранения данных в SQLite

**Описание**: Создать систему для хранения и управления данными анализа текста в SQLite.

**Технические требования**:
- Создать БД с таблицами: `texts`, `analyses`, `word_frequencies`
- Класс `TextDatabase` для работы с БД (CRUD операции)
- Методы: `save_text()`, `save_analysis()`, `get_text_by_id()`, `get_analyses_by_date_range()`
- Использовать транзакции для целостности данных

**Тест-кейсы**:
```python
import sqlite3
from text_database import TextDatabase

# Тест 1: Создание БД и таблиц
db = TextDatabase("test.db")
assert db.connection is not None

# Тест 2: Сохранение текста
text_id = db.save_text("Python is great", "test.txt")
assert text_id > 0

# Тест 3: Получение текста по ID
text = db.get_text_by_id(text_id)
assert text['content'] == "Python is great"
assert text['filename'] == "test.txt"

# Тест 4: Сохранение анализа
analysis_id = db.save_analysis(text_id, {'word_count': 3, 'char_count': 15})
assert analysis_id > 0

# Тест 5: Поиск по диапазону дат
from datetime import datetime, timedelta
start_date = datetime.now() - timedelta(days=7)
end_date = datetime.now()
analyses = db.get_analyses_by_date_range(start_date, end_date)
assert len(analyses) > 0

# Тест 6: Сохранение частотности слов
db.save_word_frequencies(text_id, {'python': 1, 'is': 1, 'great': 1})
frequencies = db.get_word_frequencies(text_id)
assert frequencies['python'] == 1
```

**Выходной результат**:
- Файл `text_database.py` с классом `TextDatabase`
- Файл `schema.sql` с SQL схемой БД
- Файл `test_database.py` с тестами
- Демонстрационный скрипт `demo_database.py`
- Все тесты должны проходить

---

## Задача 6.2: ORM с SQLAlchemy

**Описание**: Переписать предыдущую задачу с использованием SQLAlchemy ORM.

**Технические требования**:
- Определить модели: `Text`, `Analysis`, `WordFrequency`
- Настроить связи между моделями (relationships)
- Создать сессию для работы с БД
- Реализовать те же методы через ORM

**Тест-кейсы**:
```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Text, Analysis, WordFrequency, Base

# Тест 1: Создание сессии
engine = create_engine('sqlite:///test_orm.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Тест 2: Создание текста через ORM
text = Text(content="Python is great", filename="test.txt")
session.add(text)
session.commit()
assert text.id > 0

# Тест 3: Создание анализа с связью
analysis = Analysis(text_id=text.id, word_count=3, char_count=15)
session.add(analysis)
session.commit()
assert analysis.id > 0
assert analysis.text.content == "Python is great"

# Тест 4: Запросы через ORM
texts = session.query(Text).filter(Text.filename == "test.txt").all()
assert len(texts) == 1

# Тест 5: Сложный запрос с join
results = session.query(Text, Analysis).join(Analysis).all()
assert len(results) > 0
```

**Выходной результат**:
- Файл `models.py` с моделями SQLAlchemy
- Файл `database_orm.py` с функциями для работы с БД
- Файл `test_orm.py` с тестами
- Все тесты должны проходить

---

