# Работа с HTTP и API

**Почему важно**: Большинство современных приложений взаимодействуют с веб-сервисами.

**Что изучать**:
- Модуль `requests` для HTTP запросов
- REST API основы
- Парсинг JSON ответов
- Обработка ошибок HTTP
- Аутентификация (API keys, OAuth)
- Библиотека `httpx` (асинхронная альтернатива)

**Материалы**:
- **Real Python - requests**: https://realpython.com/python-requests/
- **Requests документация**: https://requests.readthedocs.io/
- **HTTPX документация**: https://www.python-httpx.org/

---

## Задача 10.1: Работа с HTTP API

**Описание**: Создать утилиты для работы с HTTP API и обработки ответов.

**Технические требования**:
- Класс `APIClient` для работы с REST API
- Методы: `get()`, `post()`, `put()`, `delete()`
- Обработка ошибок HTTP
- Поддержка аутентификации через API ключ
- Класс `WeatherAPI` для работы с OpenWeatherMap API (или другой публичный API)

**Тест-кейсы**:
```python
from api_client import APIClient
from weather_api import WeatherAPI

# Тест 1: GET запрос
client = APIClient(base_url="https://jsonplaceholder.typicode.com")
response = client.get("/posts/1")
assert response.status_code == 200
assert "title" in response.json()

# Тест 2: POST запрос
data = {"title": "Test", "body": "Test body", "userId": 1}
response = client.post("/posts", data=data)
assert response.status_code == 201
assert response.json()["title"] == "Test"

# Тест 3: Обработка ошибок
try:
    client.get("/nonexistent")
except HTTPError as e:
    assert e.status_code == 404

# Тест 4: API с аутентификацией
weather = WeatherAPI(api_key="test_key")
# Мокировать запрос для теста
weather_data = weather.get_weather("London")
assert "temperature" in weather_data or "temp" in weather_data

# Тест 5: Кэширование запросов
# Первый запрос
weather.get_weather("London")
# Второй запрос должен использовать кэш
# Проверить, что запрос не отправляется повторно
```

**Выходной результат**:
- Файл `api_client.py` с базовым клиентом
- Файл `weather_api.py` с примером использования
- Файл `test_api.py` с тестами (использовать моки для HTTP запросов)
- Все тесты должны проходить

---

