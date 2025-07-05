from typing import Union, Optional


def add(x: Union[int, float], y: Union[int, float]) -> Optional[Union[int, float]]:
    try:
        result = x + y
    except Exception as e:
        print(e)
        return None

    return result


# [int, float] 는 정수나 실수가 출력될 수 있음을 의미함

if __name__ == "__main__":
    print(add(1, 2))
    print(add(1.5, 2.5))
    print(add(1, 2.5))
    print(add(1.5, 7))
