import requests
import time
import json

responce_without_method = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job")
print(responce_without_method.text)

t_fake = {"token": "abc"}
t_real = {"token": "AOyojNyoDOwAiMy0COw0SMyAjM"}

responce_t_fake = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params=t_fake)
responce_t_real = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params=t_real)

print(responce_t_fake.text)
print(responce_t_real.text)


def get_token():
    obj = json.loads(responce_without_method.text)
    key = "token"
    str = obj[key]
    return str


print(get_token())


def get_seconds():
    global int
    obj = json.loads(responce_without_method.text)
    key = "seconds"
    int = int(obj[key])
    return int


print(get_seconds())
