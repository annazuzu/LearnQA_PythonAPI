import requests

responce = requests.post("https://playground.learnqa.ru/api/get_301", allow_redirects=True)
first_responce = responce.history[0]
second_responce = responce

print(first_responce.url)
print(second_responce.url)

# ------------------------------

result = responce.history

for i in range(len(result)):
    print(result[i])
    print(result[i].url)