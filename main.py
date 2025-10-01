from fastapi import FastAPI

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