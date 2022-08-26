import requests
# id= input("entrez l'id du produit que vous voulez supprimer : ")

url= "http://127.0.0.1:8000/product/list/"

response=requests.get(url)

print(response.json())
print(response.status_code)