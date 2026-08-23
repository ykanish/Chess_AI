from chess_game.domain.board import Board
from chess_game.domain.pieces.bishop import Bishop
from chess_game.domain.pieces.king import King
from chess_game.domain.pieces.knight import Knight
from chess_game.domain.pieces.pawn import Pawn
from chess_game.domain.pieces.queen import Queen
from chess_game.domain.pieces.rook import Rook
from chess_game.enums.piece_color import PieceColor


def test_board_has_64_boxes():
    board = Board()

    assert len(board.boxes) == 8
    assert all(len(row) == 8 for row in board.boxes)


def test_white_pieces_are_initialized():
    board = Board()

    assert isinstance(board.get_box(0, 0).piece, Rook)
    assert isinstance(board.get_box(0, 1).piece, Knight)
    assert isinstance(board.get_box(0, 2).piece, Bishop)
    assert isinstance(board.get_box(0, 3).piece, Queen)
    assert isinstance(board.get_box(0, 4).piece, King)

    for column in range(8):
        assert isinstance(
            board.get_box(1, column).piece,
            Pawn
        )


def test_black_pieces_are_initialized():
    board = Board()

    assert isinstance(board.get_box(7, 0).piece, Rook)
    assert isinstance(board.get_box(7, 1).piece, Knight)
    assert isinstance(board.get_box(7, 2).piece, Bishop)
    assert isinstance(board.get_box(7, 3).piece, Queen)
    assert isinstance(board.get_box(7, 4).piece, King)

    for column in range(8):
        assert isinstance(
            board.get_box(6, column).piece,
            Pawn
        )


def test_board_has_correct_piece_colors():
    board = Board()

    assert board.get_box(0, 4).piece.color == PieceColor.WHITE
    assert board.get_box(7, 4).piece.color == PieceColor.BLACK

def test_move_piece():
    board = Board()

    # e2 -> e4
    board.move_piece(1, 4, 3, 4)

    assert board.get_box(1, 4).is_empty()

    moved_piece = board.get_box(3, 4).piece

    assert moved_piece is not None
    assert moved_piece.color == PieceColor.WHITE