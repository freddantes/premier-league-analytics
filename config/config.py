import os
from dotenv import load_dotenv

# Carrega as variáveis definidas no arquivo .env para o sistema
load_dotenv()

# Cria constantes que o resto do programa vai usar
API_KEY = os.getenv("API_KEY")
API_BASE_URL = os.getenv("API_BASE_URL")

# Verificação de segurança: Se a chave não estiver no .env, o programa avisa
if not API_KEY:
    raise ValueError("Atenção: A variável API_KEY não foi encontrada no arquivo .env!")