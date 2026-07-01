import requests
import json
from config.config import API_KEY, API_BASE_URL

def get_premier_league_standings():
    """
    Busca a tabela de classificação da Premier League (código PL).
    """
    url = f"{API_BASE_URL}/competitions/PL/standings"
    headers = {'X-Auth-Token': API_KEY}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Levanta um erro se a requisição falhar (ex: 404, 500)
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Erro ao conectar na API: {e}")
        return None

def save_raw_data(data, filename="data/bronze/pl_standings.json"):
    """
    Salva o JSON bruto na pasta bronze (Ingestão).
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print(f"Dados salvos com sucesso em {filename}")

if __name__ == "__main__":
    # Teste rápido do script
    data = get_premier_league_standings()
    if data:
        save_raw_data(data)