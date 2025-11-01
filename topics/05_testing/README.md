# Тестирование (Testing)

**Почему важно**: Вы пишете код, но не тестируете его автоматически. Тесты критичны для надежности.

**Что изучать**:
- Модуль `unittest` (стандартная библиотека)
- `pytest` (более популярный фреймворк)
- Фикстуры (fixtures)
- Параметризованные тесты
- Моки и заглушки (mocks)
- Покрытие кода (coverage)

**Материалы**:
- **Real Python - Testing**: https://realpython.com/python-testing/
- **pytest документация**: https://docs.pytest.org/
- **"Python Testing with pytest"** by Brian Okken

---

## Задача 5.1: Написание тестов с pytest

**Описание**: Написать полный набор тестов для всех предыдущих задач с использованием pytest.

**Технические требования**:
- Для каждой задачи из Месяца 1 создать файл тестов
- Использовать фикстуры (fixtures) для подготовки данных
- Параметризованные тесты для проверки множества входных данных
- Использовать моки (mocks) для тестирования внешних зависимостей
- Достичь покрытия кода >80%

**Тест-кейсы**:
```python
# Пример структуры тестов для Matrix
import pytest
from matrix import Matrix

@pytest.fixture
def sample_matrix():
    return Matrix([[1, 2], [3, 4]])

@pytest.mark.parametrize("data,expected", [
    ([[1, 2], [3, 4]], [[2, 4], [6, 8]]),
    ([[0, 0], [0, 0]], [[0, 0], [0, 0]]),
])
def test_matrix_multiply_by_scalar(sample_matrix, data, expected):
    matrix = Matrix(data)
    result = matrix * 2
    assert result.data == expected

def test_matrix_determinant(sample_matrix):
    assert sample_matrix.determinant() == -2
```

**Выходной результат**:
- Папка `tests/` со всеми тестовыми файлами
- Файл `pytest.ini` с настройками
- Файл `requirements.txt` с зависимостями (pytest, pytest-cov)
- Отчет о покрытии кода: `pytest --cov=. --cov-report=html`
- Все тесты должны проходить: `pytest tests/`

---

