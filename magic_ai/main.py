## main.py
from genetic_algorithm import GeneticAlgorithm
from neural_network import NeuralNetwork
from dynamic_layer import DynamicLayer
from learning_paradigm import LearningParadigm
from user_interface import UserInterface

if __name__ == "__main__":
    # Initialize genetic algorithm
    ga = GeneticAlgorithm()

    # Initialize neural network
    nn = NeuralNetwork()

    # Initialize dynamic layer
    dl = DynamicLayer()

    # Initialize learning paradigm
    lp = LearningParadigm()

    # Initialize user interface
    ui = UserInterface()

    # Add dynamic layer to neural network
    nn.add_layer(dl.generate())

    # Apply learning paradigm to neural network
    lp.apply_paradigm(nn)

    # Start the genetic algorithm evolution process
    ga.evolve()

    # Run the user interface
    ui.run()
