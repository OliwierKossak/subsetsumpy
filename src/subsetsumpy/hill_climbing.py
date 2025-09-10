import random

from utils import BaseSubsetMethods





class HillClimbingDeterministic(BaseSubsetMethods):

    def __init__(self, basic_set: list[int]):
        self.basic_set = basic_set

    def search_solution(self,target_sum: int,status:bool=False, max_iterations: int = 20):
        """
        Searching for a subset that sums to a given value.

        Args:
            target_sum: The sought sum of the subset.
            status: True display information about current iteration.
            max_iterations: Number of iterations of the subset search process.

        Returns:
            list[int]: found best subset
        """
        loop_index = 0
        current_best_solution = self.generate_subset(self.basic_set)
        best_solution_score = self.evaluate_subset(self.basic_set,current_best_solution, target_sum)

        while loop_index < max_iterations and  best_solution_score != 0:
            neighbours = self.generate_neighbours(current_best_solution)
            current_best_solution = self.__find_best_neighbour(current_best_solution, neighbours, target_sum)
            best_solution_score = self.evaluate_subset(self.basic_set,current_best_solution,target_sum)
            self.__print_loop_iteration(loop_index, best_solution_score,self.basic_set,current_best_solution,status)
            loop_index +=1

        current_best_solution = self.convert_to_decimal_format(self.basic_set, current_best_solution)
        return current_best_solution


# class Hill

# arr = [1,4,2,3,7,-2,9, 10, 11, 12, -5, -6, -3, 8]
# arr2 = [random.randint(-100,100) for x in range(100)]
# target_sum = 35
# hill = HillClimbingDeterministic(arr)
# hill.search_solution(target_sum, status=True)
# print()
# print(hill.search_solution(-20, status=True))
