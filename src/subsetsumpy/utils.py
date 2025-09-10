import numpy as np


class BaseSubsetMethods:

    def convert_to_decimal_format(self, basic_set: list[int], binary_subset: list[int]):
        """
        Convert list with binary mask to list with decimal numbers.

        Args:
            basic_set: original list with decimial numbers.
            binary_subset: list with elements in binary mask format.

        Returns:
            list[int] : list with elements converted to decimal format
        """

        if not isinstance(basic_set, list):
            raise TypeError("basic_set must be a list of integers.")

        if not isinstance(binary_subset, list):
            raise TypeError("binary_subset must be a list of integers.")

        converted_list = []
        for index in range(len(binary_subset)):
            if binary_subset[index] == 1:
                converted_list.append(basic_set[index])
        return converted_list

    def generate_subset(self, basic_set: list[int], binary_output: bool = True):
        """
        Generate a random subset of the given list.

        Args:
            basic_set: Original list with decimial numbers.
            binary_output:
                If True, return a binary mask (list of 0/1).
                If False, return the actual elements of subset.
                Default is True

        Returns:
            list[int]: Either a binary mask or the actual subset elements.
        """
        if not isinstance(basic_set, list):
            raise TypeError("basic_set must be a list of integers.")

        if not isinstance(binary_output, bool):
            raise TypeError("binary_output must be a list of bool.")

        generated_subset = np.random.randint(0, 2, size=len(basic_set)).tolist()
        if not binary_output:
            generated_subset = convert_to_decimal_format(basic_set, generated_subset)
        return generated_subset

    def evaluate_subset(
        self, basic_set: list[int], binary_subset: list[int], target_sum: int
    ):
        """
        Evaluates a given subset. Perfect score for subset is 0,
            that means subset have same sum as target sum.

        Args:
            basic_set: Original list with decimial numbers.
            binary_subset: List with elements in binary mask format.
            target_sum: Sought sum of subset.
        Returns:
            int: Calculated score of given subset.
        """

        if not isinstance(basic_set, list):
            raise TypeError("basic_set must be a list of integers.")

        if not isinstance(binary_subset, list):
            raise TypeError("binary_subset must be a list of integers.")

        if not isinstance(target_sum, int):
            raise TypeError("target_sum must be an integer.")

        sum_of_subset = sum(self.convert_to_decimal_format(basic_set, binary_subset))
        score = abs(target_sum - sum_of_subset)

        return score

    def invert_binary_number(self, binary_number: int):
        """
        Invert binary number. 0 -> 1 , 1 -> 0.

        Args:
            binary_number: Binary number that will inverted.

        Returns:
            int: Binary number.
        """
        if not isinstance(binary_number, int):
            raise TypeError(f"Expected int, got {type(binary_number).__name__}")
        if binary_number not in (0, 1):
            raise ValueError(f"Expected 0 or 1, got {binary_number}")
        return 0 if binary_number == 1 else 1

    def generate_neighbours(self, binary_subset: list[int]):
        """
        Generates neigbours subsets basis on given subset.

        Args:
            binary_subset:  List with elements in binary mask format.
        Returns:
            list[list[int]]: List with neigbours in binary mask format.
        """

        if not isinstance(binary_subset, list):
            raise TypeError("binary_subset must be a list of integers.")

        neighbours = [binary_subset]

        for index in range(len(binary_subset)):
            new_neighbour = binary_subset.copy()
            new_neighbour[index] = self.invert_binary_number(new_neighbour[index])
            neighbours.append(new_neighbour)
        return neighbours

    def __print_loop_iteration(self, iter: int, score: int, basic_set: list[int], best_subset_binary: list[int],status:bool=False):
        """
        Displays the best subset found in each iteration of the loop.

        Args:
            iter: Current loop iteration.
            score: Points scored by the subset.
            basic_set: The set for which the subset satisfying the sum is sought
            best_subset_binary: Best found subset in current iteration, format binary mask.
            status: True display information about current iteration.
        """
        if status:
            subset_decimal_format = self.convert_to_decimal_format(basic_set,best_subset_binary)
            print(f"Iter: {iter} | Score: {score} | Subset: {subset_decimal_format}")


    def __find_best_neighbour(self, best_subset: list[int],neighbours: list[list[int]], target_sum: int):
        """
        Searching for the best subset in the generated neighboring solutions.

        Args:
            best_subset: Currently the best subset that will be compared with other subsets.
            neighbours: Adjacent subsets generated from best_subset.
            target_sum: The sought sum of the subset.
        Returns:
            list[int]: Best found subset.

        """
        best_subset_score = self.evaluate_subset(self.basic_set, best_subset, target_sum)
        current_best_subset = best_subset
        for neigbour in neighbours:
            current_neigbour_score = self.evaluate_subset(self.basic_set, neigbour, target_sum)
            if best_subset_score > current_neigbour_score:
                current_best_subset = neigbour.copy()
                best_subset_score = current_neigbour_score

        return current_best_subset
