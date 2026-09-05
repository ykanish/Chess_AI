from chess_game.domain.box import Box
from chess_game.domain.move import Move

from chess_game.domain.pieces.bishop import Bishop
from chess_game.domain.pieces.king import King
from chess_game.domain.pieces.knight import Knight
from chess_game.domain.pieces.pawn import Pawn
from chess_game.domain.pieces.queen import Queen
from chess_game.domain.pieces.rook import Rook
from chess_game.enums.piece_color import PieceColor

class Board:

    SIZE = 8

    def __init__(self):
        self.boxes = [
            [Box(row, column) for column in range(self.SIZE)]
            for row in range(self.SIZE)
        ]

        self.setup_board()

    def get_box(self, row: int, column: int) -> Box:
        if not self.is_valid_position(row, column):
            raise IndexError("Invalid board position")

        return self.boxes[row][column]

    def is_valid_position(self, row: int, column: int) -> bool:
        return (
            0 <= row < self.SIZE
            and 0 <= column < self.SIZE
        )

    def setup_board(self) -> None:
        self._setup_pawns()
        self._setup_back_rank(PieceColor.WHITE, 0)
        self._setup_back_rank(PieceColor.BLACK, 7)

    def _setup_pawns(self) -> None:
        for column in range(self.SIZE):
            self.get_box(1, column).set_piece(
                Pawn(PieceColor.WHITE)
            )

            self.get_box(6, column).set_piece(
                Pawn(PieceColor.BLACK)
            )
    def _setup_back_rank(
        self,
        color: PieceColor,
        row: int,
    ) -> None:

        pieces = [
            Rook(color),
            Knight(color),
            Bishop(color),
            Queen(color),
            King(color),
            Bishop(color),
            Knight(color),
            Rook(color),
        ]

        for column, piece in enumerate(pieces):
            self.get_box(row, column).set_piece(piece)
    
    def move_piece(
        self,
        start_row: int,
        start_column: int,
        end_row: int,
        end_column: int,
    ) -> None:

        start_box = self.get_box(start_row, start_column)
        end_box = self.get_box(end_row, end_column)

        if start_box.is_empty():
            raise ValueError("There is no piece at the starting position")

        piece = start_box.remove_piece()

        end_box.set_piece(piece)

    def apply_move(self, move: Move) -> None:
        start_box = self.get_box(
            move.start.row,
            move.start.column,
        )

        end_box = self.get_box(
            move.end.row,
            move.end.column,
        )

        if start_box.is_empty():
            raise ValueError("There is no piece at the starting position")

        piece = start_box.remove_piece()

        if not end_box.is_empty():
            captured_piece = end_box.remove_piece()
            if captured_piece is not None:
                captured_piece.capture()

        end_box.set_piece(piece)

    def undo_move(self, move: Move) -> None:
        moving_piece = self.get_box(
            move.end.row,
            move.end.column,
        ).remove_piece()

        self.get_box(
            move.start.row,
            move.start.column,
        ).set_piece(moving_piece)

        if move.captured_piece is not None:
            move.captured_piece.is_captured = False

            self.get_box(
                move.end.row,
                move.end.column,
            ).set_piece(move.captured_piece)