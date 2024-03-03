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


# import dataclasses as dc
# @dc.dataclass
# class Result:
#     station: str
#     min: float
#     mean: float
#     max: float

#     @classmethod
#     def from_string(cls, x: str) -> t.Self:
#         station, rest = x.split("=")
#         min, mean, max = rest.split("/")
#         return cls(station, float(min), float(mean), float(max))


# def parse_results(path: str) -> list[Result]:
#     with open(path, "r") as fp:
#         data = fp.read().splitlines()
#     return [Result.from_string(x) for x in data]


# def test_solution1():
#     results = parse_results(RESULTS_PATH)
#     outputs = parse_results(OUTPUTS_PATH)

#     # correct number of stations
#     assert len(results) == len(outputs)

#     actual_stations = [o.station for o in outputs]

#     # unique stations
#     assert len(set(actual_stations)) == len(actual_stations)
