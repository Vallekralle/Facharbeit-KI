import numpy as np
from matplotlib import pyplot as plt


class Graph:
    def __init__(self, epochen:int, vorhersage:int, verlust:dict):
        self.epochen = epochen
        self.vorhersage = vorhersage
        self.verlust = list(verlust.values())
        
        self.setzteVerluste()
        self.erzeugeGraphen()
        plt.show()
        
        
    def erzeugeGraphen(self):
        x = np.arange(0, self.vorhersage + 1, 1)
        y = 2 * x
        
        plt.title("Modell-Verluste")
        plt.xlabel("X-Achse")
        plt.ylabel("Y-Achse")
        plt.plot(x, y, color="black")
        
        
    def setzteVerluste(self):
        x, y, dir, color = 0, 0, 1, "blue"
        
        for i in range(2):
            for i in range(self.epochen):
                x += self.vorhersage / self.epochen
                y = 2 * x + (self.verlust[0][i] * dir)
                plt.plot(x, y, marker="o", color=color)
                
            x, y, dir, color = 0, 0, -1, "red"
