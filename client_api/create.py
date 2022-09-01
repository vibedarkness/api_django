import json
# from wsgiref import headers
import requests
from getpass import getpass

url_token="http://127.0.0.1:8000/api/auth"
username=input("veuillez saisir votre nom d'utlisateur: " )
password=getpass("entrez votre mot de passe : " )
auth_response=requests.post(url_token,json={'username':username,'password':password})
print(auth_response.json())

if auth_response.status_code == 200:
    url="http://127.0.0.1:8000/product/create/"
    url_get="http://127.0.0.1:8000/product/list/"

    headers={
        'Authorization':'Bearer 05a144c6e6b2e7cdf2081041d192e0ee158b69ee'
    }
    response=requests.post(url, json={'name':'omzo', 'content':'lorem ipsum vibe darkness mangue', 'price':'128256.23'},headers=headers)
    response_get=requests.get(url_get)
    print(response.json())
    print(response_get.json())
    print(response.status_code)