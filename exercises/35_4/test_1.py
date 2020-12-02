from one import FizzBuzz


def test_FizzBuzz_3_multiple_numbers_should_have_Fizz():
    list = FizzBuzz(30)
    for i_mult in [3, 6, 9, 12, 18, 21, 24, 27]:
        assert list[i_mult - 1] == "Fizz"


def test_FizzBuzz_5_multiple_numbers_should_have_Buzz():
    list = FizzBuzz(40)
    for i_mult in [5, 10, 20, 25, 35, 40]:
        assert list[i_mult - 1] == "Buzz"


def test_FizzBuzz_3_and_5_multiple_numbers_should_have_FizzBuzz():
    list = FizzBuzz(90)
    for i_mult in [15, 30, 45, 60, 75, 90]:
        assert list[i_mult - 1] == "FizzBuzz"


def test_FizzBuzz_with_10():
    list = [1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz"]
    assert FizzBuzz(10) == list
