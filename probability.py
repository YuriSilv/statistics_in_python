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

def combination(x: int, y: int) -> int:
    return math.factorial(x) / (math.factorial(y) * math.factorial(x-y))

def binomial_prob(sucess:int, trials:int, prob: float):
    return combination(trials, sucess) * prob**sucess * (1-prob)**(trials-sucess)

def expected_value(xs: list, probs: list) -> float:
    return sum([x*y for x,y in zip(xs, probs)])

def bernoulli_var(p: float) -> float:
    return p*(1-p)

def bernoulli_std(p: float) -> float:
    return math.sqrt(bernoulli_var(p))

def bernoulli_expected_value(p: float, n:int) -> float:
    return n*p

def bernoulli_expected_var(p: float, n:int) -> float:
    return n*p*(1-p)

def poisson_dist(k: float, lamb: float):
    return (lamb**k * math.exp(-lamb)) / math.factorial(k)
