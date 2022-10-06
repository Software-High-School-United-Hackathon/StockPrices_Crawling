import json
from fastapi import FastAPI, Response
import pandas as pd
import random
from fastapi.responses import JSONResponse, FileResponse
from bs4 import BeautifulSoup
import urllib.request
import math
import json

app = FastAPI()



@app.get("/")
def post_data():
    stock = pd.read_csv('./result.csv', index_col=0, encoding="utf-8-sig")

    num = random.randrange(1, len(stock))
    result = stock.loc[num].to_json(force_ascii=False, orient = 'columns')
    result = json.loads(result)

    return JSONResponse(content=result)


@app.get("/test")
def stock_propensity(s0: int, s1: int, s2: int, s3: int, s4: int, s5: int, s6: int, s7: int, s8: int, s9: int):

    vals = [s0, s1, s2, s3, s4, s5, s6, s7, s8, s9]

    for i in range(len(vals)):
        vals[i] = abs(vals[i])

    std = sum(vals)

    if 20 > std >= 0:
        num = 4
    if 40 > std >= 20:
        num = 3
    if 60 > std >= 40:
        num = 2
    if 80 > std >= 60:
        num = 1
    else:
        num = 0

    tendency_data = pd.read_csv('./tendency_data.csv', index_col=0, encoding="utf-8-sig")
    tendency = tendency_data.loc[num].to_json(force_ascii=False, orient='columns')
     
    tendency = json.loads(tendency)
    
    return JSONResponse(content=tendency)