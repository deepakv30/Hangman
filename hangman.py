import random
from pathlib import Path
from typing import List, Set

HANGMAN_STAGES = [
    r"""
      +---+
      |   |
          |
          |
          |
          |
    =========
    """,
    r"""
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    """,
    r"""
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    """,
    r"""
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    """,
    r"""
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========
    """,
    r"""
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========
    """,
    r"""
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========
    """
]

# Built-in word lists by difficulty
EASY_WORDS: List[str] = [
    "apple", "river", "window", "pencil", "garden", "mountain",
    "shadow", "music", "camera", "winter", "summer", "farmer",
    "baker", "doctor", "teacher", "student", "friend", "family",
    "village", "city", "street", "bridge", "kitchen", "table",
    "chair", "blanket", "ocean", "island", "tree", "flower",
    "bird", "animal", "tiger", "weather", "cloud", "thunder",
    "rain", "snow", "light", "dark", "strong", "quick",
    "happy", "brave", "honest", "simple", "clever", "careful",
]

MEDIUM_WORDS: List[str] = [
    "python", "hangman", "developer", "algorithm", "github",
    "computer", "keyboard", "monitor", "program", "function",
    "variable", "constant", "loop", "condition", "debug",
    "repository", "commit", "branch", "merge",
    "beautiful", "balance", "village", "mountain", "weather",
]

HARD_WORDS: List[str] = [
    "algorithm", "repository", "developer", "condition",
    "beautiful", "committee", "variable", "function",
    "keyboard", "monitor", "python", "hangman",
]

DIFFICULTY_CONFIG = {
    "easy": {"max_guesses": 8, "words": EASY_WORDS},
    "medium": {"max_guesses": 6, "words": MEDIUM_WORDS},
    "hard": {"max_guesses": 5, "words": HARD_WORDS},
}


def get_word_list(difficulty: str = "medium") -> List[str]:
    """Return a list of words for the given difficulty.

    Prefers words from words.txt (one word per line) when the file exists.
    Falls back to the built-in list for the selected difficulty.
    """
    words_file = Path("words.txt")
    if words_file.is_file():
        try:
            with words_file.open(encoding="utf-8") as f:
                file_words = [
                    line.strip().lower()
                    for line in f
                    if line.strip() and line.strip().isalpha()
                ]
            if file_words:
                return file_words
        except OSError:
            pass  # Fall through to built-in list

    config = DIFFICULTY_CONFIG.get(difficulty, DIFFICULTY_CONFIG["medium"])
    return list(config["words"])


def display_word(word: str, guessed_letters: Set[str]) -> str:
    """Return the current display of the word with guessed letters revealed."""
    return "".join(letter if letter in guessed_letters else "*" for letter in word)


def get_valid_guess(guessed_letters: Set[str]) -> str:
    """Prompt for a valid single lowercase letter guess."""
    while True:
        guess = input("Enter your guess (single lowercase letter): ").strip().lower()
        if len(guess) != 1:
            print("Please enter exactly one letter.")
            continue
        if not guess.isalpha():
            print("Please enter a letter (a-z).")
            continue
        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try a different letter.")
            continue
        return guess


def select_difficulty() -> str:
    """Prompt the user to select a difficulty level."""
    print("Select difficulty:")
    print("  1. Easy   (8 guesses, shorter words)")
    print("  2. Medium (6 guesses)")
    print("  3. Hard   (5 guesses, longer words)")

    while True:
        choice = input("Enter 1, 2, or 3 [default: 2]: ").strip()
        if choice == "" or choice == "2":
            return "medium"
        if choice == "1":
            return "easy"
        if choice == "3":
            return "hard"
        print("Please enter 1, 2, or 3.")


def play_hangman(difficulty: str | None = None) -> None:
    """Main function to play the Hangman game with ASCII art."""
    print("Welcome to Hangman!")
    print("Guess the hidden word letter by letter.\n")

    if difficulty is None:
        difficulty = select_difficulty()

    config = DIFFICULTY_CONFIG.get(difficulty, DIFFICULTY_CONFIG["medium"])
    max_guesses: int = config["max_guesses"]
    words = get_word_list(difficulty)
    word = random.choice(words).lower()
    guessed_letters: Set[str] = set()
    wrong_guesses = 0

    print(f"\nDifficulty: {difficulty.capitalize()}")
    print(f"The word has {len(word)} letters.")
    print(HANGMAN_STAGES[0])
    print(display_word(word, guessed_letters))
    print(f"You have {max_guesses} guesses remaining.\n")

    while wrong_guesses < max_guesses:
        guess = get_valid_guess(guessed_letters)
        guessed_letters.add(guess)

        if guess in word:
            print(f"Good guess! '{guess}' is in the word.")
        else:
            wrong_guesses += 1
            print(f"Sorry, '{guess}' is not in the word.")
            # Clamp index so we never go out of range
            stage_index = min(wrong_guesses, len(HANGMAN_STAGES) - 1)
            print(HANGMAN_STAGES[stage_index])

        current_display = display_word(word, guessed_letters)
        print(current_display)

        if current_display == word:
            print("\n🎉 Congratulations! You guessed the word correctly!")
            print(f"The word was: {word}")
            return

        remaining = max_guesses - wrong_guesses
        guess_word = "guess" if remaining == 1 else "guesses"
        print(f"Guessed letters so far: {', '.join(sorted(guessed_letters))}")
        print(f"You have {remaining} {guess_word} remaining.\n")

    print("\n😢 Game Over! You ran out of guesses.")
    print(f"The word was: {word}")


if __name__ == "__main__":
    play_hangman()
