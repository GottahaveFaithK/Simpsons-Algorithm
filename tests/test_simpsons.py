import math
from simpsons import eval_integral, Input

"""
test overall accuracy: constant, linear, quadratic, cubic (these will all have exact solutions)
test n validation: check if both the first and second pass give me an error value that is less than 1%...
try to cause premature convergence??

"""


def test_linear():
    a = 0.0
    b = 1.0
    f = lambda x: x
    tol = 0.00001

    result = eval_integral(Input(a, b, f, tol))

    expected = 0.5

    assert abs(result.estimate - expected) < tol

def test_quadratic():
    a = 0.0
    b = 1.0
    f = lambda x: x**2
    tol = 1e-8

    result = eval_integral(Input(a, b, f, tol))

    expected = 1.0 / 3.0
    assert abs(result.estimate - expected) < tol