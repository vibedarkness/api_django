import requests

url="http://127.0.0.1:8000/product/2/update"

response=requests.put(url, json={'name':'babane', 'content':'lorem ipsum vibe darkness papaye', 'price':'1200.23'})

print(response.json())
print(response.status_code)