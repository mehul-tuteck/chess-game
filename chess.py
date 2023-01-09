import pygame
import numpy as np
import re

from is_valid_move import is_valid_move
from make_move import make_move


# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((400, 400))

# Set up the game board
board = [
    ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
    ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'],
    ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR']
]

board = np.array(board)
board = board.transpose()

# Run the game loop
running = True
player = 'w'  # w for white, b for black
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Get the click coordinates
            print("Mouse Clicked")
            x, y = event.pos
            # Convert the coordinates to a move (e.g. "e4")
            move = chr(ord('a') + x // 50) + str(y // 50 + 1)
            print(move)
            if is_valid_move(player, move, board):
                # Make the move and switch to the other player
                make_move(player, move, board)
                player = 'b' if player == 'w' else 'w'

    # Draw the board
    for i in range(8):
        for j in range(8):
            color = (255, 255, 255) if (i + j) % 2 == 0 else (0, 0, 0)
            pygame.draw.rect(screen, color, (i * 50, j * 50, 50, 50))
            # Draw the piece, if there is one
            piece = board[i][j]
            if piece != ' ':
                # Load the image for the piece
                image = pygame.image.load(f"assets/{piece}.png")
                # Convert the image to a surface with the same pixel format as the screen
                image = image.convert(screen)
                # Set the piece's color to white or black
                image.set_colorkey((255, 255, 255))
                # Draw the image on the screen
                screen.blit(image, (i * 50, j * 50))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
