import os
import pytest
import sys
sys.path.append(os.path.split(os.path.dirname(__file__))[0])
from TestServices.Config.get_test_input import GetTestInput
from TestServices.AccessMethods.run_build_mail_address import RunBuildMailAddress

# Get test cofiguration input
config = GetTestInput(__file__)

# Run method to be tested
input = RunBuildMailAddress(config)


class TestClass:
    def test_001_build_mail_address(self):
        assert input.mail_address == config.assert_value

    def test_002_simple_assert(self):
        x = 1
        y = 1
        assert x == y

    @pytest.mark.parametrize("x, y, z", [(1, 1, 2), (2, 2, 4)])
    def test_003_multiple_assert(self, x, y, z):
        assert x + y == z
