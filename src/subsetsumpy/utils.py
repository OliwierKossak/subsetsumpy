import numpy as np


def convert_to_decimal_format(decimal_subset: list[int], binary_subset: list[int]):
    """
    Convert list with binary mask to list with decimal numbers.

    Args:
        decimal_subset: original list with decimial numbers.
        binary_subset: list with elements in binary mask format.

    Returns:
        list[int] : list with elements converted to decimal format
    """
    converted_list = []
    for index in range(len(binary_subset)):
        if binary_subset[index] == 1:
            converted_list.append(decimal_subset[index])
    return converted_list


def generate_subset(subset: list[int], binary_output: bool = True):
    """
    Generate a random subset of the given list.

    Args:
        subset: list of integers
        binary_output:
            If True, return a binary mask (list of 0/1).
            If False, return the actual elements of subset.
            Default is True

    Returns:
        list[int]: Either a binary mask or the actual subset elements.
    """

    generated_subset = np.random.randint(0, 2, size=len(subset)).tolist()
    if not binary_output:
        generated_subset = convert_to_decimal_format(subset, generated_subset)
    return generated_subset


arr = [1, 4, 3, 6, 5]
t = generate_subset(arr)
print(t)
print(convert_to_decimal_format(arr, t))
