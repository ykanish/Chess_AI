from chess_game.domain.pieces.piece import Piece

class Knight(Piece):
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

        # Check for the L-shaped move
        return (
            (row_difference == 2 and column_difference == 1)
            or
            (row_difference == 1 and column_difference == 2)
        )