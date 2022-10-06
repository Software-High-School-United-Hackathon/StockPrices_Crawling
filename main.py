import json
from fastapi import FastAPI, Response
import pandas as pd
import random
from fastapi.responses import JSONResponse

import json

app = FastAPI()



@app.get("/")
def post_data():
    stock = pd.read_csv('./result.csv', index_col=0, encoding="utf-8-sig")

    num = random.randrange(1, len(stock))
    result = stock.loc[num].to_json(force_ascii=False, orient = 'columns')
    result = json.loads(result)

    return JSONResponse(content=result)