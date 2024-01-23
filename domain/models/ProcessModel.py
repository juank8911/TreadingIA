class ProcessModel:

    def __init__(self, algorithm, parameters):
        self.algorithm = algorithm
        self.parameters = parameters

    def __repr__(self):
        return f"ProcessModel(algorithm={self.algorithm}, parameters={self.parameters})"