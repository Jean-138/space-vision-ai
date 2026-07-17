from fastapi import FastAPI #importa a classe FastAPI da biblioteca fastapi
from app.routes.analyze import router #importa routeer com o endpoint de analise

#cria a instacia da aplicacao

app = FastAPI(
        title="Space Vision AI",
        description="API that analyzes space images using Artificial Intelligence",
        version="1.0.0"
)

#Inclui as rotas do router
#include_router() registra todas as rotas que estao em analyze.py
app.include_router(router)



# rota teste

@app.get("/")
def home():
# retorna um dicionario
        return{"Message": "Space Vision AI is up and running"}



