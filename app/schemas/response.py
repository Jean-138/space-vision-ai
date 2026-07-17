from pydantic import BaseModel #importa o BaseModel do Pydantic



class SpaceAnalysisResponse(BaseModel): #classe herda tudo que o BaseModel sabe fazer
    object_identified: str
    description: str
    simple_explanation: str
    scientific_info: str
