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

def create_app():
    """
    앱 함수 실행
    :return:
    """

    app = FastAPI()
    app.mount("../../frontend/static/css", StaticFiles(directory="static"), name="static")

    # 라우터 정의
    app.include_router(index.router)
    return app

app = create_app()

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)