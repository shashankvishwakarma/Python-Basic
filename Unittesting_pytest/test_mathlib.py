import mathlib as m
import pytest
import sys

# @pytest.mark.skip(reason="Ignoring test")
# @pytest.mark.skipif(sys.version_info < (3,5), reason="Ignoring test")
@pytest.mark.skipif(sys.version_info > (3,5), reason="Ignoring test")
def test_calc_total():
    total = m.calc_total(4, 5)
    assert total == 9


def test_calc_multiply():
    result = m.calc_multiply(10, 3)
    assert result == 30

