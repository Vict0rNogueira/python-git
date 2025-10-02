from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

@app.get ("/")
def rota_inicial():
    return {
        "message": "Olá,Mundo"
    }

@app.get("/Teste")
def rota_teste():
    return {
        "message": "Ta funcionando"
    }

class Produto(BaseModel):
    id: int
    nome: str

produtos = []

@app.get ("/produtos")
def get_produtos():
    return produtos

@app.post ("/produtos")
def post_produtos(item: Produto):

    for produto in produtos:
        if produto.id == item.id:
            raise HTTPException(status_code=400, detail="Item já cadastrado")

    produtos.append(item)
    return item

@app.patch ("/produtos/{id}")
def patch_produtos(item: Produto, id:int):
    indice_produto = None
    for i in range(len(produtos)):
        produto = produtos[i]
        if produto.id == id:
            indice_produto = i
            break
    if indice_produto == None:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    
    produtos[i] = item
    return item

@app.delete ("/produtos/{id}")
def delete_produtos():
    return{}

