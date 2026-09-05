from chess_game.domain.board import Board
from chess_game.domain.check_detector import CheckDetector
from chess_game.enums.piece_color import PieceColor


def test_white_king_is_not_in_check_at_start():
    board = Board()
    detector = CheckDetector()

    assert not detector.is_in_check(board, PieceColor.WHITE)

def test_black_king_is_not_in_check_at_start():
    board = Board()
    detector = CheckDetector()

    assert not detector.is_in_check(board, PieceColor.BLACK)

def test_black_king_is_in_check_from_white_rook():
    board = Board()
    detector = CheckDetector()

    black_king = board.get_box(7, 4).get_piece()
    white_rook = board.get_box(0, 0).get_piece()

    # Remove pieces blocking the e-file.
    for row in range(1, 7):
        board.get_box(row, 4).remove_piece()

    # Remove the original white rook from a1.
    board.get_box(0, 0).remove_piece()

    # Place it on e1.
    board.get_box(0, 4).set_piece(white_rook)

    assert detector.is_in_check(board, PieceColor.BLACK)

def test_white_king_is_in_check_from_black_knight():
    board = Board()
    detector = CheckDetector()

    white_king = board.get_box(0, 4).get_piece()
    black_knight = board.get_box(7, 1).get_piece()

    # Remove the original black knight.
    board.get_box(7, 1).remove_piece()

    # Put black knight on c3.
    board.get_box(2, 2).set_piece(black_knight)

    assert detector.is_in_check(
        board,
        PieceColor.WHITE,
    )

def test_white_king_is_in_check_from_black_knight():
    board = Board()
    detector = CheckDetector()

    black_knight = board.get_box(7, 1).get_piece()

    board.get_box(7, 1).remove_piece()

    # c2 = (1, 2)
    board.get_box(1, 2).set_piece(black_knight)

    assert detector.is_in_check(
        board,
        PieceColor.WHITE,
    )

def test_white_king_is_in_check_from_black_bishop():
    board = Board()
    detector = CheckDetector()

    black_bishop = board.get_box(7, 2).get_piece()

    # Remove the bishop from c8.
    board.get_box(7, 2).remove_piece()

    # Remove pieces blocking the diagonal.
    board.get_box(1, 4).remove_piece()
    board.get_box(2, 3).remove_piece()
    board.get_box(3, 2).remove_piece()
    board.get_box(4, 1).remove_piece()

    # Put bishop on b5.
    board.get_box(4, 1).set_piece(black_bishop)

    assert detector.is_in_check(
        board,
        PieceColor.WHITE,
    )

def test_white_king_is_in_check_from_black_bishop():
    board = Board()
    detector = CheckDetector()

    black_bishop = board.get_box(7, 2).get_piece()

    # Remove the bishop from c8.
    board.get_box(7, 2).remove_piece()

    # Clear the diagonal b4-c3-d2-e1.
    board.get_box(2, 2).remove_piece()
    board.get_box(1, 3).remove_piece()

    # b4 = (3, 1)
    board.get_box(3, 1).set_piece(black_bishop)

    assert detector.is_in_check(
        board,
        PieceColor.WHITE,
    )

def test_white_king_is_in_check_from_black_queen():
    board = Board()
    detector = CheckDetector()

    black_queen = board.get_box(7, 3).get_piece()

    # Remove the queen from d8.
    board.get_box(7, 3).remove_piece()

    # Clear the d-file between queen and white king.
    for row in range(1, 7):
        board.get_box(row, 4).remove_piece()

    # Put queen on e8.
    board.get_box(7, 4).set_piece(black_queen)

    assert detector.is_in_check(
        board,
        PieceColor.WHITE,
    )

def test_white_king_is_in_check_from_black_pawn():
    board = Board()
    detector = CheckDetector()

    black_pawn = board.get_box(6, 3).get_piece()

    # Remove the pawn from d7.
    board.get_box(6, 3).remove_piece()

    # Put black pawn on d2.
    board.get_box(1, 3).set_piece(black_pawn)

    assert detector.is_in_check(
        board,
        PieceColor.WHITE,
    )

# def test_white_king_is_in_check_from_black_king():
#     board = Board()
#     detector = CheckDetector()

#     white_king = board.get_box(0, 4).get_piece()
#     black_king = board.get_box(7, 4).get_piece()

#     # Remove both kings from their original positions.
#     board.get_box(0, 4).remove_piece()
#     board.get_box(7, 4).remove_piece()

#     # Place them next to each other.
#     # White king = e4
#     # Black king = e5
#     board.get_box(3, 4).set_piece(white_king)
#     board.get_box(4, 4).set_piece(black_king)

#     assert detector.is_in_check(
#         board,
#         PieceColor.WHITE,
#     )

# def test_debug_black_rook_attack():
#     board = Board()
#     detector = CheckDetector()

#     white_rook = board.get_box(0, 0).get_piece()
#     black_rook = board.get_box(7, 7).get_piece()

#     # Clear the e-file.
#     for row in range(1, 7):
#         board.get_box(row, 4).remove_piece()

#     # Remove pawn from d2.
#     board.get_box(1, 3).remove_piece()

#     # Put white rook on e2.
#     board.get_box(0, 0).remove_piece()
#     board.get_box(1, 4).set_piece(white_rook)

#     # Put black rook on e8.
#     board.get_box(7, 7).remove_piece()
#     board.get_box(7, 4).set_piece(black_rook)

#     # Move white rook away from e-file.
#     board.move_piece(1, 4, 1, 3)

#     # Verify that the black piece really is a Rook.
#     assert isinstance(black_rook, Rook)

#     # Black rook attacks white king along the e-file.
#     assert black_rook.can_move(
#         7,
#         4,
#         0,
#         4,
#         board,
#     )

#     assert detector.is_in_check(
#         board,
#         PieceColor.WHITE,
#     )