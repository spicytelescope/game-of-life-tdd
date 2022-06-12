"""
Configuration for ui lib tests
"""
from typing import List
import numpy as np

# check if bad res for init trigger normal behaviour, in regards to the min/max res possible
BAD_DIM_GRID_HIGH = np.array(np.empty((2000, 2000)))
BAD_DIM_GRID_LOW = np.array(np.empty((0, 0)))
BAD_DIM_GRID_ODD = np.array(np.empty((3, 1)))

BAD_RES_LOW: List[int] = [6, 6]
BAD_RES_HIGH: List[int] = [4000, 4000]
BAD_RES_ODD: List[int] = [1021, 1022]
