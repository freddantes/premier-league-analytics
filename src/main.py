import os
from datetime import datetime
from dotenv import load_dotenv
from pathlib import Path

# Importando suas funções dos outros arquivos
from src.extract import get_league_data # Ajuste o import conforme a estrutura da sua pasta
from src.transform import process_standings
from src.load import save_data # (Você pode criar este arquivo baseado na lógica de salvamento)

load_dotenv(dotenv_path=Path(__file__).resolve().parent.parent / '.env')

LEAGUES = {
    "Premier League": "PL",
    "Copa do Mundo": "WC",
    "Champions League": "CL",
    "Mundial de Clubes": "FCWC",
    "Libertadores": "CLI",
    "Brasileirão Série A": "BSA",
    "La Liga": "PD",
    "Ligue 1": "FL1",
    "Serie A Italiana": "SA",
    "Bundesliga": "BL1"
}

def run_pipeline():
    api_key = os.getenv("API_KEY")
    today = datetime.now().strftime("%Y-%m-%d")
    
    for name, code in LEAGUES.items():
        print(f"--- Processando: {name} ---")
        try:
            # 1. EXTRACT
            raw_data = get_league_data(code, api_key)
            
            # 2. TRANSFORM
            df = process_standings(raw_data)
            
            # 3. LOAD
            if df is not None:
                save_data(df, code, today)
                print(f"Sucesso: {name} salvo.")
                
        except Exception as e:
            print(f"Erro no pipeline para {name}: {e}")

if __name__ == "__main__":
    run_pipeline()