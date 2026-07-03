import pandas as pd
import requests
import os
from dotenv import load_dotenv
from pathlib import Path

# Busca o arquivo .env na raiz do projeto, mesmo estando dentro da pasta src
load_dotenv(dotenv_path=Path(__file__).resolve().parent.parent / '.env')

def run_pipeline():
    print("Iniciando extração de dados reais...")
    
    # Busca as variáveis injetadas (seja pelo .env local ou pelo GitHub Actions)
    api_key = os.getenv("API_KEY")
    base_url = os.getenv("API_BASE_URL")
    
    # Validação simples
    if not api_key:
        raise ValueError("API_KEY não encontrada! Verifique seu arquivo .env ou Secrets do GitHub.")

    # Endpoint específico da Premier League (PL)
    endpoint = f"{base_url}/competitions/PL/standings"
    headers = {"X-Auth-Token": api_key}
    
    # Chamada para a API
    response = requests.get(endpoint, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        
        # Extrai a tabela (standings)
        # A estrutura da API football-data é: standings -> [0] (total) -> table
        standings = data['standings'][0]['table']
        
        # Cria o DataFrame
        df = pd.DataFrame(standings)
        
        # Garante a pasta e salva
        os.makedirs("data/gold", exist_ok=True)
        df.to_parquet("data/gold/kpis.parquet")
        print("Pipeline executado com sucesso! Dados reais salvos em data/gold/kpis.parquet")
    else:
        print(f"Erro ao acessar API: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    run_pipeline()