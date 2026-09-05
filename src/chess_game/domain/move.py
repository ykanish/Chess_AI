from dataclasses import dataclass
from typing import TYPE_CHECKING

from chess_game.domain.position import Position

if TYPE_CHECKING:
    from chess_game.domain.pieces.piece import Piece


@dataclass
class Move:
    start: Position
    end: Position
    piece: "Piece"
    captured_piece: "Piece | None" = None