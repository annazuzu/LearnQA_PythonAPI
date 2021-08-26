import requests

url = "https://playground.learnqa.ru/ajax/api/compare_query_type?method="
a = ["GET", "POST", "PUT", "DELETE", "HEAD"]

for i in range(5):
    if i == 0:
        for elem in a:
            resp = requests.get(url + elem)
            print("GET: " + resp.text + " method=" + elem)
    elif i == 1:
        for elem in a:
            resp = requests.post(url + elem)
            print("POST: " + resp.text + " method=" + elem)
    elif i == 2:
        for elem in a:
            resp = requests.put(url + elem)
            print("PUT: " + resp.text + " method=" + elem)
    elif i == 3:
        for elem in a:
            resp = requests.delete(url + elem)
            print("DELETE: " + resp.text + " method=" + elem)
    elif i == 4:
        for elem in a:
            resp = requests.head(url + elem)
            print("HEAD: " + resp.text + " " + elem)