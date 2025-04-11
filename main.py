from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import joblib

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Load model
model = joblib.load("voting_model.pkl")

@app.get("/", response_class=HTMLResponse)
def show_form(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})

@app.post("/submit", response_class=HTMLResponse)
def handle_form(request: Request, name: str = Form(...), age: int = Form(...), country: str = Form(...)):
    prediction = model.predict([[age]])
    if prediction[0] == 1:
        message = f"Hey {name} from {country}, you're {age} and eligible to vote!"
    else:
        message = f"Hey {name} from {country}, you're {age} and not eligible to vote yet."

    return HTMLResponse(content=f"<h3>{message}</h3><br><a href='/'>Back</a>")
