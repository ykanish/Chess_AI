from chess_game.domain.pieces.piece import Piece


class Rook(Piece):

    def can_move(
        self,
        start_row: int,
        start_column: int,
        end_row: int,
        end_column: int,
        board=None,
    ) -> bool:

        same_row = start_row == end_row
        same_column = start_column == end_column

        return same_row != same_column