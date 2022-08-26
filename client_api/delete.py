import requests
id= input("entrez l'id du produit que vous voulez supprimer : ")

url= f"http://127.0.0.1:8000/product/{id}/delete"

response=requests.delete(url)

# print(response.json())
print(response.status_code, response.status_code==204)