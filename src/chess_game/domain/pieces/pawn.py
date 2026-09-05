from chess_game.domain.pieces.piece import Piece
from chess_game.enums.piece_color import PieceColor


class Pawn(Piece):

    def can_move(
        self,
        start_row: int,
        start_column: int,
        end_row: int,
        end_column: int,
        board=None,
    ) -> bool:

        direction = (
            1
            if self.color == PieceColor.WHITE
            else -1
        )

        row_difference = end_row - start_row
        column_difference = abs(end_column - start_column)

        # One square forward.
        if row_difference == direction and column_difference == 0:
            if board is None:
                return True

            return board.get_box(
                end_row,
                end_column,
            ).is_empty()

        # Two squares forward from starting position.
        if row_difference == 2 * direction and column_difference == 0:
            if board is None:
                return True

            starting_row = (
                1
                if self.color == PieceColor.WHITE
                else 6
            )

            if start_row != starting_row:
                return False

            middle_box = board.get_box(
                start_row + direction,
                start_column,
            )

            destination_box = board.get_box(
                end_row,
                end_column,
            )

            return (
                middle_box.is_empty()
                and destination_box.is_empty()
            )

        # Diagonal movement is only for capturing.
        if row_difference == direction and column_difference == 1:
            if board is None:
                return True

            destination_box = board.get_box(
                end_row,
                end_column,
            )

            if destination_box.is_empty():
                return False

            return (
                destination_box.get_piece().color
                != self.color
            )

        return False