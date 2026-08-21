from statistics_utils import calculate_mean, calculate_range


def greet(name):
    """Return a personalized greeting."""
    return f"Hello, {name}! Welcome to my Git learning project."


def square(number):
    """Return the square of a number."""
    return number ** 2


if __name__ == "__main__":
    scores = [91, 85, 94, 88]

    print(greet("GitHub"))
    print(f"The square of 5 is {square(5)}.")
    print(f"Mean score: {calculate_mean(scores):.2f}")
    print(f"Score range: {calculate_range(scores)}")