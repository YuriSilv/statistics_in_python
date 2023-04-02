from typing import List
from collections import Counter
from math import sqrt

def mean(xs: List[float]) -> float:
    return sum(xs) / len(xs)

def weighted_avg(xs: List[float], ws: List[float]) -> float:
    return sum([a*b for a,b in zip(xs, ws)]) / len(xs)

def median(xs: List[float]) -> float:
    if (xs%2 == 0):
        return mean([xs[int((len(xs)+1)/2)], xs[int((len(xs)-1)/2)]])
    else:
        return xs[int((len(xs)-1)/2)]

def mode(xs: List[float]) -> float:
    return Counter(xs).most_common(1)[0][0]

def quantil(xs: List[float], p: float) -> float:
    sorted_xs = sorted(xs)
    return sorted_xs[int(len(sorted_xs)*p)]

def range_amp(xs: List[float]) -> float:
    return max(xs) - min(xs)

def IQR(xs: List[float]) -> float:
    return quantil(xs, 0.75) - quantil(xs, 0.25) 

def var(xs: List[float]) -> float:
    avg = mean(xs)
    return sum([(val-avg)**2 for val in xs])/ len(xs)-1

def std(xs: List[float]) -> float:
    return sqrt(var(xs))

def z_index(avg: float, std:float, value:float) -> float:
    return (value-avg)/std