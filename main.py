#!/usr/bin/env python3
"""entry point of the tdd game of life
"""
from src.MainRunner import MainRunner

if __name__ == "__main__":
    main_runner: MainRunner = MainRunner()
    main_runner.mainLoop()
