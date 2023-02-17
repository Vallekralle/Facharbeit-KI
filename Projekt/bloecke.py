import pygame
pygame.init()


class Bloecke:
    SCHWARZ = (0, 0, 0)
    
    def __init__(self, x, y, breite, hoehe, farbe):
        self.x = x
        self.y = y
        self.breite = breite
        self.hoehe = hoehe
        self.farbe = farbe
        
        self.rect = pygame.Rect(self.x, self.y, self.breite, self.hoehe)
        
        
    def gedrueckt(self, mousePos):
        if (self.x <= mousePos[0] <= self.x + self.breite and
            self.y <= mousePos[1] <= self.y + self.hoehe):
                return True
        
        
    def zeichnen(self, win):
        pygame.draw.rect(win, self.farbe, (self.x, self.y, self.breite, self.hoehe))
