import time
import requests


# Декоратор: ограничивает частоту вызова функции
def rate_limit(seconds):
    def decorator(func):
        last_time = 0  # хранит время последнего вызова

        def wrapper():
            nonlocal last_time  # позволяет изменять переменную

            now = time.time()

            # если функция вызывается слишком часто — ждём
            if now - last_time < seconds:
                wait = seconds - (now - last_time)
                print(f"Ждём {round(wait, 2)} сек...")
                time.sleep(wait)

            result = func()  # вызываем исходную функцию
            last_time = time.time()  # обновляем время
            return result

        return wrapper
    return decorator


# Замыкание: сохраняет URL
def make_fetcher(url):
    def fetch():
        response = requests.get(url)
        return response.text
    return fetch


# --- использование ---

url = "https://dogapi.dog/api/v2/facts"

# создаём замыкание
fetch_data = make_fetcher(url)

# применяем декоратор к замыканию
fetch_data = rate_limit(3)(fetch_data)


# несколько вызовов подряд
for i in range(5):
    print(f"\nЗапрос {i+1}:")

    print(fetch_data())