from enum import Enum

class GameStatus(Enum):
    ACTIVE = "ACTIVE"
    WHITE_WIN = "WHITE_WIN"
    BLACK_WIN = "BLACK_WIN"
    STALEMATE = "STALEMATE"
    FOREFET = "FORFEIT"
    RESIGNATION = "RESIGNATION"