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
        # Check if the move is within the bounds of the board
        direction = 1 if self.color == PieceColor.WHITE else -1

        row_difference = end_row - start_row
        column_difference = abs(end_column - start_column)

        #Normal one square move
        if row_difference == direction and column_difference == 0:
            return True

        if row_difference == 2 * direction and column_difference == 0:
            return True

        if row_difference == direction and column_difference == 1:
            return True

        return False
