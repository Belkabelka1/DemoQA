import pytest


# будет пропущен
@pytest.mark.skip
def test_skip():
    assert True


# будет условно прошедшим
@pytest.mark.xfail()
def test_xfail_true():
    assert True


# будет условно упавшим
@pytest.mark.xfail()
def test_xfail_false():
    assert False


# будет пропущен
@pytest.mark.skipif(2 + 2 != 3, reason="Причина")
def test_skipif():
    assert True


# запустится 5 тестов (2- фэйл, 3 - пасст)
@pytest.mark.parametrize('param', [1, 2, 3, 4, 6])
def test_parametrize(param):
    assert (param % 2) == 0
