import pytest
import requests


class TestUserAuth:
    def test_auth_user(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }

        # Первый запрос:
        responce1 = requests.post("https://playground.learnqa.ru/api/user/login", data=data)

        assert "auth_sid" in responce1.cookies, "There is no auth cookie in the responce"
        assert "x-csrf-token" in responce1.headers, "There is no CSRF token header in the responce"
        assert "user_id" in responce1.json(), "There is no user id in the responce"

        auth_sid = responce1.cookies.get("auth_sid")
        token = responce1.headers.get("x-csrf-token")
        user_id_from_auth_method = responce1.json()["user_id"]

        # Второй запрос:

        responce2 = requests.get(
            "https://playground.learnqa.ru/api/user/auth",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )

        assert "user_id" in responce2.json(), "There is no user id in the second responce"
        user_id_from_check_method = responce2.json()["user_id"]

        assert user_id_from_auth_method == user_id_from_check_method, "User id in auth method is not equal to user id from check method"

    exclude_params = [
        ("no_cookie"),
        ("no_token")
    ]

    @pytest.mark.parametrize('condition', exclude_params)
    def test_negative_auth_check(self, condition):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }

        # Первый запрос:
        responce1 = requests.post("https://playground.learnqa.ru/api/user/login", data=data)

        assert "auth_sid" in responce1.cookies, "There is no auth cookie in the responce"
        assert "x-csrf-token" in responce1.headers, "There is no CSRF token header in the responce"
        assert "user_id" in responce1.json(), "There is no user id in the responce"

        auth_sid = responce1.cookies.get("auth_sid")
        token = responce1.headers.get("x-csrf-token")

        if condition == "no_cookie":
            responce2 = requests.get(
                "https://playground.learnqa.ru/api/user/auth",
                headers={"x-csrf-token": token},

            )
        else:
            responce2 = requests.get(
                "https://playground.learnqa.ru/api/user/auth",
                cookies={"auth_sid": auth_sid},
            )

        assert "user_id" in responce1.json(), "There is no user id in the second responce"

        user_id_from_check_method = responce2.json()["user_id"]

        assert user_id_from_check_method == 0, f"User is authorized with condition {condition}"
