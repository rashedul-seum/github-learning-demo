def calculate_mean(values):
    """Return the arithmetic mean of a sequence of numbers."""
    if not values:
        raise ValueError("values cannot be empty")

    return sum(values) / len(values)


def calculate_range(values):
    """Return the difference between the maximum and minimum values."""
    if not values:
        raise ValueError("values cannot be empty")

    return max(values) - min(values)