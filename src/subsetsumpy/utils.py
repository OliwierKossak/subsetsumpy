import numpy as np





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
    print(len(subset))
    generate_subset = np.random.randint(0,2, size=len(subset)).tolist()
    print(generate_subset)

generate_subset([1,4,3,6,5])


