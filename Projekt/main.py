# Module von außen
import pygame
import time
from PIL import ImageGrab

# Eigene Module
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
bloeckListe = []
SCHWARZ = (0, 0, 0)

# Variablen für die Knoepfe
zurueckText = startText = ""
zurueckKnf = startKnf = object
ROT = (255, 0, 0)
GRUEN = (0, 255, 0)

# Attribute für die Bilder
pfad = "Projekt/img/"
bild = object


def main():
    global bloeckListe
    
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
                
                if zurueckKnf.gedrueckt(pygame.mouse.get_pos()):
                    # Liste leeren, damit sich die Bloecke nicht stappeln
                    bloeckListe = [] 
                    erzeugeZeichenFlaeche()
                    
                if startKnf.gedrueckt(pygame.mouse.get_pos()):
                    bildschrimFoto()
                    
            if pressed == True or event.type == pygame.MOUSEMOTION and pressed == True:
                malen(pygame.mouse.get_pos())
            
        zeichnen(FENSTER)


def zeichnen(pFenster):
    pFenster.fill(WEIß)
    
    # Alle Bloecke der Zeichenflaeche
    for bloeck in bloeckListe:
        bloeck.zeichnen(pFenster)
        
    # Zeichne den Zurueckknopf mit seinem Text
    zurueckKnf.zeichnen(pFenster)
    pFenster.blit(zurueckText, 
                (zurueckKnf.x + (zurueckKnf.breite // 2 - zurueckText.get_width() // 2), 
                zurueckKnf.y + (zurueckKnf.hoehe // 2 - zurueckText.get_height() // 2)))
    
    # Zeichne den Startknopf mit seinem Text
    startKnf.zeichnen(pFenster)
    pFenster.blit(startText, (startKnf.x + (startKnf.breite // 2 - startText.get_width() // 2), 
                startKnf.y + (startKnf.hoehe // 2 - startText.get_height() // 2)))
    
    pygame.display.update()
    
    
def erzeugeZeichenFlaeche():
    breite = hoehe = bildBreite / bloeckeAnzahl
    x = y = BREITE / 2 - breite * bloeckeAnzahl / 2
    
    erzeugeZurueckKnf(y)
    
    for _ in range(bloeckeAnzahl):
        for _ in range(bloeckeAnzahl):
            bloeckListe.append(Bloecke(x, y, breite, hoehe, 
                                         (240, 240, 240)))
            x += breite
        y += hoehe
        x = x - breite * bloeckeAnzahl
        
    erzeugeStartKnf(y)
    

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


def erzeugeStartKnf(pY):
    global startText
    global startKnf
    
    # Der Text für den Knopf
    font = pygame.font.SysFont("monospace", 25)
    startText = font.render("starten", 1, (0, 0, 0))
    
    # Der Knopf
    x = BREITE // 2 - startText.get_width() // 2
    startKnf = Bloecke(x, pY + startText.get_height() * 2, 
                         startText.get_width() + 10, 
                         startText.get_height() + 10, 
                         GRUEN)


def malen(mousePos):
    # Wechsel die Farbe des gedrückten Blockes
    for bloeck in bloeckListe:
        if bloeck.gedrueckt(mousePos):
            bloeck.farbe = SCHWARZ
            
            
def bildschrimFoto():
    global bild
    
    bild = ImageGrab.grab(bbox=(0, 0, BREITE, HOEHE))
    datum = str(time.ctime()).replace(":", "-") + ".png"
    bild.save(pfad + datum, "png")


if __name__ == '__main__':
    main()
    
pygame.quit()
