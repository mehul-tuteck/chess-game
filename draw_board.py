import pygame

def draw_board(screen, board):
    # Draw the squares
    for i in range(8):
        for j in range(8):
            color = (255, 255, 255) if (i + j) % 2 == 0 else (0, 0, 0)
            pygame.draw.rect(screen, color, (i * 80, j * 80, 80, 80))
    # Draw the pieces
    for i in range(8):
        for j in range(8):
            piece = board[i][j]
            if piece != ' ':
                # Load the image for the piece
                image = pygame.image.load(f"assets/{piece}.png")
                # Draw the image on the screen
                screen.blit(image, (i * 80, j * 80))
