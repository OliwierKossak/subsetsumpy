import random

from utils import BaseSubsetMethods


class HillClimbingDeterministic(BaseSubsetMethods):

    def __init__(self, basic_set: list[int]):
        self.basic_set = basic_set

    def __find_best_neighbour(
        self, best_subset: list[int], neighbours: list[list[int]], target_sum: int
    ):
        """
        Searching for the better subset in the generated neighboring solutions.

        Args:
            best_subset: Currently the best subset that will be compared with other subsets.
            neighbours: Adjacent subsets generated from best_subset.
            target_sum: The sought sum of the subset.
        Returns:
            list[int]: Best found subset.

        """
        best_subset_score = self.evaluate_subset(
            self.basic_set, best_subset, target_sum
        )
        current_best_subset = best_subset
        for neighbour in neighbours:
            current_neighbour_score = self.evaluate_subset(
                self.basic_set, neighbour, target_sum
            )
            if best_subset_score > current_neighbour_score:
                current_best_subset = neighbour.copy()
                best_subset_score = current_neighbour_score

        return current_best_subset

    def search_solution(
        self, target_sum: int, status: bool = False, max_iterations: int = 20
    ):
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
        best_solution_score = self.evaluate_subset(
            self.basic_set, current_best_solution, target_sum
        )

        while loop_index < max_iterations and best_solution_score != 0:
            neighbours = self.generate_neighbours(current_best_solution)
            current_best_solution = self.__find_best_neighbour(
                current_best_solution, neighbours, target_sum
            )
            best_solution_score = self.evaluate_subset(
                self.basic_set, current_best_solution, target_sum
            )
            self.print_loop_iteration(
                loop_index,
                best_solution_score,
                self.basic_set,
                current_best_solution,
                status,
            )
            loop_index += 1

        current_best_solution = self.convert_to_decimal_format(
            self.basic_set, current_best_solution
        )
        return current_best_solution


class HillClimbingStochastic(BaseSubsetMethods):

    def __init__(self, basic_set: list[int]):
        self.basic_set = basic_set

    def __find_better_neighbour(
        self, best_subset: list[int], neighbours: list[list[int]], target_sum: int
    ):
        """
        Searching for the best subset in the generated neighboring solutions.

        Args:
            best_subset: Currently the best subset that will be compared with other subsets.
            neighbours: Adjacent subsets generated from best_subset.
            target_sum: The sought sum of the subset.
        Returns:
            list[int]: Best found subset.

        """
        best_subset_score = self.evaluate_subset(
            self.basic_set, best_subset, target_sum
        )
        current_best_subset = best_subset

        for _ in range(len(neighbours)):
            random_index = random.randint(0, len(neighbours) - 1)
            neighbour = neighbours[random_index]
            current_neighbour_score = self.evaluate_subset(
                self.basic_set, neighbour, target_sum
            )
            if best_subset_score > current_neighbour_score:
                current_best_subset = neighbour.copy()
                best_subset_score = current_neighbour_score
                return current_best_subset
            else:
                neighbours.pop(random_index)

        return current_best_subset

    def search_solution(
        self, target_sum: int, status: bool = False, max_iterations: int = 20
    ):
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
        best_solution_score = self.evaluate_subset(
            self.basic_set, current_best_solution, target_sum
        )

        while loop_index < max_iterations and best_solution_score != 0:
            neighbours = self.generate_neighbours(current_best_solution)
            current_best_solution = self.__find_better_neighbour(
                current_best_solution, neighbours, target_sum
            )
            best_solution_score = self.evaluate_subset(
                self.basic_set, current_best_solution, target_sum
            )
            self.print_loop_iteration(
                loop_index,
                best_solution_score,
                self.basic_set,
                current_best_solution,
                status,
            )
            loop_index += 1

        current_best_solution = self.convert_to_decimal_format(
            self.basic_set, current_best_solution
        )
        return current_best_solution


arr = [1, 4, 2, 3, 7, -2, 9, 10, 11, 12, -5, -6, -3, 8]
arr2 = [random.randint(-100, 100) for x in range(100)]
target_sum = 42
hill = HillClimbingDeterministic(arr)
hillStochastic = HillClimbingStochastic(arr)
hillStochastic.search_solution(target_sum=target_sum, status=True)

# hill.search_solution(target_sum, status=True)
# print()
# print(hill.search_solution(-20, status=True))
