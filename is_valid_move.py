import re

from can_piece_move import can_piece_move


def is_valid_move(player, move, board):
    # Check if the move is in the correct format (e.g. "e4")
    print("In valid move function")
    if not re.match(r"[a-h][1-8]", move):
        return False
    # Check if the destination square is empty or contains an opponent's piece
    row = ord(move[0]) - ord('a')
    col = int(move[1]) - 1
    if board[row][col] != ' ' and board[row][col].islower() == player.islower():
        return False
    # Check if the player has a piece that can make the specified move
    return can_piece_move(player, move, board)
