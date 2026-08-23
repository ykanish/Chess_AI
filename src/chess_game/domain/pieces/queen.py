from chess_game.domain.pieces.piece import Piece


class Queen(Piece):

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

        straight_move = (
            start_row == end_row
            or start_column == end_column
        )

        diagonal_move = row_difference == column_difference

        return (straight_move or diagonal_move) and (
            row_difference != 0 or column_difference != 0
        )