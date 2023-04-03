import math

#baseado no livro "Data Science from Scratch" de Joel Grus
def uniform_pdf(x: float) -> float:
    return 1 if 0 <= x < 1 else 0

def normal_pdf(x:float, mu: float = 0, sigma: float = 1) -> float:
    return 1/math.sqrt(2*math.pi) * math.exp(-0.5*(x-mu)**2)/2*sigma**2

def normal_cdf(x: float, mu: float = 0, sigma: float = 1) -> float:
    return (1 + math.erf((x-mu)/math.sqrt(2)/sigma))/2

def normal_inverse_cdf(p: float, mu: float = 0, sigma: float = 1, tolerance: float = 0.00001) -> float:
    if mu != 0 or sigma != 1:
        return mu + sigma * normal_inverse_cdf(p, tolerance=tolerance)
    low_z = -10.0
    hi_z = 10.0
    while hi_z - low_z > tolerance:
        mid_z = (low_z + hi_z) / 2
        mid_p = normal_cdf(mid_z)
        if mid_p < p:
            low_z = mid_z
        else:
            hi_z = mid_z
    return mid_z

