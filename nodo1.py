from threading import Thread
import sys  
from flask import Flask, request, jsonify
import requests
import os
import json

numeronodo = 1


# nodos2 = [os.environ['nodo3']]
# nodos3 = [os.environ['nodo2'],os.environ['nodo4']]
# nodos4 = [os.environ['nodo3'],os.environ['nodo5']]
# nodos5 = [os.environ['nodo4']]
# nodosEnumerados = []

# def funcionPrincipal():
#     global nodos
#     requests.get(os.environ['nodo2']+"/retornamodulo",{"direcciones":",".join(nodos2),"direccion":os.environ['nodo2']})
#     requests.get(os.environ['nodo3']+"/retornamodulo",{"direcciones":",".join(nodos3),"direccion":os.environ['nodo3']})
#     requests.get(os.environ['nodo4']+"/retornamodulo",{"direcciones":",".join(nodos4),"direccion":os.environ['nodo4']})
#     requests.get(os.environ['nodo5']+"/retornamodulo",{"direcciones":",".join(nodos5),"direccion":os.environ['nodo5']})



app = Flask(__name__)
nodos2 = ["http://127.0.0.3:5000",]
nodos3 = ["http://127.0.0.2:5000","http://127.0.0.4:5000"]
nodos4 = ["http://127.0.0.3:5000","http://127.0.0.5:5000"]
nodos5 = ["http://127.0.0.4:5000"]
nodosEnumerados = []

def funcionPrincipal():
    global nodos
    requests.get("http://127.0.0.2:5000/retornamodulo",{"direcciones":",".join(nodos2),"direccion":"http://127.0.0.2:5000"})
    requests.get("http://127.0.0.3:5000/retornamodulo",{"direcciones":",".join(nodos3),"direccion":"http://127.0.0.3:5000"})
    requests.get("http://127.0.0.4:5000/retornamodulo",{"direcciones":",".join(nodos4),"direccion":"http://127.0.0.4:5000"})
    requests.get("http://127.0.0.5:5000/retornamodulo",{"direcciones":",".join(nodos5),"direccion":"http://127.0.0.5:5000"})






if __name__ == '__main__':
    funcionPrincipal()
    # Thread(target = app.run(host="127.0.0.1",port=5000,  debug=False)).start()


# if __name__ == '__main__':
#     funcionPrincipal()
#     Thread(target = app.run(host="0.0.0.0",  debug=False)).start()
    