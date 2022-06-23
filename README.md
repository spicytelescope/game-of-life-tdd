# Game of life - Python TDD

_Inspired by the game of life created by John Horton Conway in 1970, this project aims to rebuild it using TDD as a main software dev paradigm and CI/CD support for educational purposes._

<span style="display: flex; justify-content: space-evenly">

![Tests](https://github.com/spicytelescope/game-of-life-tdd/actions/workflows/tests.yml/badge.svg)

![Ubuntu](https://img.shields.io/badge/Ubuntu-20.04-E95420?style=for-the-badge&logo=ubuntu&logoColor=red)

![Windows](https://img.shields.io/badge/Windows-10-0078D6?style=for-the-badge&logo=windows&logoColor=blue)

</span>

## File structure

```bash
.
├── LICENSE
├── README.md # read it ;)
├── assets # contains sprites
├── config.json # configuration file of the project, the user must use only this file to tweak the game
├── main.py # entry point of the project
├── requirements.txt # list of dependencies for this project
├── src
│   ├── MainRunner.py # main runner communicating & syncing with every components, designed to run the game loop
│   ├── __init__.py
│   ├── __pycache__
│   ├── core_lib # core functions handling
│   ├── ui_lib # UI & graphic rendering lib
│   └── utils
├── tests
│   ├── __init__.py
│   ├── __pycache__
│   ├── core_lib_tests # tests the grid functions
│   └── core_ui_tests # tests the ui functions
└── tox.ini
```

_NB - Naming convention :_

This project follows the naming conventing edited here : https://github.com/naming-convention/naming-convention-guides/tree/master/python, except for the method of classes that will use the camelCase method, with internal ones using underscore notation.

## Installation

With `python3.8+`, run :

```bash
pip3 install -r requirements.txt
```

Or, if you have a virtual environment :

| Windows                                                                                               | Linux                                                                                         |
| ----------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `venv $YOUR_ENV_DIR && source $YOUR_ENV_DIR/Scripts/activate.ps1 && pip3 install -r requirements.txt` | `venv $YOUR_ENV_DIR && source $YOUR_ENV_DIR/bin/activate && pip3 install -r requirements.txt` |

_Note that the project is cross-platform, and has been tested on Ubuntu20.04 and Windows10._
