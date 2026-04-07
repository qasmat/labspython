Задание 1.py

### Задание:Замыкание для получение текста ответа на запрос к API.
```python
import requests

# Замыкание: функция запоминает URL API
def make_fetcher(url):
    def fetch():
        # выполняем запрос к API
        response = requests.get(url)
        return response.text  # возвращаем текст ответа
    return fetch  # возвращаем внутреннюю функцию


# --- использование ---

url = "https://dogapi.dog/api/v2/facts"

# создаём функцию с "запомненным" URL
fetch_data = make_fetcher(url)

# вызываем функцию
print(fetch_data())
```
### Результат программы
<img width="1110" height="38" alt="image" src="https://github.com/user-attachments/assets/1848539d-83dc-4441-a0b4-5a879e80ff17" />

ЗАДАНИЕ 02.py
### Задание: Декоратор, ограничивающий частоту вызовов функций.
```python
import time  # модуль для работы со временем
import requests  # модуль для HTTP-запросов


# декоратор для ограничения частоты вызова
def rate_limit(seconds):  # seconds — интервал между вызовами
    def decorator(func):  # принимает функцию
        last_time = 0  # время последнего вызова

        def wrapper():  # обёртка вокруг функции
            nonlocal last_time  # используем переменную из внешней области

            now = time.time()  # текущее время

            if now - last_time < seconds:  # если прошло мало времени
                time.sleep(seconds - (now - last_time))  # ждём

            last_time = time.time()  # обновляем время вызова
            return func()  # вызываем исходную функцию

        return wrapper  # возвращаем обёртку
    return decorator  # возвращаем декоратор


# замыкание: сохраняет URL
def make_fetcher(url):  # url передаётся один раз

    @rate_limit(3)  # применяем декоратор (не чаще 1 раза в 3 сек)
    def fetch():  # внутренняя функция
        return requests.get(url).text  # отправляем запрос и берём текст

    return fetch  # возвращаем функцию с запомненным url


# создаём функцию для API
fetch_data = make_fetcher("https://dogapi.dog/api/v2/facts")  # создаём замыкание


for i in range(5):  # цикл 5 раз
    print(f"\nЗапрос {i+1}:")  # вывод номера запроса
    print(fetch_data())  # вызываем функцию
```

### Результат программы

<img width="1729" height="285" alt="image" src="https://github.com/user-attachments/assets/838f16e9-728f-41be-b746-633ccd778557" />

##### Используемые материалы:

[Вложенные циклы Python](https://yandex.ru/video/preview/17052291634513813706?from=tabbar&parent-reqid=1773922417081846-14805252268414880922-balancer-l7leveler-kubr-yp-sas-21-BAL&text=вложенные+циклы+питон)

[Декораторы в Python](https://yandex.ru/video/preview/6155281460364812183?from=tabbar&parent-reqid=1773922469179096-11522774978742181951-balancer-l7leveler-kubr-yp-sas-21-BAL&reqid=1773922463487838-8967401134685398025-balancer-l7leveler-kubr-yp-sas-21-BAL&suggest_reqid=252038585173062242124634353451251&text=декоратор+питон)

