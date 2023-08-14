import pytest
from src.drake_eq.equation import Equation


@pytest.fixture
def equation():
    return Equation()


def test_estimate(equation):
    assert equation.estimate() == 10


def test_custom_parameters():
    equation = Equation(Rstar=3, fp=1, ne=0.2, fe=0.13,
                        fi=1, fc=0.2, L=1E9)
    assert equation.estimate() == 15_600_000


def test_zero_parameters():
    equation = Equation(Rstar=0, fp=0, ne=0, fe=0, fi=0, fc=0, L=0)
    assert equation.estimate() == 0
