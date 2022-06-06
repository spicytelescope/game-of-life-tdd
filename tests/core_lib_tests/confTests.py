"""
Configuration for core lib tests
"""
import numpy as np

# ===== Unit testing =====

# Checking good behaviour of the core function after n turns
INIT_GRID: np.ndarray = np.array([[0, 0, 1]])
EXPECTED_GRID: np.ndarray = np.array([])  # create a mock result that shoudln't
N_TURN: int = 5

# Checking expected crash for incorrect values in the core grid
INCORRECT_INIT_GRID: np.ndarray = np.array([[3, 2, 1]])

# Checking core grid behaviour with a huge number of turn
LOAD_TEST_N_TURN: int = 100_000_000
LOAD_TEST_INIT_GRID: np.ndarray = np.array([[0, 0, 1]])
LOAD_TEST_EXPECTED_GRID: np.ndarray = np.array(
    []
)  # create a mock result that shoudln't
