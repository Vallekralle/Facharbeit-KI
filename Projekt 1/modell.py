import tensorflow as tf
from tensorflow import keras
import numpy as np
from graph import Graph


class Model(tf.keras.Model):
    def __init__(self, x:list, y:list, epochen:int, vorhersage:int):
        super().__init__()
        
        self.x = x
        self.y = y
        self.epochen = epochen
        self.vorhersage = vorhersage
        
        self.modell = tf.keras.Sequential(
            [keras.layers.Dense(units=1, input_shape=[1])]
        )
        
        self.verlustListe = keras.callbacks.History()
        
        self.modellKonfiguration()
        
    
    def modellKonfiguration(self):
        self.modell.compile(optimizer="sgd", loss="mean_squared_error")
        self.modell.fit(
            self.x, self.y, epochs=self.epochen, 
            callbacks=[self.verlustListe]
        )
        
        
    def vorhersagen(self):
        ergebniss = self.modell.predict([self.vorhersage])
        
        print("Ergebniss: " + np.array2string(ergebniss) + "\n" + 
            "Gerundetes Ergebniss: " + np.array2string(np.rint(ergebniss)))


x = [1, 2, 3, 4]
y = [2, 4, 6, 8]

epochen = 10
yZahlVorhersagen = 15

modell = Model(x, y, epochen, yZahlVorhersagen)
vorhersage = modell.vorhersagen()

graph = Graph(epochen, yZahlVorhersagen, modell.verlustListe.history)
