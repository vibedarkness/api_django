import requests

url="http://127.0.0.1:8000/product/create/"

response=requests.post(url, json={'name':'mangue', 'content':'lorem ipsum vibe darkness mangue', 'price':'128256.23'})

print(response.json())
print(response.status_code)