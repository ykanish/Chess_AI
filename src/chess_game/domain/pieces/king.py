from chess_game.domain.pieces.piece import Piece


class King(Piece):

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

        return (
            row_difference <= 1
            and column_difference <= 1
            and (row_difference + column_difference) > 0
        )