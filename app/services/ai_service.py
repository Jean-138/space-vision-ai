import google.generativeai as genai
import os #acessar variáveis de ambiente
from dotenv import load_dotenv #carregar o arquivo .env
from app.schemas.response import SpaceAnalysisResponse


load_dotenv() #Carrega as variáveis do arquivo .env




#Configura o Gemini com a chave da API 
genai.configure(api_key=os.getenv("GEMINI_API_KEY")) #os.getenv busca o valor da variável ambiente GEMINI_API_KEY.

model = genai.GenerativeModel("gemini-1.5-flash") #cria o modelo




#funcao que recebe os bytes da imagem e retorna a análise completa
def analyze_space_image(image_bytes: bytes) -> SpaceAnalysisResponse:
    image_part = {
        "mime_type": "image/jpeg",
        "data": image_bytes
    }



#o prompt

    prompt = """
        You are an expert astronomer and science communicator.
        Analyze this space image and respond in the following format:

        OBJECT: [name of the identified space object]
        DESCRIPTION: [detailed description of what appears in the image]
        SIMPLE EXPLANATION: [explain as if talking to a curious 10-year-old]
        SCIENTIFIC INFO: [basic scientific data like distance, size, type, constellation]

        Be precise, educational and engaging.
        """
    

    response = model.generate_content([prompt, image_part]) #Chama o Gemini passando o prompt e a imagem


    response_text = response.text #pega o texto da resposta
    lines = response.text.split("\n") #extrai cada campo do texto separadamente

    
    
    #dicio para guardar os valores extraidos
    
    result = {
        "object_identified": "",
        "description": "",
        "simple_explanation": "",
        "scientific_info": ""
    }


#Percorre cada linha e identifica a qual campo pertence
    for line in lines:
        if line.startswith("OBJECT:"):
            result["object_identified"] = line.replace("OBJECT:", "").strip()
        elif line.startswith("DESCRIPTION:"):
            result["description"] = line.replace("DESCRIPTION:", "").strip()
        elif line.startswith("SIMPLE EXPLANATION:"):
            result["simple_explanation"] = line.replace("SIMPLE EXPLANATION:", "").strip()
        elif line.startswith("SCIENTIFIC INFO:"):
            result["scientific_info"] = line.replace("SCIENTIFIC INFO:", "").strip()
    
    return SpaceAnalysisResponse(**result)