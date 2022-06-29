from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import APIRouter

app = FastAPI()
router = APIRouter()
templates = Jinja2Templates(directory="../../frontend/templates")

@router.get('/', response_class=HTMLResponse)
def hello_world(): 
	return templates.TemplateResponse('home.html') 

if __name__ == '__main__': uvicorn.run(app)


# @router.get("/", response_class=HTMLResponse)
# async def home(request: Request):
#     data = openfile("home.md")
#     return templates.TemplateResponse("page.html", {"request": request, "data": data})