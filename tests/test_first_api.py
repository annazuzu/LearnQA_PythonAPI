import requests


class TestFirstApi:
    def test_hello_call(self):
        url = "https://playground.learnqa.ru/api/hello"
        name = 'Anna'
        data = {'name': name}

        responce = requests.get(url, params=data)

        code = responce.status_code

        assert code == 200, f"Wrong responce code - {code}"

        responce_dict = responce.json()
        assert "answer" in responce_dict, "There is no field 'answer' in the responce"

        expected_responce_text = f"Hello, {name}"
        actual_responce_text = responce_dict["answer"]
        assert actual_responce_text == expected_responce_text, "Actual text in the responce is not correct"
