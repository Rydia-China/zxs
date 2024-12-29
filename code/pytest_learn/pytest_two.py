import pytest


def test_one():
    assert 1 == 1
    assert 1 != 2
    assert 1 < 2
    assert 3 > 1
    assert 3 <= 3
    assert 3 >= 3
    # 失败了继续执行用pytest.assume
    pytest.assume("d" in "abc")
    pytest.assume("c" not in "abc")
    assert True is True
    assert False is not True
