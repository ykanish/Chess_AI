from chess_game.domain.pieces.bishop import Bishop
from chess_game.domain.pieces.king import King
from chess_game.domain.pieces.knight import Knight
from chess_game.domain.pieces.pawn import Pawn
from chess_game.domain.pieces.queen import Queen
from chess_game.domain.pieces.rook import Rook
from chess_game.enums.piece_color import PieceColor
from chess_game.domain.board import Board


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

def test_white_pawn_can_move_one_square_forward():
    board = Board()
    pawn = board.get_box(1, 4).piece

    assert pawn.can_move(
        1, 4,
        2, 4,
        board,
    )

def test_white_pawn_can_move_two_squares_from_start():
    board = Board()
    pawn = board.get_box(1, 4).piece

    assert pawn.can_move(
        1, 4,
        3, 4,
        board,
    )

def test_pawn_cannot_move_two_squares_after_leaving_start():
    board = Board()
    pawn = board.get_box(1, 4).piece

    board.move_piece(1, 4, 2, 4)

    assert not pawn.can_move(
        2, 4,
        4, 4,
        board,
    )

def test_pawn_cannot_move_diagonally_without_capture():
    board = Board()
    pawn = board.get_box(1, 4).piece

    assert not pawn.can_move(
        1, 4,
        2, 5,
        board,
    )

def test_pawn_can_capture_opponent():
    board = Board()

    white_pawn = board.get_box(1, 4).piece
    black_pawn = board.get_box(6, 3).piece

    board.move_piece(1, 4, 3, 4)
    board.move_piece(6, 3, 4, 3)

    assert white_pawn.can_move(
        3, 4,
        4, 3,
        board,
    )

def test_pawn_cannot_capture_own_piece():
    board = Board()

    white_pawn = board.get_box(1, 4).piece

    assert not white_pawn.can_move(
        1, 4,
        2, 3,
        board,
    )