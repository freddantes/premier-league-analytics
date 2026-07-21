import pandas as pd
from src.schemas import StandingRowSchema
from src.logging_config import logger

def process_standings(raw_data: dict) -> pd.DataFrame:
    try:
        # Lógica atual de extração do JSON da API para extrair a tabela
        standings_list = raw_data['standings'][0]['table']
        
        processed_data = []
        for row in standings_list:
            item = {
                "position": row.get("position"),
                "team": row.get("team", {}).get("name"),
                "points": row.get("points"),
                "playedGames": row.get("playedGames"),
                "won": row.get("won"),
                "draw": row.get("draw"),
                "lost": row.get("lost"),
                "goalsFor": row.get("goalsFor"),
                "goalsAgainst": row.get("goalsAgainst"),
                "goalDifference": row.get("goalDifference")
            }
            
            # Validação via Pydantic por linha (Contrato de Dados)
            validated_row = StandingRowSchema(**item)
            processed_data.append(validated_row.model_dump())
            
        df = pd.DataFrame(processed_data)
        logger.info("Contrato de dados validado com sucesso para a tabela.")
        return df

    except Exception as e:
        logger.error(f"Falha na validação do contrato de dados: {e}")
        raise e