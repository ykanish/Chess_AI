from chess_game.domain.board import Board
from chess_game.domain.move import Move
from chess_game.domain.position import Position

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

def test_apply_move():
    board = Board()

    pawn = board.get_box(1, 4).piece

    move = Move(
        start=Position(1, 4),
        end=Position(3, 4),
        piece=pawn,
    )

    board.apply_move(move)

    assert board.get_box(1, 4).is_empty()
    assert board.get_box(3, 4).piece is pawn

def test_apply_move_captures_opponent_piece():
    board = Board()

    white_pawn = board.get_box(1, 4).piece
    black_pawn = board.get_box(6, 3).piece

    # Put the pawns in capture position.
    board.move_piece(1, 4, 3, 4)
    board.move_piece(6, 3, 4, 3)

    move = Move(
        start=Position(3, 4),
        end=Position(4, 3),
        piece=white_pawn,
        captured_piece=black_pawn,
    )

    board.apply_move(move)

    assert board.get_box(3, 4).is_empty()
    assert board.get_box(4, 3).piece is white_pawn
    assert black_pawn.is_captured

def test_undo_move_restores_board():
    board = Board()

    pawn = board.get_box(1, 4).get_piece()

    move = Move(
        start=Position(1, 4),
        end=Position(3, 4),
        piece=pawn,
    )

    board.apply_move(move)
    board.undo_move(move)

    assert board.get_box(1, 4).get_piece() is pawn
    assert board.get_box(3, 4).is_empty()