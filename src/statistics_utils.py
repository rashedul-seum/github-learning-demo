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


def calculate_median(values):
    """Return the median of a sequence of numbers."""
    if not values:
        raise ValueError("values cannot be empty")

    sorted_values = sorted(values)
    n = len(sorted_values)
    midpoint = n // 2

    if n % 2 == 1:
        return sorted_values[midpoint]

    return (
        sorted_values[midpoint - 1] + sorted_values[midpoint]
    ) / 2