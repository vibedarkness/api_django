import requests

url="http://127.0.0.1:8000/product/"

response=requests.post(url, json={'name':'melon', 'content':'lorem ipsum vibe darkness', 'price':'1237.23'})

print(response.json())
print(response.status_code)

#HTTP REQUEST --->HTML
#REST API HTTP ---->JSON 
  
