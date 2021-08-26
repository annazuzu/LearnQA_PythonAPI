import requests


class TestEx11SomeCookie:
    def test_some_cookie(self):
        responce = requests.get("https://playground.learnqa.ru/api/homework_cookie")

        print(dict(responce.cookies))

        some_cookie = "HomeWork"

        assert some_cookie in responce.cookies, f"There is no {some_cookie} in the responce"
        assert "hw_value" in responce.cookies.get(some_cookie), "Cookie don't have that value"
