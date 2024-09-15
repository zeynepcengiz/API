
import requests
import http.client

conn = http.client.HTTPSConnection("api.collectapi.com")

headers = {
    'content-type': "application/json",
    'authorization': "apikey 2PQ95s1FToH12ll21l0mdj:2Y6qFJZc7oFZYKbD9FyMl8"
    }

conn.request("GET", "/health/dutyPharmacy?ilce=%C3%87ankaya&il=Ankara", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))