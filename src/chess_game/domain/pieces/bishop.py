from chess_game.domain.pieces.piece import Piece


class Bishop(Piece):

    def can_move(
        self,
        start_row: int,
        start_column: int,
        end_row: int,
        end_column: int,
        board=None,
    ) -> bool:

        row_difference = abs(end_row - start_row)
        column_difference = abs(end_column - start_column)

        return row_difference == column_difference and row_difference != 0