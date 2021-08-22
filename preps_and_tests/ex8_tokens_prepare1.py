import requests
import json
import time

responce_without_method = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job")

obj = json.loads(responce_without_method.text)


def get_token(obj_str):
    key = "token"
    s = obj_str[key]
    return s


print(get_token(obj))


def get_seconds(obj_str):
    global i
    key = "seconds"
    i = int(obj_str[key])
    return i


print(get_seconds(obj))

t_real = {"token": get_token(obj)}

responce_t_real_before = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params=t_real)

print(responce_t_real_before.text)


def get_status(obj_str):
    key = "status"
    s = obj_str[key]
    return s

def get_result(obj_str):
    key = "result"
    s = obj_str[key]
    return s


if get_status(json.loads(responce_t_real_before.text)) == "Job is NOT ready":
    time.sleep(get_seconds(obj))

responce_t_real_after = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params=t_real)

obj2 = json.loads(responce_t_real_after.text)

if get_status(obj2) == "Job is ready" and get_status(obj2) != "":
    print(get_status(obj2) + " " + get_result(obj2))
    print("Done!")

