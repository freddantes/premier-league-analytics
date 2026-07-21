from pydantic import BaseModel, Field, field_validator

class StandingRowSchema(BaseModel):
    position: int = Field(..., ge=1, description="A posição na tabela deve ser maior ou igual a 1")
    team: str = Field(..., min_length=1, description="O nome do time não pode ser vazio")
    points: int = Field(..., ge=0, description="Os pontos não podem ser negativos")
    playedGames: int = Field(..., ge=0)
    won: int = Field(..., ge=0)
    draw: int = Field(..., ge=0)
    lost: int = Field(..., ge=0)
    goalsFor: int = Field(..., ge=0)
    goalsAgainst: int = Field(..., ge=0)
    goalDifference: int

    @field_validator('points', 'playedGames')
    @classmethod
    def validate_not_negative(cls, v: int) -> int:
        if v < 0:
            raise ValueError('O valor não pode ser negativo')
        return v