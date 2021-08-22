import requests

url = "https://playground.learnqa.ru/ajax/api/compare_query_type"

m_GET = {"method":"GET"}
m_POST = {"method":"POST"}
m_PUT = {"method":"PUT"}
m_DELETE = {"method":"DELETE"}

responce_without_method = requests.post(url)
print(responce_without_method.text)

m_HEAD = {"method":"HEAD"}

responce_wrong_method = requests.head("https://playground.learnqa.ru/ajax/api/compare_query_type", data=m_HEAD)
print(responce_wrong_method.text)

responce1 = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params=m_GET)
responce2 = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data=m_POST)
responce3 = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", data=m_PUT)
responce4 = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", data=m_DELETE)

print(responce1.text)
print(responce2.text)
print(responce3.text)
print(responce4.text)


a = [m_GET, m_POST, m_PUT, m_DELETE, m_HEAD]

def check_method():
    for i in range(len(a)):
        if i == 0:
            for elem in a:
                resp = requests.get(url, params=elem)
                print("GET: " + resp.text + " " + str(elem))
        elif i == 1:
            for elem in a:
                resp = requests.post(url, data=elem)
                print("POST: " + resp.text + " " + str(elem))
        elif i == 2:
            for elem in a:
                resp = requests.put(url, data=elem)
                print("PUT: " + resp.text + " " + str(elem))
        elif i == 3:
            for elem in a:
                resp = requests.delete(url, data=elem)
                print("DELETE: " + resp.text + " " + str(elem))
        elif i == 4:
            for elem in a:
                resp = requests.head(url)
                print("HEAD: " + resp.text + " " + str(elem))

check_method()