import numpy as np
class Environment:
    def __init__(self, size_x, size_y) -> None:
        self.size_x = size_x
        self.size_y = size_y
        self.board = np.zeros((self.size_x, self.size_y))