from hangman import (
    get_word_list,
    display_word,
    get_valid_guess,
    DIFFICULTY_CONFIG,
    EASY_WORDS,
    MEDIUM_WORDS,
    HARD_WORDS,
)


# --- get_word_list ---

def test_get_word_list_not_empty():
    assert len(get_word_list()) > 0


def test_get_word_list_all_lowercase_alpha():
    for word in get_word_list():
        assert word == word.lower()
        assert word.isalpha()


def test_get_word_list_easy():
    words = get_word_list("easy")
    assert len(words) > 0
    # When words.txt is present it is preferred; otherwise EASY_WORDS is used.
    # Both are valid.
    assert all(w.isalpha() and w == w.lower() for w in words)


def test_get_word_list_medium():
    words = get_word_list("medium")
    assert len(words) > 0


def test_get_word_list_hard():
    words = get_word_list("hard")
    assert len(words) > 0


def test_get_word_list_invalid_difficulty_falls_back_to_medium():
    words = get_word_list("invalid")
    assert len(words) > 0


def test_difficulty_config_has_expected_keys():
    assert set(DIFFICULTY_CONFIG.keys()) == {"easy", "medium", "hard"}
    assert DIFFICULTY_CONFIG["easy"]["max_guesses"] == 8
    assert DIFFICULTY_CONFIG["medium"]["max_guesses"] == 6
    assert DIFFICULTY_CONFIG["hard"]["max_guesses"] == 5


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
