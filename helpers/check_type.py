import requests

responce = requests.post("https://playground.learnqa.ru/api/get_301", allow_redirects=True)
first_responce = responce.history[0]
second_responce = responce

print(first_responce.url)
print(second_responce.url)