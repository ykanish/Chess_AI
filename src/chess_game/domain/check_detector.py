from chess_game.domain.board import Board
from chess_game.domain.move import Move
from chess_game.domain.position import Position
from chess_game.domain.pieces.bishop import Bishop
from chess_game.domain.pieces.king import King
from chess_game.domain.pieces.knight import Knight
from chess_game.domain.pieces.pawn import Pawn
from chess_game.domain.pieces.queen import Queen
from chess_game.domain.pieces.rook import Rook
from chess_game.enums.piece_color import PieceColor


class CheckDetector:

    def is_in_check(
        self,
        board: Board,
        color: PieceColor,
    ) -> bool:

        king_position = self._find_king(
            board,
            color,
        )

        if king_position is None:
            return False

        for row in range(board.SIZE):
            for column in range(board.SIZE):

                piece = board.get_box(
                    row,
                    column,
                ).get_piece()

                if piece is None:
                    continue

                # Only opponent pieces can attack the King.
                if piece.color == color:
                    continue

                if self._can_attack(
                    piece,
                    row,
                    column,
                    king_position,
                    board,
                ):
                    return True

        return False

    def _find_king(
        self,
        board: Board,
        color: PieceColor,
    ) -> Position | None:

        for row in range(board.SIZE):
            for column in range(board.SIZE):

                piece = board.get_box(
                    row,
                    column,
                ).get_piece()

                if isinstance(piece, King) and piece.color == color:
                    return Position(row, column)

        return None

    def _can_attack(
        self,
        piece,
        start_row: int,
        start_column: int,
        king_position: Position,
        board: Board,
    ) -> bool:

        end_row = king_position.row
        end_column = king_position.column

        # Pawn attacks are handled separately because
        # Pawn.can_move() treats forward movement differently
        # from attacking diagonally.
        if isinstance(piece, Pawn):
            return self._pawn_can_attack(
                piece,
                start_row,
                start_column,
                end_row,
                end_column,
            )

        if not piece.can_move(
            start_row,
            start_column,
            end_row,
            end_column,
            board,
        ):
            return False

        if isinstance(
            piece,
            (Bishop, Rook, Queen),
        ):
            return self._is_path_clear(
                start_row,
                start_column,
                end_row,
                end_column,
                board,
            )

        return True

    @staticmethod
    def _pawn_can_attack(
        pawn: Pawn,
        start_row: int,
        start_column: int,
        end_row: int,
        end_column: int,
    ) -> bool:

        direction = (
            1
            if pawn.color == PieceColor.WHITE
            else -1
        )

        return (
            end_row - start_row == direction
            and abs(end_column - start_column) == 1
        )

    def _is_path_clear(
        self,
        start_row: int,
        start_column: int,
        end_row: int,
        end_column: int,
        board: Board,
    ) -> bool:

        row_step = self._get_step(
            start_row,
            end_row,
        )

        column_step = self._get_step(
            start_column,
            end_column,
        )

        current_row = start_row + row_step
        current_column = start_column + column_step

        while (
            current_row != end_row
            or current_column != end_column
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