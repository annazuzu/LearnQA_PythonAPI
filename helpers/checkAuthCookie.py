import requests

payload = {"login":"secret_login", "password":"secret_pass"}
responce1 = requests.post("https://playground.learnqa.ru/api/get_auth_cookie", data=payload)

# Из запроса нам интересна только строка с именем 'auth_cookie'. Возьмем только её:
cookie_value = responce1.cookies.get('auth_cookie')

# создаем пустой массив:
cookies = {}

# если логин-пароль верные и авторизация успешна:
if cookie_value is not None:
    cookies.update({'auth_cookie': cookie_value})

responce2 = requests.post("https://playground.learnqa.ru/api/check_auth_cookie", cookies=cookies)

print(dict(responce1.cookies))
print(responce2.text)