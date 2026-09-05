from abc import ABC, abstractmethod
from typing import TYPE_CHECKING
from chess_game.enums.piece_color import PieceColor

if TYPE_CHECKING:
    from chess_game.domain.board import Board

class Piece(ABC):
    def __init__(self, color: PieceColor):
        self.color = color
        self.is_captured = False

    @abstractmethod
    def can_move(
        self,
        start_row: int,
        start_column: int,
        end_row: int,
        end_column: int,
        board: "Board | None" = None,
    ) -> bool:
        """Determine whether this piece can make the given move."""
        pass

    def capture(self) -> None:
        self.is_captured = True