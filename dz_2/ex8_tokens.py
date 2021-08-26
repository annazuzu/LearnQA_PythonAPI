import requests
import json
import time

responce_without_method = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job")

obj = json.loads(responce_without_method.text)


# "t" for "token", "s" for "status", "r" for "result"
def get_str_value(obj_str, keyword):
    key = ""
    if keyword == "t":
        key = "token"
    if keyword == "s":
        key = "status"
    if keyword == "r":
        key = "result"
    s = obj_str[key]
    return s


def get_seconds(obj_str):
    global i
    key = "seconds"
    i = int(obj_str[key])
    return i


t_real = {"token": get_str_value(obj, "t")}

responce_t_real_before = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params=t_real)

print(get_str_value(json.loads(responce_t_real_before.text), "s") + ". Please, wait " + str(
    get_seconds(obj)) + " seconds")

if get_str_value(json.loads(responce_t_real_before.text), "s") == "Job is NOT ready":
    time.sleep(get_seconds(obj))

responce_t_real_after = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params=t_real)

obj2 = json.loads(responce_t_real_after.text)

if get_str_value(obj2, "s") == "Job is ready" and get_str_value(obj2, "r") != "":
    print(get_str_value(obj2, "s") + " " + get_str_value(obj2, "r"))
    print("Done! Spending time: " + str(get_seconds(obj)))
