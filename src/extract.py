import requests
import os

def get_league_data(league_code, api_key):
    """Busca dados de qualquer liga através do código passado."""
    url = f"{os.getenv('API_BASE_URL')}/competitions/{league_code}/standings"
    headers = {"X-Auth-Token": api_key}
    
    response = requests.get(url, headers=headers)
    response.raise_for_status() # Lança erro se a API falhar
    return response.json()