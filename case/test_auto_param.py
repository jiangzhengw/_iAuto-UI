# Time: 2021/9/2 16:43
# Author: jiangzhw
# FileName: test_auto_param.py
import pytest

from common.common import auto_parametrize


class TestAutoParam:
    params = [
        (1, 2, 3, 4, 5, 6, 7),
        (7, 6, 5, 4, 3, 2, 1),
    ]

    @pytest.mark.parametrize('a, b, c, d, e, f, g', params)
    def test_many_args1(self, a, b, c, d, e, f, g):
        assert a + b + c + d + e + f + g == 28

    @auto_parametrize(params)
    def test_many_args2(self, a, b, c, d, e, f, g):
        assert a + b + c + d + e + f + g == 28
