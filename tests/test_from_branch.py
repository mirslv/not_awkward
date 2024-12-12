import pytest

class TestBranch:

    @pytest.mark.branch_tests
    def test_branch_case_1(self):
        c = 8
        d = 10
        assert c != d