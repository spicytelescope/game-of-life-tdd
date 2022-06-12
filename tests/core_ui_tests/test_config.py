"""
Configuration for ui lib tests
"""
from typing import List

# check if bad grid dim for init trigger normal behaviour, in regards to the min/max res possible
BAD_DIM_HIGH = [2000, 2000]
BAD_DIM_LOW = [0, 0]
BAD_DIM_ODD = [3, 1]

# check if bad res for init trigger normal behaviour, in regards to the min/max res possible
BAD_RES_LOW: List[int] = [6, 6]
BAD_RES_HIGH: List[int] = [4000, 4000]
BAD_RES_ODD: List[int] = [1021, 1022]
