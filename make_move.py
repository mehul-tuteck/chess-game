from is_valid_move import is_valid_move
from draw_board import draw_board
import pygame


screen = pygame.display.set_mode((400, 400))


def make_move(player, move, board):
    if is_valid_move(player, move, board):
        # Update the board
        row = ord(move[0]) - ord('a')
        col = int(move[1]) - 1
        if board[row][col] != ' ':
            print("Piece taken!")
        board[row][col] = player
        draw_board(screen, board)
        pygame.display.flip()
        return True
    else:
        print("Invalid move!")
        return False
