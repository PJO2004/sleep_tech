from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import File, UploadFile
import os

# graph
import pandas as pd
import cufflinks as cf

df = pd.read_csv('data/sample_sleep.csv')
data = df['EMAIL'].value_counts()
plot = data.iplot(asFigure=True, xTitle='EMAIL', yTitle='data count')
pjs = plot.to_json().replace('/', '')
print(data)

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request:Request):
    return templates.TemplateResponse('home.html', {"request": request, 'data':pjs}) 

@app.post("/csv")
async def upload_file(file: UploadFile = File(...)):
    upload_directory = "./data/"
    contents = await file.read()

    # test
    with open(os.path.join(upload_directory, "data.csv"), "wb") as fp:
        fp.write(contents)

    with open(os.path.join(upload_directory, "filename.txt"), "w") as fp:
        fp.write(file.filename.split(".")[0])

    return {"filename": file.filename}