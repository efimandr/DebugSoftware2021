from my_funcs.utils import integer_division
import pytest

@pytest.mark.parametrize("a, b, expected_result", [(10, 2, 5),
                                                   (20, 10, 2),
                                                   (30, -3, -10),
                                                   (10, 0.5, 20)])

def test_01_good(a, b, expected_result):
    assert integer_division(a, b) == expected_result


@pytest.mark.parametrize("expected_excettion, divider", [(ZeroDivisionError, 0),
                                                         (TypeError, "2")])

def test_01_Zero_error(expected_excettion, divider, divisionable):
    with pytest.raises(expected_excettion):
        integer_division(divisionable, divider)