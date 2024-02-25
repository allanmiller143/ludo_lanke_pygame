

import pygame 

class Board:
    def __init__(self,screen):
        self.screen = screen
        self.matriz = [
            [0,0,0,0,0,0,1,1,1,0,0,0,0,0,0],
            [0,0,0,0,0,0,1,'B',"S",0,0,0,0,0,0],
            [0,0,0,0,0,0,'S','B',1,0,0,0,0,0,0],
            [0,0,0,0,0,0,1,'B',1,0,0,0,0,0,0],
            [0,0,0,0,0,0,1,'B',1,0,0,0,0,0,0],
            [0,0,0,0,0,0,1,'B',1,0,0,0,0,0,0],
            [1,'S',1,1,1,1,0,'B',0,1,1,1,'S',1,1],
            [1,'Y','Y','Y','Y','Y','Y',0,'R','R','R','R','R','R',1],
            [1,1,'S',1,1,1,0,'G',0,1,1,1,1,'S',1],
            [0,0,0,0,0,0,1,'G',1,0,0,0,0,0,0],
            [0,0,0,0,0,0,1,'G',1,0,0,0,0,0,0],
            [0,0,0,0,0,0,1,'G',1,0,0,0,0,0,0],
            [0,0,0,0,0,0,1,'G','S',0,0,0,0,0,0],
            [0,0,0,0,0,0,'S','G',1,0,0,0,0,0,0],
            [0,0,0,0,0,0,1,1,1,0,0,0,0,0,0],
        ]

    def draw(self):
        for row in range(len(self.matriz)):
            for col in range(len(self.matriz[0])):
                pos_x = 30 * col
                pos_y = 100 + 30 * row
                if self.matriz[row][col] == 0:
                    pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(pos_x, pos_y, 30, 30))
                elif self.matriz[row][col] == 1:
                    pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(pos_x , pos_y , 30, 30))
                elif self.matriz[row][col] == 'S':
                    pygame.draw.rect(self.screen, (139,0,139), pygame.Rect(pos_x , pos_y , 30, 30))
                elif self.matriz[row][col] == 'B':
                    pygame.draw.rect(self.screen, (0, 0, 255), pygame.Rect(pos_x , pos_y , 30, 30))
                elif self.matriz[row][col] == "G":
                    pygame.draw.rect(self.screen, (0,128,0), pygame.Rect(pos_x , pos_y , 30, 30))
                elif self.matriz[row][col] == 'Y':
                    pygame.draw.rect(self.screen, (255,255,0), pygame.Rect(pos_x , pos_y , 30, 30))
                elif self.matriz[row][col] == 'R':
                    pygame.draw.rect(self.screen, (255,0,0), pygame.Rect(pos_x , pos_y , 30, 30))
                elif self.matriz[row][col] == 'PY':
                    pygame.draw.rect(self.screen, (255,255,0), pygame.Rect(pos_x , pos_y , 30, 30))
                    pygame.draw.circle(self.screen, (255,255,0), radius = 12, center=(pos_x+15,pos_y+15))
                    pygame.draw.circle(self.screen, (0,0,0), radius = 12,width=2, center=(pos_x+15,pos_y+15))
                  

                if self.matriz[row][col] != 0:
                    pygame.draw.rect(self.screen, (169,169,169), pygame.Rect(pos_x, pos_y, 30, 30), 1)
        
        pygame.draw.circle(self.screen, (255, 255, 255), radius=65,center=(90,190))
        pygame.draw.circle(self.screen, (255, 255, 255), radius=65,center=(360,190))
        pygame.draw.circle(self.screen, (255, 255, 255), radius=65,center=(90,460))
        pygame.draw.circle(self.screen, (255, 255, 255), radius=65,center=(360,460))

     