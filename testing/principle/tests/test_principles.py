#TODO make it with `pip install -e .`

from math_demo import (
    add,
    add_with_bug,
    calculate_tax_bugged,
    calculate_tax
)

# [DONE] Ранее тестирование позволяет сэкономить время позднее
# [DONE] Тесты показывают наличие ошибок, а не их отсутствие

# {
#   [DONE] Тесты не должны дублировать логику тестируемого кода
#   [DONE] Тесты не должны делать предположения о внутреннем устройст ве кода
# }

# [DONE] Тесты не должны использовать ВСЕ наборы входных параметров
# [DONE] Тесты должны покрывать "кластеры" входных параметров
# [DONE] Тестовые функции должны тестировать логические блоки

# [DONE] Тесты должны обнаруживать ошибки (perscide paradox)
# Тесты покрывают как успешные так и ошибочные кейсы

def test_addition():
    assert add(2, 2) == 4
    assert add(0, 0) == 0
    assert add(7, 6) == 13
    print("Test addition passed")

def test_addition_with_bug():
    assert add_with_bug(2,2) == 4
    assert add_with_bug(0,0) == 0
    print("Test bugged addition passed")
    # finally we found data that make test reliable
    # assert add_with_bug(7,6) == 13 # will fail here 

def test_addition_duplicate():
    assert add(6,7) == 6+7
    print("Test duplicate addition passed")

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

def test_addition_commutative():
    assert add(9, 5) == 14
    assert add(5, 9) == 14
    print("Tests commutative passed")

def test_tax_calculator_pesticide():
    assert calculate_tax_bugged(1000) == 150
    assert calculate_tax_bugged(100) == 15
    assert calculate_tax_bugged(10) == 1.5
    assert calculate_tax_bugged(1) == 0.15
    assert calculate_tax_bugged(234) == 35.1
    print("Test tax calculator passed")
    # float may give us test cases
    # not available when using int
    # assert calculate_tax_bugged(2.34) == 0.35 # 0.351

def test_tax_calculator():
    assert calculate_tax(1000) == 150
    assert calculate_tax(100) == 15
    assert calculate_tax(10) == 1.5
    assert calculate_tax(1) == 0.15
    assert calculate_tax(234) == 35.1
    print("Test unbugged tax calculator passed")
    assert calculate_tax(2.34) == 0.35 # 0.351

def test_negative_income():
    try:
        calculate_tax(-100)
        print("Test negative income failed")
    except ValueError as e:
        print("Test negative income passed")

if __name__ == "__main__":
    test_addition()
    test_addition_with_bug()
    test_addition_duplicate()
    # test_additional_overkill() # can try it on your risk
    test_addition_clusters()
    test_addition_commutative()
    test_tax_calculator()
    test_tax_calculator_pesticide()
    test_negative_income()

