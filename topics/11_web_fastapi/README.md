# Веб-разработка (FastAPI)

**Почему важно**: Создание веб-приложений и API - популярное направление.

**Что изучать**:
- **FastAPI** (современный, быстрый)
- Роутинг и обработка запросов
- Валидация запросов и ответов (Pydantic)
- REST API разработка
- Документация API (автоматически)
- Деплой приложений

**Материалы**:
- **FastAPI Tutorial**: https://fastapi.tiangolo.com/tutorial/
- **Real Python - FastAPI**: https://realpython.com/fastapi-python-web-apis/

---

## Задача 11.1: REST API с FastAPI

**Описание**: Создать REST API для анализа текста с использованием FastAPI.

**Технические требования**:
- Endpoint `POST /analyze` - принимает текст, возвращает анализ
- Endpoint `GET /analyses` - список всех анализов
- Endpoint `GET /analyses/{id}` - конкретный анализ
- Использовать Pydantic модели для валидации запросов/ответов
- Интеграция с БД (SQLAlchemy)
- Документация API (автоматически через FastAPI)

**Тест-кейсы**:
```python
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

# Тест 1: Анализ текста
response = client.post("/analyze", json={"text": "Python is great"})
assert response.status_code == 200
data = response.json()
assert "word_count" in data
assert data["word_count"] == 3

# Тест 2: Получение списка анализов
response = client.get("/analyses")
assert response.status_code == 200
assert isinstance(response.json(), list)

# Тест 3: Получение конкретного анализа
# Сначала создать анализ
create_response = client.post("/analyze", json={"text": "Test"})
analysis_id = create_response.json()["id"]

# Получить анализ по ID
response = client.get(f"/analyses/{analysis_id}")
assert response.status_code == 200
assert response.json()["word_count"] > 0

# Тест 4: Валидация входных данных
response = client.post("/analyze", json={})
assert response.status_code == 422  # Validation error

# Тест 5: Несуществующий анализ
response = client.get("/analyses/99999")
assert response.status_code == 404
```

**Выходной результат**:
- Файл `main.py` с FastAPI приложением
- Файл `api_routes.py` с роутами
- Файл `test_api_integration.py` с интеграционными тестами
- Запущенное API на `http://localhost:8000`
- Документация доступна на `http://localhost:8000/docs`
- Все тесты должны проходить

---

