Задание 1.py

### Задание:Замыкание для получение текста ответа на запрос к API.
```python
import requests


# Замыкание: функция запоминает URL API
def make_fetcher(url):
    def fetch():
        # выполняем запрос к API
        return requests.get(url).json()["data"][0]["attributes"]["body"]
    return fetch  # возвращаем внутреннюю функцию


# --- использование ---

url = "https://dogapi.dog/api/v2/facts"

# создаём функцию с "запомненным" URL
fetch_data = make_fetcher(url)

# вызываем функцию
print(fetch_data())
```
### Результат программы
<img width="1041" height="37" alt="image" src="https://github.com/user-attachments/assets/6970ddf5-0f2c-4a1b-be59-09567454fbd9" />


ЗАДАНИЕ 02.py
### Задание: Декоратор, ограничивающий частоту вызовов функций.
```python
import time  # модуль для работы со временем
import requests  # модуль для HTTP-запросов


# декоратор для ограничения частоты вызова
def rate_limit(seconds):  # seconds — интервал между вызовами
    def decorator(func):  # принимает функцию
        last_time = 0  # время последнего вызова

        def wrapper(*args, **kwargs):  # обёртка вокруг функции
            nonlocal last_time  # используем переменную из внешней области

            now = time.time()  # текущее время

            if now - last_time < seconds:  # если прошло мало времени
                print("Слишком частый вызов!")
                return

            last_time = now  # обновляем время вызова
            return func(*args, **kwargs)  # вызываем исходную функцию

        return wrapper  # возвращаем обёртку
    return decorator  # возвращаем декоратор


# замыкание: сохраняет URL
@rate_limit(5)
def make_fetcher(url):  # url передаётся один раз

  
    def fetch():  # внутренняя функция
        return requests.get(url).json()["data"][0]["attributes"]["body"] # отправляем запрос и берём текст

    return fetch  # возвращаем функцию с запомненным url





for i in range(5):  # цикл 5 раз
    print(f"\nЗапрос {i+1}:")  # вывод номера запроса
    print(make_fetcher("https://dogapi.dog/api/v2/facts"))  # вызываем функцию
```

### Результат программы

<img width="766" height="283" alt="image" src="https://github.com/user-attachments/assets/f1e23f21-69d7-40f8-9a6e-c32dfb7d9af1" />


##### Используемые материалы:

[Вложенные циклы Python](https://yandex.ru/video/preview/17052291634513813706?from=tabbar&parent-reqid=1773922417081846-14805252268414880922-balancer-l7leveler-kubr-yp-sas-21-BAL&text=вложенные+циклы+питон)

[Декораторы в Python](https://yandex.ru/video/preview/6155281460364812183?from=tabbar&parent-reqid=1773922469179096-11522774978742181951-balancer-l7leveler-kubr-yp-sas-21-BAL&reqid=1773922463487838-8967401134685398025-balancer-l7leveler-kubr-yp-sas-21-BAL&suggest_reqid=252038585173062242124634353451251&text=декоратор+питон)

