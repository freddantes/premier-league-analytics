import pandas as pd
import os

def run_pipeline():
    print("Iniciando pipeline...")
    
    # Simulação de dados (já que ainda não configuramos a extração da API)
    # Assim que você tiver a extração, substituiremos este dicionário pelos dados reais
    data = [
        {"team": "Liverpool", "points": 80, "goals": 75},
        {"team": "Manchester City", "points": 78, "goals": 72},
        {"team": "Arsenal", "points": 75, "goals": 70}
    ]
    
    df = pd.DataFrame(data)
    
    # Criar diretórios se não existirem
    os.makedirs("data/gold", exist_ok=True)
    
    # Salvar o arquivo parquet
    df.to_parquet("data/gold/kpis.parquet")
    print("Pipeline executado com sucesso! Arquivo gerado em data/gold/kpis.parquet")

if __name__ == "__main__":
    run_pipeline()