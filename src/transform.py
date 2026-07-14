import pandas as pd

def process_standings(data):
    """Processa o JSON bruto da API e calcula as métricas (Gold)."""
    # Verifica se há dados de classificação
    if 'standings' not in data or not data['standings']:
        return None
        
    all_groups = []
    for stage in data['standings']:
        if 'table' in stage:
            all_groups.append(pd.DataFrame(stage['table']))
    
    if not all_groups: 
        return None
    
    df = pd.concat(all_groups, ignore_index=True)
    
    # Flattening do dicionário de times
    if 'team' in df.columns:
        df_team = pd.json_normalize(df['team']).add_prefix('team_')
        df = pd.concat([df.drop(columns=['team']), df_team], axis=1)
    
    # Cálculos de Analytics (KPIs)
    df['goals_per_game'] = (df['goalsFor'] / df['playedGames']).fillna(0).round(2)
    df['points_pct'] = (df['points'] / (df['playedGames'] * 3)).fillna(0).round(2)
    
    return df