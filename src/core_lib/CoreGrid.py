"""Core functions for the grid processing
"""
import numpy as np
from numpy.typing import _Shape


class CoreGrid:
    """Handle the main grid which keep tracks of the current state of the game's cells"""

    def __init__(self, default_cell_mat: np.ndarray):

        self.cell_mat: np.ndarray = default_cell_mat
        self.old_cell_mat: np.ndarray = default_cell_mat
        self.grid_dim: _Shape = default_cell_mat.shape
        self.validateGriIdnit()

    def applyRules(self) -> None:
        """Apply the 3 main rules of the Game of Life to the main matrix"""

    def validateGriIdnit(self) -> None:
        """Make sure that the grid has authorized dimensions in regards to the resolution of the UI, and correct values for the cells too"""

    def getCellMat(self) -> np.ndarray:
        """Return the grid, representing the cells on the form of nest np array

        Returns:
            np.ndarray: the grid containing the cells
        """
        return self.cell_mat
