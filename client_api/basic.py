import requests

url="http://127.0.0.1:8000/product/"

response=requests.get(url)

print(response.json())
print(response.status_code)

#HTTP REQUEST --->HTML
#REST API HTTP ---->JSON 
  
