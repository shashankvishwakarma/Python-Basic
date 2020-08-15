import mathlib as m


def test_calc_total():
    total = m.calc_total(4, 5)
    assert total == 9


def test_calc_multiply():
    result = m.calc_multiply(10, 3)
    assert result == 30


'''
# to run
python -m test
py.test
'''