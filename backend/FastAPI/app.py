from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("../../frontend/static", StaticFiles(directory="static"), name="static")

@app.get('/')
def hello_world(): 
	return {'message':'안녕하세요'} 

@app.get("/home.html", response_class=HTMLResponse) 
async def read_item(request: Request): 
	return templates.TemplateResponse("home.html") 

if __name__ == '__main__': uvicorn.run(app)