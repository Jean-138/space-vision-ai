# Importa o APIRouter para criar rotas separadas do main.py
# Importa o UploadFile e File para receber arquivos via requisição
from fastapi import APIRouter, UploadFile, File
from app.services.vision import process_image #Importa a função de processamento de imagem do vision.py
from app.services.ai_service import analyze_space_image #Importa a função de análise do ai_service.py
from app.schemas.response import SpaceAnalysisResponse #importa o schema de resposta


router = APIRouter() #cria o roteador



# Define a rota POST /analyze
# Quando alguém enviar uma imagem pra esse endereço, essa função executa
@router.post("/analyze", response_model=SpaceAnalysisResponse)
async def analyze_image(file: UploadFile = File(...)):
    image_bytes = await file.read() #le os bytes do arquivo enviado
    processed_bytes = process_image(image_bytes) #passa os bytes pro OpenCV processar
    result = analyze_space_image(processed_bytes) #passa os bytes processados pro Gemini analisar
    return result # retorna o resultado no formato do schema

