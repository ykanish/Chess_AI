from chess_game.domain.pieces.bishop import Bishop
from chess_game.domain.pieces.king import King
from chess_game.domain.pieces.knight import Knight
from chess_game.domain.pieces.pawn import Pawn
from chess_game.domain.pieces.queen import Queen
from chess_game.domain.pieces.rook import Rook
from chess_game.enums.piece_color import PieceColor


def test_knight_movement():
    knight = Knight(PieceColor.WHITE)

    assert knight.can_move(0, 1, 2, 2)
    assert knight.can_move(0, 1, 2, 0)

    assert not knight.can_move(0, 1, 1, 1)


def test_bishop_movement():
    bishop = Bishop(PieceColor.WHITE)

    assert bishop.can_move(2, 2, 4, 4)
    assert bishop.can_move(4, 4, 2, 2)

    assert not bishop.can_move(2, 2, 2, 5)


def test_rook_movement():
    rook = Rook(PieceColor.WHITE)

    assert rook.can_move(0, 0, 0, 5)
    assert rook.can_move(0, 0, 5, 0)

    assert not rook.can_move(0, 0, 5, 5)


def test_queen_movement():
    queen = Queen(PieceColor.WHITE)

    assert queen.can_move(0, 0, 0, 5)
    assert queen.can_move(0, 0, 5, 0)
    assert queen.can_move(0, 0, 5, 5)

    assert not queen.can_move(0, 0, 2, 3)


def test_king_movement():
    king = King(PieceColor.WHITE)

    assert king.can_move(4, 4, 5, 5)
    assert king.can_move(4, 4, 4, 5)

    assert not king.can_move(4, 4, 6, 6)