def fair_sharer(values, num_iterations, share=0.1):
    """
    Runs num_iterations of a fair sharing process.

    In each iteration, the highest value in `values` gives a fraction
    (`share`) of its value to both its left and right neighbors.
    The list is treated as circular (first and last elements are neighbors).

    Args:
        values (list of float or int): Initial values.
        num_iterations (int): Number of iterations.
        share (float): Fraction to share with each neighbor.

    Returns:
        list: Values after all iterations.
    """
    values = list(values)

    n = len(values)

    for _ in range(num_iterations):
        new_values = values.copy()
        max_index = values.index(max(values))
        amount = values[max_index] * share

        left = (max_index - 1) % n
        right = (max_index + 1) % n

        new_values[max_index] -= 2 * amount
        new_values[left] += amount
        new_values[right] += amount

        values = new_values

    return values

