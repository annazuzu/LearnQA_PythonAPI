import requests

# Метод showAllHeaders - отображает все те заголовки, которые мы передаем с запросом

headers = {"some_header":"123"}
responce = requests.get("https://playground.learnqa.ru/api/show_all_headers", headers=headers)

print(responce.text)
print(responce.headers)