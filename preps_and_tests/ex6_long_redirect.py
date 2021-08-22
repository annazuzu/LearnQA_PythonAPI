import json

import requests

responce = requests.get("https://playground.learnqa.ru/api/long_redirect")

list = responce.history
print(len(list))

for i in range(len(list)):
    print(list[i].headers)

# for i in range(len(list)):
#     print('status_code: {0} - Инициатор: {1} --> Локация: {2}'.format(list[i].status_code, list[i].url, list[i].headers.get('Location')))

for i in range(len(list)):
    print(list[i].url)