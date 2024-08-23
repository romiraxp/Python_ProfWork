import pytest
from discr_solution import discriminant, solution

@pytest.mark.parametrize(
    'a,b,c,expected',
    (
        [1, 8, 15, "-3.0 -5.0"],
        [1, -13, 12, "12.0 1.0"],
        [-4, 28, -49, "3.5"], # использую здесь строку как ожидаемый результат, но возвращает число и тест Failed
        [1, 1, 1, "корней нет"],
        [1, 0, 0, -1]
    )
)

def test_discriminant_solution_params(a, b, c, expected):
    discriminant(a, b, c)
    result = solution(a, b, c)
    assert result == expected, f"Возвращено значение {result} тип {type(result)} вместо {expected} тип {type(expected)}"
