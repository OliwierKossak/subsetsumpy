from utils import BaseSubsetMethods

class HillClimbingDeterministic(BaseSubsetMethods):

    def __init__(self, basic_set: list[int], target_sum: int, max_iterations: int = 20):
        self.basic_set = basic_set
        self.target_sum = target_sum
        self.max_iterations = max_iterations

    def __find_best_neighbour(self, best_subset: list[int],neighbours: list[list[int]]):
        best_subset_score = self.evaluate_subset(self.basic_set, best_subset, self.target_sum)
        current_best_subset = best_subset
        for neigbour in neighbours:
            current_neigbour_score = self.evaluate_subset(self.basic_set, neigbour, self.target_sum)
            if best_subset_score > current_neigbour_score:
                current_best_subset = neigbour.copy()
                best_subset_score = current_neigbour_score

        return current_best_subset



    def search_solution(self):
        loop_index = 0
        current_best_solution = self.generate_subset(self.basic_set)
        best_solution_score = self.evaluate_subset(self.basic_set,current_best_solution, self.target_sum)

        while loop_index < 20 and  best_solution_score != 0:
            neighbours = self.generate_neighbours(current_best_solution)
            current_best_solution = self.__find_best_neighbour(current_best_solution, neighbours)
            best_solution_score = self.evaluate_subset(self.basic_set,current_best_solution,self.target_sum)
            print(best_solution_score, current_best_solution)

# arr = [1,4,2,3,7,-2,9]
# target_sum = 5
# hill = HillClimbingDeterministic(arr, target_sum)
# hill.search_solution()
