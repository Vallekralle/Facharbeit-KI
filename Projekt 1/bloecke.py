import pygame
pygame.init()


class Bloecke:
    SCHWARZ = (0, 0, 0)
    
    def __init__(self, x, y, width, height, farbe):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.farbe = farbe
        
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        
        
    def clicked(self, mousePos):
        if (self.x <= mousePos[0] <= self.x + self.width and
            self.y <= mousePos[1] <= self.y + self.height):
                return True
        
        
    def zeichnen(self, win):
        pygame.draw.rect(win, self.farbe, (self.x, self.y, self.width, self.height))
