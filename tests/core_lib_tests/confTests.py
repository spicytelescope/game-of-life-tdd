"""
Configuration for core lib tests
"""
import numpy as np

# ===== Unit testing =====

# checking good behaviour of the core function after n turns
NORMAL_INIT_GRID: np.ndarray = np.array([[0, 0, 1]])
NORMAL_EXPECTED_GRID: np.ndarray = np.array([])
NORMAL_N_TURN: int = 5

# checking expected crash for incorrect values in the core grid
INCORRECT_INIT_GRID: np.ndarray = np.array([[3, 2, 1]])

# checking core grid behaviour with a huge number of turn
LOAD_TEST_N_TURN: int = 100_000_000
LOAD_TEST_INIT_GRID: np.ndarray = np.array([[0, 0, 1]])
LOAD_TEST_EXPECTED_GRID: np.ndarray = np.array([])

# create a mock result that is expected not to yield out living cells
NO_LIVING_INIT_GRID: np.ndarray = np.array([[0, 0, 1]])
NO_LIVING_EXPECTED_GRID: np.ndarray = np.array([0, 0, 0])

# check if bad res for init trigger normal behaviour, in regards to the max res possible
BAD_RES = [4, 7]
