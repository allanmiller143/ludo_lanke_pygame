import pygame
from board import Board
from player import Player

def main():
    pygame.init()

    width, height = 450, 650
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Janela do Pygame")
    bg_color = (255, 255, 255)
    board = Board(screen)
    player = Player(screen,(255,255,0))
    running = True


    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Se o botão do mouse foi pressionado
                mouse_pos = pygame.mouse.get_pos()
                player.move_piece(mouse_pos,board)
      
        screen.fill(bg_color)
        board.draw()
        player.draw()
        #player.ButtonOut()


        # Atualizar a tela
        pygame.display.flip()

        # Controlar a taxa de quadros por segundo (FPS)
        pygame.time.Clock().tick(60)


