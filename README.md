# Hangman CLI Game

**A simple, dependency-free implementation of the classic Hangman word-guessing game in Python.**

## Overview
This repository contains a beginner-friendly command-line Hangman game. Players guess letters to reveal a hidden word within a chosen number of attempts.

**Note:** This is an early Python project (2019) by a DevSecOps engineer. It is being actively improved for better code quality, documentation, and maintainability as of 2026.

## Features
- Random word selection from a small built-in list
- Customizable number of guesses
- Basic duplicate letter handling
- Clear win/lose feedback
- Pure Python — no external dependencies

## How to Play
1. Clone the repository and run the script.
2. Enter the desired number of guesses.
3. Guess one letter at a time (lowercase recommended).
4. Try to reveal the full word before running out of attempts!

## Installation & Running
```bash
git clone https://github.com/deepakv30/Hangman.git
cd Hangman
python hangman.py
```

## Tech Stack
- Python 3.x (standard library only: `random`)

## Project Structure
```
Hangman/
├── hangman.py          # Main game logic
├── README.md
├── LICENSE
└── .gitignore
```

## Future Improvements / Roadmap
See the main GitHub Issue for the full prioritized list, progress tracking, and discussion.

- [x] Add comprehensive README
- [x] Add MIT LICENSE
- [x] Add Python .gitignore
- [ ] Fix duplicate letter revelation bug properly
- [ ] Improve input validation and UX
- [ ] Add unit tests with pytest
- [ ] Set up GitHub Actions CI
- [ ] Expand word list (from file or external source)
- [ ] Add ASCII hangman art and difficulty levels
- [ ] Modernize code style (f-strings, better structure, docstrings)
- [ ] Clean up dangling submodule entry

## Contributing
Contributions are welcome! Please:
1. Comment on or reference the main improvement issue first.
2. Fork the repo and create a feature branch from `improve-hangman-repo`.
3. Submit a Pull Request.

## License
MIT License — see the [LICENSE](LICENSE) file for details.

## Acknowledgments
Originally created as a simple Python learning project in 2019. Being modernized in 2026 as part of ongoing professional development and portfolio improvement.

**This work addresses recommendations from a structured Senior GitHub Profile Strategist review.**
