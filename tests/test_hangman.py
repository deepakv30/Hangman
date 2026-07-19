import pytest
from hangman import display_word, get_valid_guess


def test_display_word_basic():
    """Test basic display functionality."""
    assert display_word("python", set()) == "******"
    assert display_word("python", {"p", "o"}) == "p***o*"
    assert display_word("hangman", {"h", "a", "n"}) == "han**an"


def test_display_word_duplicates():
    """Ensure duplicate letters are handled correctly (the original bug fix)."""
    assert display_word("room", {"r", "o"}) == "roo*"
    assert display_word("room", {"o"}) == "*oo*"
    assert display_word("commit", {"c", "o", "m"}) == "com**t"


def test_get_valid_guess_valid_input(monkeypatch):
    """Test that a valid single letter is accepted."""
    inputs = iter(["a"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    guessed = set()
    result = get_valid_guess(guessed)
    assert result == "a"


def test_get_valid_guess_rejects_invalid(monkeypatch, capsys):
    """Test rejection of invalid inputs (numbers, multiple chars, symbols)."""
    inputs = iter(["1", "ab", "!", "b"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    guessed = set()
    result = get_valid_guess(guessed)
    captured = capsys.readouterr()
    assert "Please enter exactly one letter." in captured.out
    assert result == "b"


def test_get_valid_guess_rejects_already_guessed(monkeypatch, capsys):
    """Test rejection of already guessed letters."""
    inputs = iter(["a", "a", "c"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    guessed = {"a"}
    result = get_valid_guess(guessed)
    captured = capsys.readouterr()
    assert "You already guessed 'a'" in captured.out
    assert result == "c"


def test_get_valid_guess_case_insensitive(monkeypatch):
    """Test that uppercase input is normalized to lowercase."""
    inputs = iter(["P", "y"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    guessed = set()
    result = get_valid_guess(guessed)
    assert result == "p"
