from script import sum, devide

def test_sum():
    a=1
    b=2
    result = 3
    assert sum(a,b) == result

def test_devide():
    a = 2
    b = 4
    result = 0.5
    assert devide(a,b) == result

def test_devide_zero():
    a = 8
    b = 4
    try:
        sum(a,b)
        assert True
    except ValueError as e:
        print("Test (zero-devision) passed")

def test_devision_prohibited():
    try:
        devide("A","B")
        assert False
    except ValueError as e:
        print("Test string-devision passed")

if __name__ == "__main__":
    test_devide()
    test_sum()
    test_devide_zero()
    test_devision_prohibited()