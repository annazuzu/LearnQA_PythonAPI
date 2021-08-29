import requests

responce = requests.get("https://playground.learnqa.ru/api/homework_header")

print(responce.headers)

some_header = "x-secret-homework-header"

print(responce.headers.get(some_header))