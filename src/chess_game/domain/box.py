from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from chess_game.domain.pieces.piece import Piece


@dataclass
class Box:
    row: int
    column: int
    piece: "Piece | None" = None

    def is_empty(self) -> bool:
        return self.piece is None

    def set_piece(self, piece: "Piece") -> None:
        self.piece = piece

    def remove_piece(self) -> "Piece | None":
        piece = self.piece
        self.piece = None
        return piece
