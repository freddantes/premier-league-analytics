import os

def save_data(df, code, date_str):
    """Salva o DataFrame processado na estrutura de pastas versionadas."""
    target_dir = os.path.join("data", "gold", date_str)
    os.makedirs(target_dir, exist_ok=True)
    
    file_path = os.path.join(target_dir, f"{code}_{date_str}.parquet")
    df.to_parquet(file_path)
    print(f"Sucesso: Dados de {code} salvos em {file_path}")