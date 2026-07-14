import pytest
import pandas as pd
from src.transform import process_standings

def test_process_standings_calculation():
    # 1. Dados simulados (Mock) para testar a função
    mock_data = {
        'standings': [{
            'table': [{
                'position': 1,
                'team': {'name': 'Time A'},
                'playedGames': 10,
                'won': 5,
                'draw': 3,
                'lost': 2,
                'goalsFor': 20,
                'goalsAgainst': 10,
                'goalDifference': 10,
                'points': 18
            }]
        }]
    }
    
    # 2. Executa a transformação
    df = process_standings(mock_data)
    
    # 3. Verifica se os cálculos foram feitos corretamente
    # Gols por jogo: 20 / 10 = 2.0
    assert df['goals_per_game'].iloc[0] == 2.0
    
    # Aproveitamento: 18 / (10 * 3) = 0.6
    assert df['points_pct'].iloc[0] == 0.6
    
    # Verifica se as colunas necessárias existem
    assert 'team_name' in df.columns
    assert 'goals_per_game' in df.columns

def test_process_standings_empty():
    # Testa como o código lida com dados vazios
    assert process_standings({'standings': []}) is None