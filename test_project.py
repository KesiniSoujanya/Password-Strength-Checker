import pytest
from project import generate_password
from project import is_strong_password
from project import get_valid_password


def test_generate_password_length():

    length = 10
    password = generate_password(length)
    assert len(password) == length


def test_is_strong_password():

    strong_password = "Strong@123"
    assert is_strong_password(strong_password) == True

    weak_password = "weakpassword"
    assert is_strong_password(weak_password) == False

@pytest.mark.parametrize("inputs, expected_output", [
    (["weakpassword", "Strong@123"], "Strong@123"),

])



def test_get_valid_password(monkeypatch, inputs, expected_output):


    input_mock = iter(inputs)

    with monkeypatch.context() as m:
        m.setattr('builtins.input', lambda _: next(input_mock))
        valid_password = get_valid_password()

    assert valid_password == expected_output
