#TODO make it with `pip install -e .`

from math_demo import (
    add,
    add_with_bug
)

# [DONE] Ранее тестирование позволяет сэкономить время позднее
# [DONE] Тесты показывают наличие ошибок, а не их отсутствие

# {
#   [DONE] Тесты не должны дублировать логику тестируемого кода
#   [DONE] Тесты не должны делать предположения о внутреннем устройст ве кода
# }

# [DONE] Тесты не должны использовать ВСЕ наборы входных параметров
# Тесты должны покрывать "кластеры" входных параметров
# Тесты должны обнаруживать ошибки (perscide paradox)
# Тесты покрывают как успешные так и ошибочные кейсы

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

def test_addition_duplicate():
    assert add(6,7) == 6+7
    print("test duplicate addition passed")

def test_addition_overkill():
    for i in range(0, 2**32):
        for j in range(0, 2**64):
            assert add(i, j) == i+j # violation of duplication
            assert add(-i, j) == -i + j
            assert add(-i, -j) == -i - j
            assert add(i, -j) == i-j

def test_addition_clusters():
    assert add(7, 6) == 13
    assert add(0, 6) == 6
    assert add(7, 0) == 7
    assert add(10, -11) == -1
    assert add(-10, -11) == -21
    assert add(-5, 0) == -5
    assert add(0, -2) == -2
    print("Test clusters passed")

if __name__ == "__main__":
    test_addition()
    test_addition_with_bug()
    test_addition_duplicate()
    # test_additional_overkill() # can try it on your risk
    test_addition_clusters()

