from __future__ import annotations

import pytest
from brc import solution1

MEASUREMENTS_PATH = "./measurements_1000.txt"
RESULTS_PATH = "./results_1000.txt"
OUTPUTS_PATH = "./results_1000.txt"

TEST_DATA_ROOT = "src/test/resources/samples"


@pytest.mark.parametrize(
    "tag",
    [
        "1",
        "2",
        "3",
        "10",
        "20",
        "10000-unique-keys",
        "boundaries",
        "complex-utf8",
        "dot",
        "short",
        "shortest",
        "rounding",
    ],
)
def test_measurements(tag: str):
    with open(f"{TEST_DATA_ROOT}/measurements-{tag}.out", "r") as fp:
        expected = fp.read()

    actual = solution1.solve(f"{TEST_DATA_ROOT}/measurements-{tag}.txt")

    assert expected == actual


@pytest.mark.slow
def test_measurements_full():
    with open(f"{TEST_DATA_ROOT}/measurements.out", "r") as fp:
        expected = fp.read()

    actual = solution1.solve(f"{TEST_DATA_ROOT}/measurements.txt")

    assert expected == actual
