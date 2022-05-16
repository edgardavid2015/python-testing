import pytest


@pytest.mark.xfail()
def test_passing():
    assert (1, 2, 3) == (3, 2, 3)
