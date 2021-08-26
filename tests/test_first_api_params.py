import pytest
import requests


class TestFirstApi:
    names = [
        ("Anna"),
        ("Polina"),
        ("")
    ]

    @pytest.mark.parametrize('name', names)
    def test_hello_call(self, name):
        url = "https://playground.learnqa.ru/api/hello"
        data = {'name': name}

        responce = requests.get(url, params=data)

        code = responce.status_code

        assert code == 200, f"Wrong responce code - {code}"

        responce_dict = responce.json()
        assert "answer" in responce_dict, "There is no field 'answer' in the responce"

        if len(name) == 0:
            expected_responce_text = "Hello, someone"
        else:
            expected_responce_text = f"Hello, {name}"

        actual_responce_text = responce_dict["answer"]
        assert actual_responce_text == expected_responce_text, "Actual text in the responce is not correct"
