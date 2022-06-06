# Game of life - Python TDD

> Inspired by the game of life created by John Horton Conway in 1970, this project aims to rebuild it using TDD as a main software dev paradigm and CI/CD support for educational purposes.


## File structure

```bash
game-of-life-tdd/
├─ src/
│  ├─ utils/ # contains all the utils like logging, ...
│  ├─ graphic_lib.py # UI & graphic rendering functions
│  ├─ core_lib.py # core functions handling
├─ tests/
│  ├─ grid_test.py # tests the grid functions
```

*NB -  Naming convention :*

This project follows the naming conventing edited here : https://github.com/naming-convention/naming-convention-guides/tree/master/python

## Installation

With `python3.8+`, run :

```bash
venv .env && source .venv/bin/activate && pip3 install -r requirements.txt
```