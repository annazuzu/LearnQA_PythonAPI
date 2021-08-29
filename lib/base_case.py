import json

from requests import Response

class BaseCase:
    def get_cookie (self, response: Response, cookie_name):
        assert cookie_name in response.cookies, f"Cannot find cookie with name {cookie_name} in the last responce"
        return response.cookies[cookie_name]

    def get_header (self, response: Response, headers_name):
        assert headers_name in response.headers, f"Cannot find header with name {headers_name} in the last responce"
        return response.headers[headers_name]

    def get_json_value (self, response: Response, name):
        try:
            responce_as_dict = response.json()
        except json.decoder.JSONDecodeError:
            assert False, f"Responce is not JSON format. Responce text is '{response.text}'"

        assert name in responce_as_dict, f"Responce JSON doesn't have key '{name}'"

        return responce_as_dict[name]

