import json
from fastapi import FastAPI, Response
import pandas as pd
import random

app = FastAPI()

@app.get("/")
def post_data():
    stock = pd.read_csv('./problem_data.csv', index_col=0)
    num = random.randrange(1, len(stock) + 1)
    result = stock.loc[num].to_json(orient = 'columns')

    return Response(result)