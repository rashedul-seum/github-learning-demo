from src.statistics_utils import (
    calculate_mean,
    calculate_median,
    calculate_range,
)


def test_calculate_mean():
    assert calculate_mean([2, 4, 6]) == 4


def test_calculate_median_odd():
    assert calculate_median([1, 3, 2]) == 2


def test_calculate_median_even():
    assert calculate_median([1, 2, 3, 4]) == 2.5


def test_calculate_range():
    assert calculate_range([2, 5, 11]) == 9