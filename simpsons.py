import argparse
import math
from typing import Callable
from dataclasses import dataclass

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
    iterations = 0

    while True:
        iterations += 1
        val_n, relative_first, relative_second = compute_relative_errors(n, params)

        if should_double_n(relative_first, params.tol):
            n *= 2
            continue

        if relative_second is not None and relative_second < params.tol:
            return Result(n, iterations, relative_first, relative_second, val_n)

        if iterations > 1000:
            raise RuntimeError("Maximum iterations exceeded")

        n *= 2

    raise RuntimeError("eval_integral exited unexpectedly") #this is to stop static analysis warnings.


def compute_relative_errors(n: int, params: Input) -> tuple[float, float, float]:

    val_n = simpsons(n, params)
    val_double_n = simpsons(2 * n, params)
    relative_first = get_relative_error(val_n, val_double_n)

    relative_second = None
    if should_double_n(relative_first, params.tol):
        insurance = simpsons(4 * n, params)
        relative_second = get_relative_error(val_double_n, insurance)

    return val_n, relative_first, relative_second


def should_double_n(relative_diff: float, tol: float) -> bool:
    return relative_diff > tol

def simpsons(n: int, params: Input) -> float:
    h = get_h(params.a, params.b, n)

    total_sum = params.f(params.a) + params.f(params.b)

    for i in range(1, n):
        if i % 2 == 0:
            total_sum += 2 * (params.f(params.a + i * h))
        else:
            total_sum += 4 * (params.f(params.a + i * h))

    approx = total_sum * (h / 3)

    return approx

def get_h(a: float, b: float, n: int) -> float:
    return (b-a)/n

def get_relative_error(val_n: float, val_double_n: float) -> float:
    return abs(val_double_n-val_n)/abs(val_double_n)


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--a", type=float, required=True)
    parser.add_argument("--b", type=float, required=True)
    parser.add_argument("--func", type=str, required=True)
    parser.add_argument("--tol", type=float, default=0.01)
    parser.add_argument("--verbose", action="store_true")

    args = parser.parse_args()

    f = get_function(args.func)

    result = eval_integral(Input(args.a, args.b, f, args.tol))

    print (result.estimate)


if __name__ == "__main__":
    main()