import requests

def buscar_dados():
    request = requests.get("http://127.0.0.1:5000/")
    print(request.content)