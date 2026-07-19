import pytest
from string_utils import StringUtils


string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected

@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected",[
    (" Test", "Test"),
    (" skypro", "skypro"),
    (" 123", "123"),
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str)  == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected",[
    ("  Test", "Test"),
    ("skypro", "skypro"),
    (" Пароль 123", "Пароль 123"),
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str)  == expected

@pytest.mark.positive
@pytest.mark.parametrize("input_str, input_simbol, expected",[
    ("Test1", "1", True),
    ("skypro", "s", True),
    ("Пароль 123", "2", True),
])
def test_contains_positive(input_str, input_simbol, expected):
    assert string_utils.contains(input_str, input_simbol)  == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str, input_simbol, expected",[
    ("Test1", "2", False),
    ("skypro", "h", False),
    ("Пароль 123", "0", False),
])
def test_contains_negative(input_str, input_simbol, expected):
    assert string_utils.contains(input_str, input_simbol)  == expected

@pytest.mark.positive
@pytest.mark.parametrize("input_str, input_simbol, expected",[
    ("Test", "t", "Tes"),
    ("skypro1", "1", "skypro"),
    ("123", "23", "1"),
])
def test_delete_symbol_positive(input_str, input_simbol, expected):
    assert string_utils.delete_symbol(input_str, input_simbol)  == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str, input_simbol, expected",[
    ("skypro1", "5", "skypro1"),
    ("123", " ", "123"),
])
def test_delete_symbol_negative(input_str, input_simbol, expected):
    assert string_utils.delete_symbol(input_str, input_simbol)  == expected