## neural_network.py
import tensorflow as tf
from tensorflow.keras import layers

class NeuralNetwork:
    def __init__(self, input_shape: tuple = (10,), output_shape: int = 1):
        self.input_shape = input_shape
        self.output_shape = output_shape
        self.model = tf.keras.Sequential()

    def add_layer(self, layer_size: int = 10, activation: str = 'relu'):
        if not self.model.layers:
            self.model.add(layers.Dense(layer_size, activation=activation, input_shape=self.input_shape))
        else:
            self.model.add(layers.Dense(layer_size, activation=activation))

    def compile_model(self, optimizer: str = 'adam', loss: str = 'mean_squared_error'):
        self.model.compile(optimizer=optimizer, loss=loss)

    def train(self, x_train, y_train, epochs: int = 10, batch_size: int = 32):
        self.model.fit(x_train, y_train, epochs=epochs, batch_size=batch_size)

    def predict(self, x_test):
        return self.model.predict(x_test)
