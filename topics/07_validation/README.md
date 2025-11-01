# Валидация данных и схемы

**Почему важно**: Вы работаете с JSON/CSV, но не валидируете структуру данных. Это важно для надежности.

**Что изучать**:
- Библиотека `pydantic` (современный стандарт)
- Валидация типов и значений
- Кастомные валидаторы
- Схемы данных (Data Models)
- Валидация из JSON/CSV

**Материалы**:
- **Pydantic документация**: https://docs.pydantic.dev/
- **Real Python - Pydantic**: https://realpython.com/python-pydantic/

---

## Задача 7.1: Валидация данных с Pydantic

**Описание**: Создать систему валидации данных для различных структур.

**Технические требования**:
- Модель `TextAnalysisResult` - валидация результатов анализа текста
- Модель `CSVRow` - валидация строк CSV
- Модель `UserData` - валидация пользовательских данных (email, возраст, имя)
- Кастомные валидаторы для проверки бизнес-логики

**Тест-кейсы**:
```python
from pydantic import ValidationError
from models import TextAnalysisResult, CSVRow, UserData

# Тест 1: Валидация результатов анализа
valid_data = {
    "word_count": 100,
    "char_count": 500,
    "sentence_count": 10,
    "avg_word_length": 5.0
}
result = TextAnalysisResult(**valid_data)
assert result.word_count == 100

# Тест 2: Ошибка валидации - отрицательные значения
try:
    invalid_data = {"word_count": -10, "char_count": 500}
    TextAnalysisResult(**invalid_data)
    assert False, "Should raise ValidationError"
except ValidationError as e:
    assert "word_count" in str(e)

# Тест 3: Валидация CSV строки
csv_row = CSVRow(name="John", age=30, email="john@example.com")
assert csv_row.email == "john@example.com"

# Тест 4: Валидация email
try:
    invalid_email = UserData(name="John", age=30, email="invalid-email")
    assert False, "Should raise ValidationError"
except ValidationError:
    pass  # Ожидаемое поведение

# Тест 5: Кастомный валидатор возраста
try:
    invalid_age = UserData(name="John", age=200, email="john@example.com")
    assert False, "Should raise ValidationError"
except ValidationError:
    pass  # Возраст должен быть от 0 до 150
```

**Выходной результат**:
- Файл `validators.py` с Pydantic моделями
- Файл `test_validators.py` с тестами
- Скрипт `validate_data.py` для демонстрации
- Все тесты должны проходить

---

