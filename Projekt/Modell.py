# Modul von außen
import tensorflow as tf
import sys


class Modell:
    def __init__(self, xTraining, yTraining, name):
        self.xTraining = xTraining
        self.yTraining = yTraining
        self.name = name
        
        self.modell = tf.keras.models.Sequential()
        
        self.createModell()
        
        self.modell.compile(
            optimizer="adam", loss="sparse_categorical_crossentropy",
            metrics=["accuracy"]
        )
        
        
    def createModell(self):
        # Eingabeschicht
        self.modell.add(tf.keras.layers.Flatten(
            input_shape=(28, 28)
            )
        )
        
        # verborgene Schichten
        self.modell.add(tf.keras.layers.Dense(
            128, activation="relu"
            )
        )
        self.modell.add(tf.keras.layers.Dense(
            128, activation="relu"
            )
        )
        self.modell.add(tf.keras.layers.Dense(
            10, activation="softmax"
            )
        )
        
        
    def traniereModell(self):
        self.modell.fit(self.xTraining, self.yTraining, epochs=1)
        self.modell.save(self.name)


name = "HandschriftModell"


def main():
    datenSatz = tf.keras.datasets.mnist
    (xTraining, yTraining), (xTest, yTest) = datenSatz.load_data()
    
    auswahl = int(input("Möchtest du trainieren(1) oder testen(2)? " + 
                        "(3 zum verlassen): "))
        
    try:
        if auswahl == 1:
            # Trainingssätze und Testsätze für KNN
            xTraining = tf.keras.utils.normalize(xTraining, axis=1)
            xTest = tf.keras.utils.normalize(xTest, axis=1)
                
            # Training
            modell = Modell(xTraining, yTraining, name)
            modell.traniereModell()
            

        if auswahl == 2:
            # Testen
            modell = tf.keras.models.load_model(name)
            verlust, ganauigkeit = modell.evaluate(xTest, yTest)

            print(f"Der Verlust liegt bei: {verlust} " +
                f"und die Genauigkeit bei: {ganauigkeit * 100}")
        
        sys.exit() if auswahl == 3 else False
        
        main()
    
    except Exception as e:
        print(e)
        main()


if __name__ == "__main__":
    main()
