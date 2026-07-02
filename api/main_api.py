from fastapi import FastAPI, HTTPException
import pandas as pd
import os
from typing import List, Any

app = FastAPI(title="Premier League Analytics API")

def get_gold_data():
    file_path = os.path.join("data", "gold", "kpis.parquet")
    if not os.path.exists(file_path):
        return None
    # Lê o parquet e converte para uma lista de dicionários
    return pd.read_parquet(file_path).to_dict(orient="records")

@app.get("/")
def read_root():
    return {"message": "Bem-vindo à Premier League Analytics API!"}

# Aqui definimos que o retorno será uma lista (List[Any])
@app.get("/standings", response_model=List[Any])
def get_standings():
    data = get_gold_data()
    if data is None:
        raise HTTPException(status_code=404, detail="Arquivo de dados não encontrado (kpis.parquet)")
    return data