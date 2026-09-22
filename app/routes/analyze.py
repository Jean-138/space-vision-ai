# Importa o APIRouter para criar rotas separadas do main.py
# Importa o UploadFile e File para receber arquivos via requisição
from fastapi import APIRouter, UploadFile, File, HTTPException
import os # Manipulaçao de arquivos e diretórios
from app.services.vision import process_image #Importa a função de processamento de imagem do vision.py
from app.services.ai_service import analyze_space_image #Importa a função de análise do ai_service.py
from app.schemas.response import SpaceAnalysisResponse #importa o schema de resposta


router = APIRouter() #cria o roteador



# Define a rota POST /analyze
# Quando alguém enviar uma imagem pra esse endereço, essa função executa
@router.post("/analyze", response_model=SpaceAnalysisResponse)
async def analyze_image(file: UploadFile = File(...)):
    if not file.filename: # Verifica se o arquivo foi enviado, se não, retorna erro 400
        raise HTTPException(status_code=400, detail="No file was uploaded")
    image_bytes = await file.read() #le os bytes do arquivo enviado
    if not image_bytes: # Verifica se o arquivo contém dados, se não, retorna erro 400

        raise HTTPException(status_code=400, detail="The uploaded file is empty")
    MAX_FILE_SIZE = 10 * 1024 * 1024
    if len(image_bytes) > MAX_FILE_SIZE: #Verifica se o arquivo excede o tamanho máximo permitido 10mb
        raise HTTPException(status_code=413, detail="File is too large. Maximum size is 10 MB")
    allowed_extensions = {".jpg", ".jpeg", ".png", ".webp", ".bmp", ".gif"} # extensoes de arquivo permitidas
    file_extension = os.path.splitext(file.filename)[1].lower()
    if file_extension not in allowed_extensions: #Verifica se a extensão do arquivo é permitida
        raise HTTPException(status_code=400, detail="Invalid file type")
    try: #inicia o bloco de tratamento de erros
        processed_bytes = process_image(image_bytes) #passa os bytes pro OpenCV processar
        result = analyze_space_image(processed_bytes) #passa os bytes processados pro Gemini analisar
        return result # retorna o resultado no formato do schema
    except ValueError as e: #Captura erros de valor inválido retornados pelas funções
        raise HTTPException(status_code=400, detail=str(e))
    except Exception: #Captura qualquer outro erro inesperado no servidor
        raise HTTPException(status_code=500, detail="Internal server error")

