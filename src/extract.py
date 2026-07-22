import os
import time
import requests
from src.logging_config import logger

def get_league_data(url_or_code: str, headers: dict = None, max_retries: int = 3, backoff_factor: int = 2) -> dict:
    """
    Extrai dados da API com suporte a retry, exponential backoff e injeção garantida de headers.
    """
    # Garante que os headers tenham a chave da API caso não tenham sido passados corretamente
    if not headers or "X-Auth-Token" not in headers:
        api_key = os.getenv("API_KEY")
        headers = {"X-Auth-Token": api_key} if api_key else {}

    # Monta a URL completa se for passado apenas o código da liga
    if not url_or_code.startswith("http"):
        base_url = os.getenv("API_BASE_URL", "https://api.football-data.org/v4")
        url = f"{base_url}/competitions/{url_or_code}/standings"
    else:
        url = url_or_code

    for attempt in range(1, max_retries + 1):
        try:
            logger.info(f"Tentativa {attempt} de {max_retries} para a URL: {url}")
            
            response = requests.get(url, headers=headers, timeout=10)
            
            if response.status_code == 200:
                logger.info("Dados extraídos com sucesso da API.")
                return response.json()
            
            elif response.status_code in [429, 500, 502, 503, 504]:
                logger.warning(f"Servidor retornou status {response.status_code}. Tentando novamente...")
            else:
                logger.error(f"Erro fatal na requisição. Status code: {response.status_code} - Resposta: {response.text}")
                response.raise_for_status()

        except (requests.exceptions.ConnectionError, requests.exceptions.Timeout) as e:
            logger.warning(f"Falha de conexão ou timeout na tentativa {attempt}: {e}")

        if attempt < max_retries:
            sleep_time = backoff_factor ** attempt
            logger.info(f"Aguardando {sleep_time} segundos antes da próxima tentativa...")
            time.sleep(sleep_time)
        else:
            logger.error("Número máximo de tentativas excedido. Falha na extração.")
            raise Exception(f"Não foi possível extrair os dados para {url} após várias tentativas.")