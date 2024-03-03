import dataclasses as dc
from collections import defaultdict
from brc.rounding import java_round


@dc.dataclass
class Station:
    _min: int = dc.field(default=int(+1_000_000), init=False)
    _max: int = dc.field(default=int(-1_000_000), init=False)
    _sum: int = dc.field(default=0, init=False)
    _count: int = dc.field(default=0, init=False)

    def update(self, x: int) -> None:
        self._min = min(self._min, x)
        self._max = max(self._max, x)
        self._sum += x
        self._count += 1

    def get_min(self) -> float:
        return self._min / 10

    def get_mean(self) -> float:
        return java_round(self._sum / self._count) / 10

    def get_max(self) -> float:
        return self._max / 10

    def str(self, name: str) -> str:
        return f"{name}={self.get_min():.1f}/{self.get_mean():.1f}/{self.get_max():.1f}"


def solve(path: str) -> str:
    with open(path, "r") as fp:
        data = fp.read().splitlines()

    stations: dict[str, Station] = defaultdict(Station)

    for line in data:
        name, temperature = line.split(";")
        temp_x10 = temperature.replace(".", "")
        stations[name].update(int(temp_x10))

    sorted_stations = dict(sorted(stations.items(), key=lambda x: x[0]))

    return (
        "{"
        + ", ".join(station.str(name) for name, station in sorted_stations.items())
        + "}\n"
    )
