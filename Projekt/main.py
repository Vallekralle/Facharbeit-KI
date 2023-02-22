# Module von außen 
import pygame
import time
from PIL import Image

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

# Variablen für die Zeichenflaeche und das Modell
bildBreite, bildHoehe = 300, 300
bloeckeAnzahl = 50 
bloeckListe = []

flaechenBreite = flaechenHoehe = bildBreite / bloeckeAnzahl
flaechenX = flaechenY = BREITE / 2 - flaechenBreite * bloeckeAnzahl / 2

SCHWARZ = (0, 0, 0)

# Variablen für die Knoepfe
zurueckText = startText = ""
zurueckKnf = startKnf = object
font = pygame.font.SysFont("monospace", 25)
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
                    bildschirmFoto()
                    
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
    x, y = flaechenX, flaechenY
    
    erzeugeZurueckKnf(y)
    
    for _ in range(bloeckeAnzahl):
        for _ in range(bloeckeAnzahl):
            bloeckListe.append(Bloecke(x, y, flaechenBreite, 
                                       flaechenHoehe, (240, 240, 240)))
            x += flaechenBreite
        y += flaechenHoehe
        x = x - flaechenBreite * bloeckeAnzahl
        
    erzeugeStartKnf(y)
    

def erzeugeZurueckKnf(pY):
    global zurueckText
    global zurueckKnf
    
    # Der Text für den Knopf
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
            
            
def bildschirmFoto():
    global bild
    
    # Screenshot machen und Bild speichern
    datum = str(time.ctime()).replace(":", "-") + ".png"
    bild = FENSTER.subsurface(pygame.Rect(flaechenX, flaechenY, 
                                          bildBreite, bildHoehe))
    pygame.image.save(bild, pfad + datum)
    
    # Bildgroesse aendern und speichern
    bild = Image.open(pfad + datum)
    neueGroesse = bild.resize((28, 28))
    neueGroesse.save(pfad + datum)
    


if __name__ == '__main__':
    main()
    
pygame.quit()
