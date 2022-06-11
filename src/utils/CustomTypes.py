"""Defines the custom types needed for the project
"""
from typing import get_args
from typing import Literal

DEAD_CELL_STATE_TYPE = Literal[0]
ALIVE_CELL_STATE_TYPE = Literal[1]
GRID_CELL_STATE_TYPE = Literal[DEAD_CELL_STATE_TYPE, ALIVE_CELL_STATE_TYPE]

DEAD_CELL_STATE: DEAD_CELL_STATE_TYPE = get_args(DEAD_CELL_STATE_TYPE)[0]
ALIVE_CELL_STATE: ALIVE_CELL_STATE_TYPE = get_args(ALIVE_CELL_STATE_TYPE)[0]
