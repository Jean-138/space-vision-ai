from fastapi import FastAPI #importa a classe FastAPI da biblioteca fastapi


#cria a instacia da aplicacao

app = FastAPI(
        title="Space Vision AI",
        description="API that analyzes space images using Artificial Intelligence",
        version="1.0.0"
)


# primeira rota

@app.get("/")
def home():
# retorna um dicionario
        return{"Message": "Space Vision AI is up and running"}



