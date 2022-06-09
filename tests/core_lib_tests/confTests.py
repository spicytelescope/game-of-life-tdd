"""
Configuration for core lib tests
"""
import numpy as np

# ===== Unit testing =====

# checking good behaviour of the core functions and more precisely the 3 core rules of the game after n turns
NORMAL_INIT_GRID: np.ndarray = np.array([[0, 0, 1]])
NORMAL_EXPECTED_GRID: np.ndarray = np.array([])
NORMAL_N_TURN: int = 5

# checking expected crash for incorrect values in the core grid
INCORRECT_INIT_GRID: np.ndarray = np.array([[3, 2, 1]])

# check if bad res for init trigger normal behaviour, in regards to the min/max res possible
BAD_DIM_GRID_HIGH = np.array(np.empty((100000, 100000)))
BAD_DIM_GRID_LOW = np.array(np.empty((0, 0)))

# checking core grid behaviour with a huge number of turn
LOAD_TEST_N_TURN: int = 100_000_000
LOAD_TEST_INIT_GRID: np.ndarray = np.array([[0, 0, 1]])
LOAD_TEST_EXPECTED_GRID: np.ndarray = np.array([])

# create a mock result that is expected not to yield out living cells
NO_LIVING_INIT_GRID: np.ndarray = np.array([[0, 0, 1]])
NO_LIVING_EXPECTED_GRID: np.ndarray = np.array([0, 0, 0])
