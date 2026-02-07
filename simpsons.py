import argparse
import math
from typing import Callable
from dataclasses import dataclass


"""
1. break into even number n intervals
    n must be even
    pick small even n
        compute
    double n
        compute
    compare results (with relative error, wanting less than 1%) abs(n2 - n1)/abs(n2)
    n needs a cap

2. take parabolic fits
3. add up weighted values

4. multiply that by ((b-a)/n)/3

take only straight functions like linear, quadratic, constant, this is not a parser project
"""
@dataclass
class Result:
    n: int
    iterations: int
    rel_diff_2n_n: float
    rel_diff_4n_2n: float
    estimate: float

@dataclass
class Input:
    a: float
    b: float
    f: Callable[[float], float]
    tol: float

func_map: dict[str, Callable[[float], float]] = {
    "linear": lambda x: x,
}

def get_function(function: str) -> Callable[[float], float]:
    try:
        return func_map[function]
    except KeyError:
        raise ValueError(f"Unknown function: {function}")


def eval_integral(params: Input) -> Result:
    n = 2
    #TODO return result


def simpsons():
    pass


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--a", type=float, required=True)
    parser.add_argument("--b", type=float, required=True)
    parser.add_argument("--func", type=str, required=True)
    parser.add_argument("--tol", type=float, default=0.01)
    parser.add_argument("--verbose", action="store_true")

    args = parser.parse_args()

    f = get_function(args.func)




if __name__ == "__main__":
    main()