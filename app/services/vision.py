import cv2
import numpy as np 




#funcao que recebe os bytes das imaggenns e retorna os bytes processados
def process_image(image_byte: bytes) -> bytes: 
    np_array = np.frombuffer(image_byte, np.uint8)# Converte os bytes em um array numpy
    image = cv2.imdecode(np_array, cv2.IMREAD_COLOR)#Converte o array np em uma imagem legível OpenCV


    if image is None:# Verifica se a imagem é válida, retorna None se falhar
        raise ValueError("Invalid image, Could not process the file")
    
    height, width = image.shape[:2]
    
    if width > 1024:
        #calcula a proporcao pra n distorcer a imagem
        ratio = 1024 / width
        new_width = 1024
        new_height = int(height * ratio)

        image = cv2.resize(image, (new_width, new_height))#redimensiona a imagem

    _, processed_bytes = cv2.imencode(".jpg", image) #converte a imagem processada de volta pra bytes
    return processed_bytes.tobytes()#Rrtorna os bytes prontos pra mandar pro gemini