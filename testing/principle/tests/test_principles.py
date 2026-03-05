#TODO make it with `pip install -e .`

from math_demo import (
    add,
    add_with_bug
)

# [DONE] Ранее тестирование позволяет сэкономить время позднее
# [DONE] Тесты показывают наличие ошибок, а не их отсутствие

# [DONE] Тесты не должны дублировать логику тестируемого кода
# Тесты не должны делать предположения о внутреннем устройстве кода

# Тесты не должны использовать ВСЕ наборы входных параметров
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

if __name__ == "__main__":
    test_addition()
    test_addition_with_bug()
    test_addition_duplicate()