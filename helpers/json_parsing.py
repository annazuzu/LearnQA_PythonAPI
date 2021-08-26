import json

str_as_json_format = '{"answer": "Hello, User"}'
obj = json.loads(str_as_json_format)

key = "answer"

if key in obj:
    print(obj[key])
else:
    print(f"Ключа {key} в JSON нет")