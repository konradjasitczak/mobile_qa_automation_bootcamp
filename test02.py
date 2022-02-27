import pytest

@pytest.mark.xfail(reason="Unable to execute test")
def test_02():
    print("Execute test case 2")