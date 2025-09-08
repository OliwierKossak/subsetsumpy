from .utils import BaseSubsetMethods

class HillClimbingDeterministic(BaseSubsetMethods):

    def __init__(self, basic_set: list[int], target_sum: int, max_iterations: int = 20):
        self.basic_set = basic_set
        self.target_sum = target_sum
        self.max_iterations = max_iterations


