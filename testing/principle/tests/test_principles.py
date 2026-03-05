#TODO make it with `pip install -e .`

from math_demo import (
    add,
    add_with_bug
)

# Ранее тестирование позволяет сэкономить время позднее
# 


def test_addition():
    assert add(2, 2) == 4
    assert add(0, 0) == 0
    assert add(7, 6) == 13
    print("Test addition passed")

def test_addition_with_bug():
    assert add_with_bug(2,2) == 4
    assert add_with_bug(0,0) == 0
    print("test bugged addition passed")
    # finally we found data that make test reliable
    # assert add_with_bug(7,6) == 13 # will fail here 

if __name__ == "__main__":
    test_addition()
    test_addition_with_bug()