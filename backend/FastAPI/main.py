from numpy import diag
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import File, UploadFile
import os

# sample_data
os.system('python dashboard_sample_data/test.py')

# graph
import pandas as pd
import cufflinks as cf
from database.db_connect import engine

import json

df = pd.read_csv('data/sample_sleep.csv')
data = df['EMAIL'].value_counts()
plot = data.iplot(asFigure=True, xTitle='EMAIL', yTitle='data count')
pjs = plot.to_json().replace('/', '')

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request:Request):
    conn = engine.connect()
    email, diag_nm, duravg, efficiency, durstd, sleep_score = [],[],[],[],[],[]
    data = conn.execute('select * from processing;')
    for _ in data:
        email.append(_[0])
        diag_nm.append(_[1])
        duravg.append(int(_[2]))
        efficiency.append(int(_[3]))
        durstd.append(int(_[4]))
        sleep_score.append(int(_[5]))
    
    df = pd.DataFrame([
        ['email', len(set(email))], 
        ['diag_nm', len(set(diag_nm))], 
        ['duravg', len(set(duravg))], 
        ['efficiency', len(set(efficiency))], 
        ['durstd', len(set(durstd))], 
        ['sleep_score', len(set(sleep_score))]])
    df.columns = ['name', 'cnt_data']
    df.set_index('name', inplace=True)
    json_object = df.to_json()

    with open('./src/app.json', 'w') as f:
        f.write(json_object)
    
    return templates.TemplateResponse('home.html', {"request": request}) 

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


