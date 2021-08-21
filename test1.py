import requests

m_GET = {"method":"GET"}
m_POST = {"method":"POST"}
m_PUT = {"method":"PUT"}
m_DELETE = {"method":"DELETE"}
m_HEAD = {"method":"HEAD"}
m_OPTIONS = {"method":"OPTIONS"}
m_PATCH = {"method":"PATCH"}

url = "https://playground.learnqa.ru/ajax/api/compare_query_type"
a = [m_GET, m_POST, m_PUT, m_DELETE, m_HEAD, m_OPTIONS, m_PATCH]

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
    elif i == 5:
        for elem in a:
            resp = requests.options(url, data=elem)
            print("OPTIONS: " + resp.text + " " + str(elem))
    elif i == 6:
        for elem in a:
            resp = requests.patch(url, data=elem)
            print("PATCH: " + resp.text + " " + str(elem))