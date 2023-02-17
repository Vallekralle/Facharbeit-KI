import pygame
from bloecke import Bloecke
pygame.init()


# Pygame Variablen zum einstellen des Fensters
BREITE, HOEHE = 700, 700
FENSTER = pygame.display.set_mode((BREITE, HOEHE))
pygame.display.set_caption(
    "KI zum Erkennen von handgeschriebenen Zahlen")
FPS = 120
WEIß = (255, 255, 255)

# Bildbreite für Raster und Modell festlegen
bildBreite, bildHoehe = 300, 300


# Variablen der Zeichenflaeche
bloeckeAnzahl = 50 
rasterBloecke = []
SCHWARZ = (0, 0, 0)

# Variablen für die Knoepfe
zurueckText = startText = ""
zurueckKnf = startenKnf = object
ROT = (255, 0, 0)


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
                if zurueckKnf.gedrueckt(pygame.mouse.get_pos()):
                    erzeugeZeichenFlaeche()
                pressed = False
            if event.type == pygame.MOUSEMOTION and pressed == True:
                malen(pygame.mouse.get_pos())
            
        zeichnen(FENSTER)


def zeichnen(pFenster):
    pFenster.fill(WEIß)
    
    for bloeck in rasterBloecke:
        bloeck.zeichnen(pFenster)
        
    zurueckKnf.zeichnen(pFenster)
    pFenster.blit(zurueckText, 
                (zurueckKnf.x + (zurueckKnf.breite // 2 - zurueckText.get_width() // 2), 
                zurueckKnf.y + (zurueckKnf.hoehe // 2 - zurueckText.get_height() // 2)))
    
    pygame.display.update()
    
    
def erzeugeZeichenFlaeche():
    breite = hoehe = bildBreite / bloeckeAnzahl
    x = y = BREITE / 2 - breite * bloeckeAnzahl / 2
    
    erzeugeZurueckKnf(y)
    
    for _ in range(bloeckeAnzahl):
        for _ in range(bloeckeAnzahl):
            rasterBloecke.append(Bloecke(x, y, breite, hoehe, 
                                         (240, 240, 240)))
            x += breite
        y += hoehe
        x = x - breite * bloeckeAnzahl
    

def erzeugeZurueckKnf(pY):
    global zurueckText
    global zurueckKnf
    
    # Der Text für den Knopf
    font = pygame.font.SysFont("monospace", 25)
    zurueckText = font.render("zurück", 1, (0, 0, 0))
    
    # Der Knopf
    x = BREITE // 2 - zurueckText.get_width() // 2
    zurueckKnf = Bloecke(x, pY - zurueckText.get_height() * 2, 
                         zurueckText.get_width() + 10, 
                         zurueckText.get_height() + 10, 
                         ROT)


def malen(mousePos):
    for bloeck in rasterBloecke:
        if bloeck.gedrueckt(mousePos):
            bloeck.farbe = SCHWARZ


if __name__ == '__main__':
    main()
    
pygame.quit()
