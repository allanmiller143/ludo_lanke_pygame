import pygame
from board import Board

def main():
    pygame.init()

    width, height = 450, 450
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Janela do Pygame")
    bg_color = (255, 255, 255)
    board = Board(screen)
    running = True


    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
      
        screen.fill(bg_color)
        board.draw()
        #running = False

        # Atualizar a tela
        pygame.display.flip()

        # Controlar a taxa de quadros por segundo (FPS)
        pygame.time.Clock().tick(60)


