import random


def get_word_list():
    """Return a list of words for the game."""
    return [
        "python", "hangman", "developer", "algorithm", "github",
        "computer", "keyboard", "monitor", "program", "function",
        "variable", "constant", "loop", "condition", "debug",
        "repository", "pullrequest", "commit", "branch", "merge"
    ]


def display_word(word, guessed_letters):
    """Return the current display of the word with guessed letters revealed."""
    return "".join(letter if letter in guessed_letters else "*" for letter in word)


def get_valid_guess(guessed_letters):
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


def play_hangman():
    """Main function to play the Hangman game."""
    print("Welcome to Hangman!")
    print("Guess the hidden word letter by letter.\n")

    words = get_word_list()
    word = random.choice(words).lower()
    guessed_letters = set()
    remaining_guesses = 8  # Standard number of attempts for a good challenge

    print(f"The word has {len(word)} letters.")
    print(display_word(word, guessed_letters))
    print(f"You have {remaining_guesses} guesses remaining.\n")

    while remaining_guesses > 0:
        guess = get_valid_guess(guessed_letters)
        guessed_letters.add(guess)

        if guess in word:
            print(f"Good guess! '{guess}' is in the word.")
        else:
            remaining_guesses -= 1
            print(f"Sorry, '{guess}' is not in the word. You have {remaining_guesses} guesses left.")

        current_display = display_word(word, guessed_letters)
        print(current_display)

        if current_display == word:
            print("\n🎉 Congratulations! You guessed the word correctly!")
            print(f"The word was: {word}")
            return

        print(f"Guessed letters so far: {', '.join(sorted(guessed_letters))}\n")

    # If loop ends without winning
    print("\n😢 Game Over! You ran out of guesses.")
    print(f"The word was: {word}")


if __name__ == "__main__":
    play_hangman()
