import pytest
import requests


class TestEx13UserAgent:
    user_agents = [
        "Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
        "Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 "
        "Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0",
        "Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
    ]

    expected_values = [
        {'platform': 'Mobile', 'browser': 'No', 'device': 'Android'},
        {'platform': 'Mobile', 'browser': 'Chrome', 'device': 'iOS'},
        {'platform': 'Googlebot', 'browser': 'Unknown', 'device': 'Unknown'},
        {'platform': 'Web', 'browser': 'Chrome', 'device': 'No'},
        {'platform': 'Mobile', 'browser': 'No', 'device': 'iPhone'}
    ]

    testdata = [
        (user_agents[0], expected_values[0]['platform'], expected_values[0]['browser'], expected_values[0]['device']),
        (user_agents[1], expected_values[1]['platform'], expected_values[1]['browser'], expected_values[1]['device']),
        (user_agents[2], expected_values[2]['platform'], expected_values[2]['browser'], expected_values[2]['device']),
        (user_agents[3], expected_values[3]['platform'], expected_values[3]['browser'], expected_values[3]['device']),
        (user_agents[4], expected_values[4]['platform'], expected_values[4]['browser'], expected_values[4]['device'])
    ]

    def assertation_message(self, actual_value, expected_value, value):
        return f"Actual {value} {actual_value} is not equal to expected {value} {expected_value}"

    @pytest.mark.parametrize('user_agent, expected_platform, expected_browser, expected_device', testdata,
                             ids=[1, 2, 3, 4, 5])
    def test_responce_user_agent(self, user_agent, expected_platform, expected_browser, expected_device):
        headers = {"User-Agent": user_agent}

        responce = requests.get("https://playground.learnqa.ru/ajax/api/user_agent_check", headers=headers)

        code = responce.status_code
        assert code == 200, f"Wrong responce code - {code}"

        responce_dict = responce.json()

        assert "platform" in responce_dict, "There is no field 'platform' in the responce"
        assert "browser" in responce_dict, "There is no field 'browser' in the responce"
        assert "device" in responce_dict, "There is no field 'device' in the responce"

        actual_platform = responce_dict["platform"]
        actual_browser = responce_dict["browser"]
        actual_device = responce_dict["device"]

        print("actual_platform: " + actual_platform)
        print("actual_browser: " + actual_browser)
        print("actual_device: " + actual_device)

        # Делаем так, чтобы AssertionError не выбивал из теста при первом несоответствии и тест фиксировал все:
        errors = []

        if not actual_platform == expected_platform:
            errors.append(self.assertation_message(actual_platform, expected_platform, "platform"))
        if not actual_browser == expected_browser:
            errors.append(self.assertation_message(actual_browser, expected_browser, "browser"))
        if not actual_device == expected_device:
            errors.append(self.assertation_message(actual_device, expected_device, "device"))

        # нет сообщений об ошибках. Если есть, то прокинуть AssertionError и вывести все сообщения:
        assert not errors, "errors occured:\n{}".format("\n".join(errors))
