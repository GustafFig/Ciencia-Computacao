import pytest
from unittest.mock import patch
from four import verify_emails


@pytest.fixture
def test():
    return (
        ["nome@dominio.com", "errad#@dominio.com", "outro@dominio.com"],
        ["nome@dominio.com", "outro@dominio.com"],
    )


def test_verify_emails_returns_corrects_emails(test):
    enter, expected_out = test
    assert verify_emails(enter) == expected_out


@patch("builtins.print")
def test_verify_emails_print_on_wrong_emails(mocked_print, test):
    emails_input, _ = test
    verify_emails(emails_input)
    mocked_print.assert_called_with("errad#@dominio.com")
