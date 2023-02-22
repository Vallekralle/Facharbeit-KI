# Modul von außen
import tensorflow as tf


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
    # Trainingssätze und Testsätze für KNN
    datenSatz = tf.keras.datasets.mnist
    (xTraining, yTraining), (xTest, yTest) = datenSatz.load_data()

    xTraining = tf.keras.utils.normalize(xTraining, axis=1)
    xTest = tf.keras.utils.normalize(xTest, axis=1)
    
    # Training
    modell = Modell(xTraining, yTraining, name)
    modell.traniereModell()

    print("_______Fertig mit trainieren, nun wird getestet!_______")

    # Testen
    modell = tf.keras.models.load_model(name)
    verlust, ganauigkeit = modell.evaluate(xTest, yTest)

    print(f"Der Verlust liegt bei: {verlust} " +
        f"und die Genauigkeit bei: {ganauigkeit * 100}")


if __name__ == "__main__":
    main()
