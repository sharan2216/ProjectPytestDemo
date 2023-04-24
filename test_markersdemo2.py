import pytest
import sys

@pytest.mark.skip
def test_login():
    print("Login Done")


@pytest.mark.skipif(sys.version_info>(3,8),reason="python version not supported")
def test_addProduct():
    print("Login Done")



def test_logout():
    print("Login Done")

