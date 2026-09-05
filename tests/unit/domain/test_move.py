from chess_game.domain.move import Move
from chess_game.domain.position import Position
from chess_game.domain.pieces.pawn import Pawn
from chess_game.enums.piece_color import PieceColor


def test_move_stores_start_and_end_positions():
    pawn = Pawn(PieceColor.WHITE)

    move = Move(
        start=Position(1, 4),
        end=Position(3, 4),
        piece=pawn,
    )

    assert move.start == Position(1, 4)
    assert move.end == Position(3, 4)
    assert move.piece is pawn


def test_move_without_capture():
    pawn = Pawn(PieceColor.WHITE)

    move = Move(
        start=Position(1, 4),
        end=Position(3, 4),
        piece=pawn,
    )

    assert move.captured_piece is None


def test_move_with_capture():
    white_pawn = Pawn(PieceColor.WHITE)
    black_pawn = Pawn(PieceColor.BLACK)

    move = Move(
        start=Position(4, 4),
        end=Position(5, 5),
        piece=white_pawn,
        captured_piece=black_pawn,
    )

    assert move.piece is white_pawn
    assert move.captured_piece is black_pawn