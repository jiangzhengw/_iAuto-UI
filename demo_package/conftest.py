# Time: 2021/12/29 0:00
# Author: jiangzhw
# FileName: conftest.py
import pytest


@pytest.fixture(scope="session")
def fixturedemo():
    print("执行fixture")
