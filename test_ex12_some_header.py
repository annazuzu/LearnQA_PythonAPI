import requests


class TestEx12SomeHeader:
    def test_some_header(self):
        responce = requests.get("https://playground.learnqa.ru/api/homework_header")

        print(responce.headers)

        some_header = "x-secret-homework-header"

        assert some_header in responce.headers, f"There is no {some_header} header in the responce"

        assert "Some secret value" in responce.headers.get(some_header), f"{some_header} don't have that value"
