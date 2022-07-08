from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import APIRouter

app = FastAPI()
router = APIRouter()
templates = Jinja2Templates(directory="/templates")

app.mount("/static", StaticFiles(directory="static"), name="css")
app.include_router(index.router)

@router.get('/', response_class=HTMLResponse)
def hello_world(): 
	return templates.TemplateResponse('home.html') 
