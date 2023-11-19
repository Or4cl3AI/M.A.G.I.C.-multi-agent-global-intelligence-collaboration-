## memory_module.py
class MemoryModule:
    def __init__(self, learned_information: list = None):
        if learned_information is None:
            learned_information = []
        self.learned_information = learned_information

    def store_information(self, information):
        self.learned_information.append(information)

    def retrieve_information(self):
        return self.learned_information
