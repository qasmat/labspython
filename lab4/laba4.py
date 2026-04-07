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