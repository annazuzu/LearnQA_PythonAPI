import requests

responce = requests.get("https://playground.learnqa.ru/api/homework_cookie")

print(dict(responce.cookies))

print(responce.cookies.get("HomeWork"))