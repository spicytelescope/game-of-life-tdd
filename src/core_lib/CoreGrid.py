"""Core functions for the grid processing
"""
from typing import Dict

import numpy as np
from numpy.typing import _Shape
from src.utils.confUtils import fetch_game_config


class CoreGrid:
    """Handle the main grid which keep tracks of the current state of the game's cells"""

    def __init__(self, default_cell_mat: np.ndarray):

        self.cell_mat: np.ndarray = default_cell_mat
        self.old_cell_mat: np.ndarray = default_cell_mat
        self.grid_dim: _Shape = default_cell_mat.shape
        self.gameConfig: Dict = fetch_game_config()["videoSettings"]
        self.validateGriIdnit()

    def applyRules(self) -> None:
        """Apply the 3 main rules of the Game of Life to the main matrix"""

    def validateGriIdnit(self) -> None:
        """Make sure that the grid has authorized dimensions in regards to the resolution of the UI, and correct values for the cells too"""
        assert (
            self.gameConfig["min_grid_dim"][0]
            <= self.grid_dim[0]
            <= self.gameConfig["res"][0]
        ), f"grid_dim 0 ({self.grid_dim[0]}) should be between {self.gameConfig['min_grid_dim'][0]} and {self.gameConfig['res'][0]}"

        assert all(
            dim % 2 == 0 for dim in self.grid_dim
        ), "grid dimensions should be even numbers"

        assert all(
            low <= x <= high
            for low, x, high in zip(
                self.gameConfig["min_grid_dim"],
                self.grid_dim,
                self.gameConfig["res"],
            )
        ), f"grid_dim 0 ({self.grid_dim[0]}) should be between {self.gameConfig['min_grid_dim'][0]} and {self.gameConfig['res'][0]}"

        assert all(
            (0 <= self.cell_mat) & (self.cell_mat <= 1)
        ), "all cells should be represented by integer of 0 or 1 (dead or alive state)"

    def getCellMat(self) -> np.ndarray:
        """Return the grid, representing the cells on the form of nest np array

        Returns:
            np.ndarray: the grid containing the cells
        """
        return self.cell_mat
