# Contributing to Hangman CLI Game

Thank you for your interest in contributing! This project welcomes improvements of all kinds — bug fixes, new features, documentation, and tests.

## Getting Started

1. Fork the repository.
2. Clone your fork:
   ```bash
   git clone https://github.com/<your-username>/Hangman.git
   cd Hangman
   ```
3. Create a feature branch from `main`:
   ```bash
   git checkout -b feature/your-feature-name
   ```

## Development Setup

```bash
# Install pinned development dependencies (runtime stays stdlib-only)
pip install -r requirements-dev.txt

# Run the game
python hangman.py

# Run tests
pytest tests/ -v

# Lint
flake8 . --max-line-length=100
```

CI runs the same flake8 + pytest commands on Python 3.11 and 3.12.

## Making Changes

- Follow the existing code style (f-strings, type hints, docstrings).
- Add or update tests for any new behavior.
- Keep the game dependency-free at runtime (standard library only).
- Update the README if you change user-facing behavior or project structure.

## Submitting a Pull Request

1. Ensure all tests pass and the code is lint-clean.
2. Push your branch and open a Pull Request against `main`.
3. Use the provided Pull Request template.
4. Clearly describe the problem and the solution.
5. Link any related issues.

## Code of Conduct

Be respectful and constructive. We aim to maintain a welcoming environment for all contributors.

## Questions?

Open an issue using one of the provided templates or start a discussion in a Pull Request.

Thank you for helping improve this project!
