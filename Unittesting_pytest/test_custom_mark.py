import pytest


@pytest.mark.windows
def test_window_1():
    assert True


@pytest.mark.windows
def test_window_2():
    assert True


@pytest.mark.mac
def test_mac_1():
    assert True

@pytest.mark.mac
def test_mac_1():
    assert True

