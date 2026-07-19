from hangman import get_word_list, display_word, get_valid_guess


# --- get_word_list ---

def test_get_word_list_not_empty():
    assert len(get_word_list()) > 0


def test_get_word_list_all_lowercase_alpha():
    for word in get_word_list():
        assert word == word.lower()
        assert word.isalpha()


# --- display_word ---

def test_display_word_no_letters_guessed():
    assert display_word("hangman", set()) == "*******"


def test_display_word_single_occurrence():
    assert display_word("hangman", {"h"}) == "h******"


def test_display_word_duplicate_letters_revealed_together():
    # regression test for the duplicate-letter bug
    assert display_word("hangman", {"a"}) == "*a***a*"


def test_display_word_multiple_duplicates():
    assert display_word("committee", {"t", "e"}) == "*****ttee"


def test_display_word_fully_revealed():
    word = "loop"
    guessed = set(word)
    assert display_word(word, guessed) == word


def test_display_word_unrelated_guesses_ignored():
    assert display_word("debug", {"x", "y", "z"}) == "*****"


# --- get_valid_guess ---

def test_get_valid_guess_accepts_valid_letter(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "a")
    assert get_valid_guess(set()) == "a"


def test_get_valid_guess_rejects_multiple_characters(monkeypatch, capsys):
    responses = iter(["cs", "c"])
    monkeypatch.setattr("builtins.input", lambda _: next(responses))
    result = get_valid_guess(set())
    assert result == "c"
    assert "exactly one letter" in capsys.readouterr().out


def test_get_valid_guess_rejects_empty_input(monkeypatch, capsys):
    responses = iter(["", "a"])
    monkeypatch.setattr("builtins.input", lambda _: next(responses))
    result = get_valid_guess(set())
    assert result == "a"
    assert "exactly one letter" in capsys.readouterr().out


def test_get_valid_guess_rejects_non_alpha(monkeypatch, capsys):
    responses = iter(["5", "a"])
    monkeypatch.setattr("builtins.input", lambda _: next(responses))
    result = get_valid_guess(set())
    assert result == "a"
    assert "Please enter a letter" in capsys.readouterr().out


def test_get_valid_guess_rejects_already_guessed(monkeypatch, capsys):
    responses = iter(["a", "b"])
    monkeypatch.setattr("builtins.input", lambda _: next(responses))
    result = get_valid_guess({"a"})
    assert result == "b"
    assert "already guessed" in capsys.readouterr().out


def test_get_valid_guess_normalizes_uppercase(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "A")
    assert get_valid_guess(set()) == "a"


def test_get_valid_guess_strips_whitespace(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "  a  ")
    assert get_valid_guess(set()) == "a"
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
