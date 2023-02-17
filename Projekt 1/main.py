import pygame
from bloecke import Bloecke
from threading import Thread
pygame.init()


# Pygame Variablen zum einstellen des Fensters
BREITE, HOEHE = 700, 700
FENSTER = pygame.display.set_mode((BREITE, HOEHE))
pygame.display.set_caption("KI zum Erkennen von handgeschriebenen Zahlen")

FPS = 60
WEIß = (255, 255, 255)


# Bildbreite für Raster und Modell festlegen
bildBreite, bildHoehe = 300, 300


# Attribute der Zeichenflaeche
bloeckeAnzahl = 30 
rasterBloecke = []
SCHWARZ = (0, 0, 0)

def main():
    laufen = True
    pressed = bool
    
    erzeugeZeichenFlaeche()
    
    while(laufen):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                laufen = False
                break
            if event.type == pygame.MOUSEBUTTONDOWN:
                pressed = True
            if event.type == pygame.MOUSEBUTTONUP:
                pressed = False
            if event.type == pygame.MOUSEMOTION and pressed == True:
                malen(pygame.mouse.get_pos())
            
        zeichnen(FENSTER)


def zeichnen(pFenster):
    pFenster.fill(WEIß)
    
    for bloeck in rasterBloecke:
        bloeck.zeichnen(pFenster)
    
    pygame.display.update()
    
    
def erzeugeZeichenFlaeche():
    breite = hoehe = bildBreite / bloeckeAnzahl
    x = y = BREITE / 2 - breite * bloeckeAnzahl / 2
    
    for _ in range(bloeckeAnzahl):
        for _ in range(bloeckeAnzahl):
            rasterBloecke.append(Bloecke(x, y, breite, hoehe, (0, 255, 0)))
            x += breite
        y += hoehe
        x = BREITE // 2 - breite * bloeckeAnzahl // 2
    

def malen(mousePos):
    for bloeck in rasterBloecke:
        if bloeck.clicked(mousePos):
            bloeck.farbe = SCHWARZ


if __name__ == '__main__':
    main()
    
pygame.quit()
