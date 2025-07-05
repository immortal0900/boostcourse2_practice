import pytest
from typing import Union
from main import add


# parametrize 는 내가 테스트 해보고 싶은 인자들을 넣어서 자동으로 수행해줌
@pytest.mark.parametrize(
    "a, b, expected", [(1, 2, 3), (1.0, 2.0, 3.0), (0, 0, 0), (-1, -1, -2)]
)
def test_add(a: Union[int, float], b: Union[int, float], expected: Union[int, float]):
    result = add(a, b)
    assert result == expected
