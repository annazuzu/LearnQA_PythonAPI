import requests

responce = requests.get("https://playground.learnqa.ru/api/long_redirect")

list = responce.history
print(len(list))

for i in range(len(list)):
    print('{0} - {1}'.format(list[i].status_code, list[i].url))