# Hangman CLI Game

[![CI](https://github.com/deepakv30/Hangman/actions/workflows/ci.yml/badge.svg)](https://github.com/deepakv30/Hangman/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.11+](https://img.shields.io/badge/python-3.11%20%7C%203.12-blue.svg)](https://www.python.org/)

**Clean, tested, and CI-enabled Python Hangman CLI game with ASCII art, input validation, difficulty levels, and modern best practices — portfolio project by a DevSecOps engineer.**

## Overview

A beginner-friendly yet professionally structured command-line Hangman game written in pure Python. Players guess letters to reveal a hidden word before the hangman drawing is complete.

This started as an early 2019 learning project and has been iteratively modernized in 2026 with tests, CI, documentation, input validation, ASCII stages, type hints, difficulty levels, and clean code practices suitable for a developer portfolio.

## Features

- **Difficulty levels**: Easy (8 guesses), Medium (6), Hard (5)
- **Play again?** loop after win or lose
- Random word selection from a curated built-in list or optional `words.txt`
- Progressive ASCII hangman stages
- Correct handling of duplicate letters (all occurrences revealed at once)
- Robust input validation (single letter, already-guessed, non-letters, case-insensitive)
- Remaining-guess counter after every turn
- Clear win / lose feedback with emoji
- **Optional colored output** via `colorama` (fully optional — zero hard dependencies)
- Fully typed helpers + comprehensive `pytest` suite
- GitHub Actions CI (flake8 + pytest)

## How to Play

1. Clone the repository and run the script.
2. Choose a difficulty (Easy / Medium / Hard).
3. Guess one letter at a time (uppercase is accepted and normalized).
4. A correct guess reveals every matching letter. A miss advances the hangman drawing.
5. Reveal the full word before you run out of guesses.
6. After the round, choose whether to play again.

## Example Gameplay

### Winning game
```text
Welcome to Hangman!
Guess the hidden word letter by letter.

Select difficulty:
  1. Easy   (8 guesses, shorter words)
  2. Medium (6 guesses)
  3. Hard   (5 guesses, longer words)
Enter 1, 2, or 3 [default: 2]: 2

Difficulty: Medium
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

...

🎉 Congratulations! You guessed the word correctly!
The word was: constant

Play again? (y/n) [default: n]: n
Thanks for playing! Goodbye.
```

## Installation & Running

```bash
git clone https://github.com/deepakv30/Hangman.git
cd Hangman
python hangman.py
```

### Optional: Colored output

For colored terminal messages (green for correct, red for wrong, etc.):

```bash
pip install colorama
```

The game works perfectly without it — colors are completely optional.

### Optional: Custom word list

Create a `words.txt` file in the project root (one word per line). The game will prefer these words when the file is present and falls back to the built-in lists otherwise. A sample `words.txt` is included.

Run lint and tests (development dependencies only — the game itself stays zero-dep):

```bash
pip install -r requirements-dev.txt
flake8 . --max-line-length=100
pytest tests/ -v
```

## Tech Stack

- Python 3.11 / 3.12 (standard library only at runtime)
- Optional: `colorama` for colored output
- Type hints throughout
- pytest + flake8 in CI via pinned `requirements-dev.txt`

## Project Structure

```text
Hangman/
├── hangman.py                 # Main game logic + ASCII stages + difficulty
├── words.txt                  # Optional external word list (sample included)
├── tests/
│   └── test_hangman.py        # Unit tests
├── .github/
│   ├── workflows/ci.yml       # GitHub Actions (Python 3.11/3.12 lint + test)
│   ├── ISSUE_TEMPLATE/        # Bug & feature templates
│   └── PULL_REQUEST_TEMPLATE.md
├── requirements-dev.txt       # Pinned flake8 + pytest (dev only)
├── README.md
├── CONTRIBUTING.md
├── SECURITY.md
├── LICENSE                    # MIT
├── .gitignore
└── pytest.ini
```

## Discoverability (Recommended Topics)

For better GitHub search and recommendation visibility, add these topics in **Settings → General → Topics**:

`python` `hangman` `cli-game` `pytest` `github-actions` `beginner-project` `portfolio` `devops`

Also update the repository short description to match the tagline above.

## Future Improvements / Roadmap

Most recommended improvements are now complete.

**Optional next steps:**
- [ ] Short terminal GIF or screenshot in the README
- [ ] Package as an installable CLI tool

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

In short:
1. Fork the repository.
2. Create a feature branch from `main`.
3. Make your changes and add tests if applicable.
4. Ensure CI passes (`pytest` + flake8).
5. Open a Pull Request using the provided template.

## Security

See [SECURITY.md](SECURITY.md) for how to report vulnerabilities.

## License

MIT License — see the [LICENSE](LICENSE) file for details.

## Acknowledgments

Originally created as a simple Python learning project in 2019. Iteratively modernized in 2026 as part of ongoing professional development and portfolio improvement.

This repository demonstrates practical application of documentation, testing, CI, type hints, and clean code practices recommended for developer portfolios.
