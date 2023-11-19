## dynamic_layer.py
from tensorflow.keras import layers

class DynamicLayer:
    def __init__(self, layer_size: int = 10, activation: str = 'relu'):
        self.layer_size = layer_size
        self.activation = activation

    def generate(self):
        return layers.Dense(self.layer_size, activation=self.activation)
