from chess_game.domain.board import Board
from chess_game.domain.move import Move
from chess_game.domain.move_validator import MoveValidator
from chess_game.domain.position import Position
from chess_game.enums.piece_color import PieceColor
from chess_game.domain.check_detector import CheckDetector


def test_valid_knight_move():
    board = Board()

    # Move the knight from b1 to c3.
    move = Move(
        start=Position(0, 1),
        end=Position(2, 2),
        piece=board.get_box(0, 1).piece,
    )

    validator = MoveValidator()

    assert validator.is_valid(move, board)


def test_invalid_knight_move():
    board = Board()

    # Knight cannot move from b1 to b2.
    move = Move(
        start=Position(0, 1),
        end=Position(1, 1),
        piece=board.get_box(0, 1).piece,
    )

    validator = MoveValidator()

    assert not validator.is_valid(move, board)


def test_cannot_capture_own_piece():
    board = Board()

    # White knight on b1 cannot capture the white pawn on b2.
    move = Move(
        start=Position(0, 1),
        end=Position(1, 1),
        piece=board.get_box(0, 1).piece,
    )

    validator = MoveValidator()

    assert not validator.is_valid(move, board)


def test_start_position_must_contain_move_piece():
    board = Board()

    pawn = board.get_box(1, 4).piece

    move = Move(
        start=Position(3, 4),
        end=Position(4, 4),
        piece=pawn,
    )

    validator = MoveValidator()

    assert not validator.is_valid(move, board)

def test_bishop_cannot_jump_over_piece():
    board = Board()

    bishop = board.get_box(0, 2).piece

    # c1 -> h6.
    # d2 contains a white pawn, so this is blocked.
    move = Move(
        start=Position(0, 2),
        end=Position(5, 7),
        piece=bishop,
    )

    validator = MoveValidator()

    assert not validator.is_valid(move, board)

def test_move_is_invalid_if_it_leaves_own_king_in_check():
    board = Board()
    validator = MoveValidator()

    white_king = board.get_box(0, 4).get_piece()
    white_rook = board.get_box(0, 0).get_piece()
    black_rook = board.get_box(7, 4).get_piece()

    # Clear the e-file so the black rook attacks the white king.
    for row in range(1, 7):
        board.get_box(row, 4).remove_piece()

    # Move black rook from e8 to e2.
    board.get_box(7, 4).remove_piece()
    board.get_box(1, 4).set_piece(black_rook)

    # White rook is currently protecting the king's position
    # by occupying a1, but we'll move it away.
    move = Move(
        start=Position(0, 0),
        end=Position(0, 1),
        piece=white_rook,
    )

    assert not validator.is_valid(move, board)

# def test_move_is_invalid_if_it_leaves_own_king_in_check():
#     board = Board()
#     validator = MoveValidator()

#     white_rook = board.get_box(0, 0).get_piece()
#     black_rook = board.get_box(7, 4).get_piece()

#     # Clear the e-file.
#     for row in range(1, 7):
#         board.get_box(row, 4).remove_piece()

#     # Remove the white pawn from d2.
#     board.get_box(1, 3).remove_piece()

#     # Move white rook from a1 to e2.
#     board.get_box(0, 0).remove_piece()
#     board.get_box(1, 4).set_piece(white_rook)

#     # Move black rook to e8.
#     board.get_box(7, 4).remove_piece()
#     board.get_box(7, 4).set_piece(black_rook)

#     # White rook moves from e2 to d2.
#     #
#     # Before:
#     #
#     # Black Rook
#     #     e8
#     #      |
#     #     e2  <- White Rook blocks attack
#     #      |
#     #     e1  <- White King
#     #
#     # After e2 -> d2:
#     #
#     # Black Rook
#     #     e8
#     #      |
#     #     e2  <- now empty
#     #      |
#     #     e1  <- White King
#     #
#     # The White King is exposed.
#     move = Move(
#         start=Position(1, 4),
#         end=Position(1, 3),
#         piece=white_rook,
#     )

#     assert not validator.is_valid(move, board)
#     board = Board()
#     validator = MoveValidator()

#     white_rook = board.get_box(0, 0).get_piece()
#     black_rook = board.get_box(7, 4).get_piece()

#     # Clear the e-file.
#     for row in range(1, 7):
#         board.get_box(row, 4).remove_piece()

#     # Put white rook on e2.
#     board.get_box(0, 0).remove_piece()
#     board.get_box(1, 4).set_piece(white_rook)

#     # Put black rook on e8.
#     board.get_box(7, 4).remove_piece()
#     board.get_box(7, 4).set_piece(black_rook)

#     # White rook moves from e2 to e3.
#     #
#     # Before the move:
#     #
#     # Black rook
#     #     e8
#     #      |
#     #     e2  <- White rook blocks attack
#     #      |
#     #     e1  <- White King
#     #
#     # After e2 -> e3, e2 becomes empty,
#     # exposing the White King.
#     move = Move(
#         start=Position(1, 4),
#         end=Position(2, 4),
#         piece=white_rook,
#     )

#     assert not validator.is_valid(move, board)
#     board = Board()
#     validator = MoveValidator()

#     white_king = board.get_box(0, 4).get_piece()
#     white_rook = board.get_box(0, 0).get_piece()
#     black_rook = board.get_box(7, 4).get_piece()

#     # Clear the e-file.
#     for row in range(1, 7):
#         board.get_box(row, 4).remove_piece()

#     # Put the white rook on e2.
#     board.get_box(0, 0).remove_piece()
#     board.get_box(1, 4).set_piece(white_rook)

#     # Put the black rook on e8.
#     board.get_box(7, 4).remove_piece()
#     board.get_box(7, 4).set_piece(black_rook)

#     # White rook currently blocks the black rook.
#     # Moving it away exposes the white king.
#     move = Move(
#         start=Position(1, 4),
#         end=Position(2, 4),
#         piece=white_rook,
#     )

#     assert not validator.is_valid(move, board)