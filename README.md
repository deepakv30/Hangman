# Hangman CLI Game

[![CI](https://github.com/deepakv30/Hangman/actions/workflows/ci.yml/badge.svg)](https://github.com/deepakv30/Hangman/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/)

**Clean, tested, and CI-enabled Python Hangman CLI game with ASCII art, input validation, and modern best practices — portfolio project by a DevSecOps engineer.**

## Overview

A beginner-friendly yet professionally structured command-line Hangman game written in pure Python. Players guess letters to reveal a hidden word before the hangman drawing is complete.

This started as an early 2019 learning project and has been iteratively modernized in 2026 with tests, CI, documentation, input validation, ASCII stages, and clean code practices suitable for a developer portfolio.

## Features

- Random word selection from a curated built-in list (~60 words)
- 6 wrong guesses with progressive ASCII hangman stages
- Correct handling of duplicate letters (all occurrences revealed at once)
- Robust input validation (single letter, already-guessed, non-letters, case-insensitive)
- Remaining-guess counter after every turn
- Clear win / lose feedback with emoji
- Zero external runtime dependencies
- Fully tested with `pytest` + GitHub Actions CI (flake8 + pytest)

## How to Play

1. Clone the repository and run the script.
2. Guess one letter at a time (uppercase is accepted and normalized).
3. A correct guess reveals every matching letter. A miss advances the hangman drawing.
4. Reveal the full word before 6 wrong guesses.

## Example Gameplay

### Winning game
```text
Welcome to Hangman!
Guess the hidden word letter by letter.

The word has 8 letters.

      +---+
      |   |
          |
          |
          |
          |
    =========

********
You have 6 guesses remaining.

Enter your guess (single lowercase letter): a
Good guess! 'a' is in the word.
*****a**
Guessed letters so far: a
You have 6 guesses remaining.

Enter your guess (single lowercase letter): e
Sorry, 'e' is not in the word.

      +---+
      |   |
      O   |
          |
          |
          |
    =========

*****a**
Guessed letters so far: a, e
You have 5 guesses remaining.

...

Enter your guess (single lowercase letter): s
Good guess! 's' is in the word.
constant

🎉 Congratulations! You guessed the word correctly!
The word was: constant
```

### Losing game (shows duplicate-letter + already-guessed handling)
```text
Welcome to Hangman!
Guess the hidden word letter by letter.

The word has 8 letters.

      +---+
      |   |
          |
          |
          |
          |
    =========

********
You have 6 guesses remaining.

Enter your guess (single lowercase letter): a
Good guess! 'a' is in the word.
*a**a***
Guessed letters so far: a
You have 6 guesses remaining.

Enter your guess (single lowercase letter): a
You already guessed 'a'. Try a different letter.

...

Enter your guess (single lowercase letter): w
Sorry, 'w' is not in the word.

      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========

*a**ab*e
Guessed letters so far: a, b, e, w
You have 0 guesses remaining.

😢 Game Over! You ran out of guesses.
The word was: variable
```

> **Note:** Text-based examples are included above. A short terminal GIF or screenshot would further improve the README — contributions welcome!

## Installation & Running

```bash
git clone https://github.com/deepakv30/Hangman.git
cd Hangman
python hangman.py
```

Run the tests (pytest is a development dependency only):

```bash
pip install pytest
pytest tests/ -v
```

## Tech Stack

- Python 3.x (standard library only at runtime: `random`)
- pytest + flake8 in CI

## Project Structure

```text
Hangman/
├── hangman.py                 # Main game logic + ASCII stages
├── tests/
│   └── test_hangman.py        # Unit tests
├── .github/
│   ├── workflows/ci.yml       # GitHub Actions (lint + test)
│   ├── ISSUE_TEMPLATE/        # Bug & feature templates
│   └── PULL_REQUEST_TEMPLATE.md
├── README.md
├── LICENSE                    # MIT
├── .gitignore
└── pytest.ini
```

## Discoverability (Recommended Topics)

For better GitHub search and recommendation visibility, consider adding these topics in **Settings → General → Topics**:

`python` `hangman` `cli-game` `pytest` `github-actions` `beginner-project` `portfolio` `devops`

Also update the repository short description to match the tagline above.

## Future Improvements / Roadmap

Most core improvements from the original review are complete.

**Optional next steps:**
- [ ] Add difficulty levels (Easy / Medium / Hard)
- [ ] Load words from an external file (`words.txt`) with fallback to built-in list
- [ ] Short terminal GIF or screenshot in the README
- [ ] Optional “Play again?” loop
- [ ] Package as an installable CLI tool

## Contributing

Contributions are welcome!

1. Fork the repository.
2. Create a feature branch from `main`.
3. Make your changes and add tests if applicable.
4. Ensure CI passes (`pytest` + flake8).
5. Open a Pull Request using the provided template.

## License

MIT License — see the [LICENSE](LICENSE) file for details.

## Acknowledgments

Originally created as a simple Python learning project in 2019. Iteratively modernized in 2026 as part of ongoing professional development and portfolio improvement.

This repository demonstrates practical application of documentation, testing, CI, and clean code practices recommended for developer portfolios.
