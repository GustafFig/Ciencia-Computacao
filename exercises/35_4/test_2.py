from two import change_to_number
import pytest


def test_change_to_numbers_with_1():
    result = change_to_number("1")
    assert result == "1"


def test_change_to_numbers_with_letters():
    result = change_to_number("MY-MISERABLE-JOB")
    assert result == "69-647372253-562"


def test_change_to_numbers_with_wrong_inserts():
    with pytest.raises(ValueError, match=r"Character . not valid"):
        change_to_number("MY-MIS/ERABLE-JOB")


def test_change_to_numbers_with_numbers():
    with pytest.raises(TypeError, match="name 1234 must be an string"):
        change_to_number(1234)
