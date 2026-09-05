from chess_game.domain.board import Board
from chess_game.domain.check_detector import CheckDetector
from chess_game.domain.move import Move
from chess_game.domain.pieces.bishop import Bishop
from chess_game.domain.pieces.queen import Queen
from chess_game.domain.pieces.rook import Rook


class MoveValidator:

    def __init__(self, check_detector=None):
        self.check_detector = check_detector or CheckDetector()

    def is_valid(self, move: Move, board: Board) -> bool:
        start_box = board.get_box(
            move.start.row,
            move.start.column,
        )

        end_box = board.get_box(
            move.end.row,
            move.end.column,
        )

        # 1. Start position must contain a piece.
        if start_box.is_empty():
            return False

        piece = start_box.get_piece()

        # 2. The move must contain the same piece
        #    that is actually on the board.
        if piece is not move.piece:
            return False

        # 3. A piece cannot capture another piece
        #    belonging to the same color.
        if (
            not end_box.is_empty()
            and end_box.get_piece().color == piece.color
        ):
            return False

        # 4. Check whether the piece can move
        #    according to its movement rules.
        if not piece.can_move(
            move.start.row,
            move.start.column,
            move.end.row,
            move.end.column,
            board,
        ):
            return False

        # 5. Sliding pieces cannot jump over pieces.
        if self._requires_path_check(piece):
            if not self._is_path_clear(move, board):
                return False

        # 6. Temporarily apply the move and check
        #    whether it leaves our own King in check.
        board.apply_move(move)

        try:
            if self.check_detector.is_in_check(
                board,
                piece.color,
            ):
                return False

            return True

        finally:
            # Always restore the board after validation.
            board.undo_move(move)

    @staticmethod
    def _requires_path_check(piece) -> bool:
        return isinstance(
            piece,
            (Bishop, Rook, Queen),
        )

    def _is_path_clear(
        self,
        move: Move,
        board: Board,
    ) -> bool:

        row_step = self._get_step(
            move.start.row,
            move.end.row,
        )

        column_step = self._get_step(
            move.start.column,
            move.end.column,
        )

        current_row = move.start.row + row_step
        current_column = move.start.column + column_step

        while (
            current_row != move.end.row
            or current_column != move.end.column
        ):
            if not board.get_box(
                current_row,
                current_column,
            ).is_empty():
                return False

            current_row += row_step
            current_column += column_step

        return True

    @staticmethod
    def _get_step(start: int, end: int) -> int:
        if end > start:
            return 1

        if end < start:
            return -1

        return 0