import pytest

class TestFake:

    @pytest.mark.initial_tests
    def test_posistive_case_1(self):
        a = 5
        b = 5
        assert a == b

    @pytest.mark.initial_tests
    def test_negative_case_1(self):
        a = 5
        b = 7
        assert a == b

    @pytest.mark.initial_tests
    def test_posistive_case_2(self):
        print('Look, this test is passed')