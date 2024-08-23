import pytest
from whoisfaster import solve

@pytest.mark.parametrize(
    'a,b,expected',
    (
        [[8, 5, 3, 2, 0, 1, 1], [3, 3, 3, 3, 3, 3, 3],"черепаха"],
        [[8, 5, 3, 2, 2, 1, 1], [3, 3, 3, 3, 3, 3, 3],"заяц"],
        [[8, 5, 3, 2, 1, 1, 1], [3, 3, 3, 3, 3, 3, 3],"одинаково"],
        [[8, 5, 3, -2, 1, 1, 1], [-3, 3, 3, 3, 3, 3, 3],"одинаково"]
    )
)

def test_discriminant_solution_params(a, b, expected):
    result = solve(a, b)
    assert result == expected, f'Ожидается {expected.upper()}, Дистанция зайца {sum(a)}, дистанция черепахи {sum(b)}'