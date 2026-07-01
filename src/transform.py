import pandas as pd
import json
import os

def load_bronze_data(filepath="data/bronze/pl_standings.json"):
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def transform_to_silver(data):
    # O JSON da API-Football/Football-Data costuma ter uma estrutura aninhada.
    # Vamos extrair a lista de times.
    standings = data['standings'][0]['table']
    
    df = pd.DataFrame(standings)
    
    # Criar um DataFrame simplificado
    silver_df = df[['position', 'team', 'playedGames', 'won', 'draw', 'lost', 'goalsFor', 'goalsAgainst', 'goalDifference', 'points']]
    
    # Extrair apenas o nome do time do dicionário 'team'
    silver_df['team_name'] = silver_df['team'].apply(lambda x: x['name'])
    silver_df = silver_df.drop(columns=['team'])
    
    return silver_df

def calculate_gold_kpis(df):
    # Exemplo de KPI de Eficiência: Média de pontos por jogo
    df['points_per_game'] = df['points'] / df['playedGames']
    
    # Exemplo de KPI de Produção: Saldo de gols por jogo
    df['goal_diff_per_game'] = df['goalDifference'] / df['playedGames']
    
    return df

if __name__ == "__main__":
    # Execução do fluxo
    data = load_bronze_data()
    df_silver = transform_to_silver(data)
    
    # Salvar Silver
    df_silver.to_parquet("data/silver/standings.parquet")
    
    # Calcular e salvar Gold
    df_gold = calculate_gold_kpis(df_silver)
    df_gold.to_parquet("data/gold/kpis.parquet")
    
    print("Transformação concluída! Dados Silver e Gold gerados.")