from pydantic import BaseModel, EmailStr

class EmailModel(BaseModel):
    email: EmailStr
    message: str
    
class TranslationRequest(BaseModel):
    text: str
    lang: str
    