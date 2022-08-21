import requests

url="http://127.0.0.1:8000/product/"

response=requests.get(url, params={'abc':1234},json={'vibe':'darkness'})

print(response.json())
print(response.status_code)

#HTTP REQUEST --->HTML
#REST API HTTP ---->JSON 
  
