import math


# copied from go implementation:
# https://github.com/marktodisco/1brc/blob/main/src/main/go/AlexanderYastrebov/calc.go
def java_round(x: float) -> float:
    t = int(x)

    if x < 0 and t - x == 0.5:
        pass
    elif abs(x - t) >= 0.5:
        t += math.copysign(1, x)

    if t == 0:
        return 0.0

    return float(t)
