from fastapi import FastAPI, HTTPException, Form, File, UploadFile
from models import EmailModel, TranslationRequest
import openai
import os
from dotenv import load_dotenv
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
from googletrans import Translator
load_dotenv()

openai_key = os.getenv("OPENAI_API_KEY")
app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.post("/email-response-generate")
async def email_response(email_req: EmailModel):
    try:
        if not openai_key:
            raise HTTPException(status_code=500, detail="OpenAI API key is missing")

        client = openai.OpenAI(api_key=openai_key)  

        response = client.chat.completions.create(  
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a professional email assistant."},
                {"role": "user", "content": f"Write a professional response email for:\n\n{email_req.message}"}
            ],
            max_tokens=150
        )
        return {
            "email": email_req.email,
            "response_generated": response.choices[0].message.content.strip()
        }

    except Exception as e:
        print(f"Error occurred while processing OpenAI email responder: {e}")
        raise HTTPException(status_code=500, detail=str(e))



@app.post("/translate")
async def translate(request: TranslationRequest):
    try:
        translator = Translator()
        translated = await translator.translate(request.text, dest=request.lang)  
        return {"translated_text": translated.text}
    except Exception as e:
        print(f"Translation error: {e}")
        raise HTTPException(status_code=500, detail="Translation failed")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("email_form.html", {"request": request})

