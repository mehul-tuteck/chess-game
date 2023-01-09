def can_piece_move(player, move, board):
    # Find the player's pieces
    pieces = [piece for row in board for piece in row if piece.lower()
              == player]
    # Check if any of the player's pieces can make the specified move
    for piece in pieces:
        if piece.lower() == 'p':
            # Pawns can move forward one square if the destination is empty, or forward
            # diagonally if the destination contains an opponent's piece
            row = ord(move[0]) - ord('a')
            col = int(move[1]) - 1
            if player == 'w':
                if move == f"{chr(ord('a') + row)}{col + 2}" and board[row][col + 1] == ' ':
                    return True
                if col < 7 and row < 7 and board[row + 1][col + 1] == 'p':
                    return True
            else:
                if move == f"{chr(ord('a') + row)}{col - 2}" and board[row][col - 1] == ' ':
                    return True
                if col > 0 and row > 0 and board[row - 1][col - 1] == 'P':
                    return True
        elif piece.lower() == 'n':
            # Knights can move to any of the squares adjacent to their current position
            row = ord(move[0]) - ord('a')
            col = int(move[1]) - 1
            if (row > 0 and col > 1 and board[row - 1][col - 2] == ' ') or \
                    (row > 1 and col > 0 and board[row - 2][col - 1] == ' ') or \
                    (row > 1 and col < 7 and board[row - 2][col + 1] == ' ') or \
                    (row < 7 and col > 1 and board[row + 1][col - 2] == ' ') or \
                    (row < 6 and col > 0 and board[row + 2][col - 1] == ' ') or \
                    (row < 6 and col < 7 and board[row + 2][col + 1] == ' ') or \
                    (row < 7 and col < 6 and board[row + 1][col + 2] == ' '):
                return True
        elif piece.lower() == 'b':
            # Bishops can move diagonally in any direction as long as the path is clear
            row = ord(move[0]) - ord('a')
            col = int(move[1]) - 1
            if row > col:
                r, c = row - col, 0
            else:
                r, c = 0, col - row
            while r < 8 and c < 8:
                if board[r][c] != ' ':
                    if r + c == row + col and board[r][c].lower() != player:
                        return True
                    break
                r += 1
                c += 1
            if row + col < 8:
                r, c = row + col, 0
            else:
                r, c = 7, row + col - 7
            while r >= 0 and c < 8:
                if board[r][c] != ' ':
                    if r - c == row - col and board[r][c].lower() != player:
                        return True
                    break
                r -= 1
                c += 1
        elif piece.lower() == 'r':
            # Rooks can move horizontally or vertically in any direction as long as the path is clear
            row = ord(move[0]) - ord('a')
            col = int(move[1]) - 1
            if row > 0:
                r = row - 1
                while r >= 0:
                    if board[r][col] != ' ':
                        if r == row - 1 and board[r][col].lower() != player:
                            return True
                        break
                    r -= 1
            if row < 7:
                r = row + 1
                while r < 8:
                    if board[r][col] != ' ':
                        if r == row + 1 and board[r][col].lower() != player:
                            return True
                        break
                    r += 1
            if col > 0:
                c = col - 1
                while c >= 0:
                    if board[row][c] != ' ':
                        if c == col - 1 and board[row][c].lower() != player:
                            return True
                        break
                    c -= 1
            if col < 7:
                c = col + 1
                while c < 8:
                    if board[row][c] != ' ':
                        if c == col + 1 and board[row][c].lower() != player:
                            return True
                        break
                    c += 1
        elif piece.lower() == 'k':
            # Kings can move one square in any direction
            row = ord(move[0]) - ord('a')
            col = int(move[1]) - 1
            if row > 0 and board[row - 1][col] == ' ' or board[row - 1][col].lower() != player:
                return True
            if row < 7 and board[row + 1][col] == ' ' or board[row + 1][col].lower() != player:
                return True
            if col > 0 and board[row][col - 1] == ' ' or board[row][col - 1].lower() != player:
                return True
            if col < 7 and board[row][col + 1] == ' ' or board[row][col + 1].lower() != player:
                return True
    return False
