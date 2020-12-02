import pytest
from three import verify_email


@pytest.fixture
def corrects():
    return ["name@email.com", "user_name@email.com", "name@email.co"]


@pytest.fixture
def wrongs():
    return [
        "nameemail.com",
        "1name@email.co",
        # Não descobri porque passa na Regex, se souber me conte :)
        "_name@email.co",
        "name@email.coma",
    ]


def test_verify_email_with_wrong_format(corrects):
    for example in corrects:
        assert verify_email(example) == True


def test_verify_email_with_wrongs_formats(wrongs):
    for email in wrongs:
        with pytest.raises(ValueError):
            assert verify_email(email)
