from src.fairsharer import fair_sharer


def test_example_one_iteration():
    assert fair_sharer([0, 1000, 800, 0], 1) == [100, 800, 900, 0]


def test_example_two_iterations():
    assert fair_sharer([0, 1000, 800, 0], 2) == [100, 890, 720, 90]

