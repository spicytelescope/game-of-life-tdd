"""
Configuration for core lib tests
"""
import numpy as np
from typing import List

# Unit testing

# Checking good behaviour of the core function after n turns
INIT_GRID: np.ndarray = np.array([[0, 0, 1]])
EXPECTED_GRID: np.ndarray = np.array([])  # create a mock result that shoudln't
N_TURN = 5

# Checking expected crash for incorrect values
