import pygame

class Player:
    def __init__(self,screen,color):
        self.screen = screen
        self.coordinates = [
                            [65,170],
                            [115,170],
                            [65,210],
                            [115,210],
                           ]
        self.color = color
        self.pieces = ['PY','PY','PY','PY']

        

    def draw(self):
        for coord in self.coordinates:
            pygame.draw.circle(self.screen, (255, 255, 0), (coord[0],coord[1]), radius=13)
    

    def move_piece(self, mouse_pos,board):
        for i, coord in enumerate(self.coordinates):
            if pygame.Rect(coord[0] - 13, coord[1] - 13, 26, 26).collidepoint(mouse_pos):
                # Atualizar a posição da peça clicada
                self.coordinates[i] = [45,290]

                board.matriz[6][1] = 'PY'


        



        


    





