"""Core functions for the grid processing
"""
from typing import Dict

import numpy as np
from numpy.typing import _Shape
from tabulate import tabulate  # type: ignore
from src.utils.confUtils import fetch_game_config
from src.utils.CustomTypes import ALIVE_CELL_STATE
from src.utils.CustomTypes import DEAD_CELL_STATE
from src.utils.CustomTypes import GRID_CELL_STATE_TYPE


class CoreGrid:
    """Handle the main grid which keep tracks of the current state of the game's cells"""

    def __init__(self, default_cell_mat: np.ndarray):

        self.cell_mat: np.ndarray = default_cell_mat
        self.old_cell_mat: np.ndarray = default_cell_mat
        self.grid_dim: _Shape = default_cell_mat.shape
        self.gameConfig: Dict = fetch_game_config()["videoSettings"]
        self.validateGrid()

    def prettyPrintCellMat(self, tabulate_fmt="grid") -> None:
        """Pretty print the grid using tabulate 'grid' format"""

        print(tabulate(self.cell_mat, tablefmt=tabulate_fmt))

    def applyRules(
        self,
    ) -> None:
        """Apply the 3 main rules of the Game of Life to the main matrix"""

    def _applyRulessOnCell(self, i: int, j: int) -> GRID_CELL_STATE_TYPE:

        next_state: GRID_CELL_STATE_TYPE = DEAD_CELL_STATE
        cell_state: GRID_CELL_STATE_TYPE = self.cell_mat[i][j]

        cell_surrounding: np.ndarray = self.__getCurrentNeighbors(i, j)
        if cell_state == ALIVE_CELL_STATE:
            # substracting one because the current cell tested is alrady on the 'alive' state
            if not (
                sum(x.count(ALIVE_CELL_STATE) for x in cell_surrounding) - 1 in [2, 3]
            ):
                next_state = DEAD_CELL_STATE
        else:
            pass

        return next_state

    def __getCurrentNeighbors(self, i: int, j: int) -> np.ndarray:
        surr_neighbours: np.ndarray = np.full((3, 3), DEAD_CELL_STATE)

        for offset_i in [-1, 0, 1]:
            for offset_j in [-1, 0, 1]:
                # checking only cells inside the grid, the other will remain set to DEAD_CELL_STATE
                if not (
                    i + offset_i < 0
                    or j + offset_j < 0
                    or i + offset_i >= self.grid_dim[1]
                    or j + offset_j >= self.grid_dim[0]
                ):
                    # retrieving cell mat value to create the neighbours
                    surr_neighbours[offset_i][offset_j] = self.cell_mat[i + offset_i][
                        j + offset_j
                    ]

        return surr_neighbours

    def validateGrid(self) -> None:
        """Make sure that the grid has authorized dimensions in regards to the resolution of the UI, and correct values for the cells too"""

        assert (
            np.array(self.grid_dim) % 2 == 0
        ).all(), "grid dimensions should be even numbers"

        assert np.all(
            [
                low <= x <= high
                for low, x, high in zip(
                    self.gameConfig["min_grid_dim"],
                    self.grid_dim,
                    self.gameConfig["res"],
                )
            ]
        ), f"grid_dim 0 ({self.grid_dim[0]}) should be between {self.gameConfig['min_grid_dim'][0]} and {self.gameConfig['res'][0]}"

        assert (
            (self.cell_mat == DEAD_CELL_STATE) | (self.cell_mat == ALIVE_CELL_STATE)
        ).all(), (
            "all cells should be represented by integer of 0 or 1 (dead or alive state)"
        )

    def getCellMat(self) -> np.ndarray:
        """Return the grid, representing the cells on the form of nest np array

        Returns:
            np.ndarray: the grid containing the cells
        """
        return self.cell_mat

    def setCell(self, i: int, j: int, value: GRID_CELL_STATE_TYPE):
        """Set the cell of the grid to a value passed in

        Args:
            i (int): row index of the cell
            j (int): column index of the cell
            value (Union[DEAD_CELL_STATE, ALIVE_CELL_STATE]): state assigned to the cell
        """
        self.cell_mat[i][j] = value
        self.validateGrid()

    def resetCellMat(self) -> None:
        """Reset the grid internal state (and it's previous state too)"""
        self.cell_mat = np.array([])
        self.old_cell_mat = np.array([])


if __name__ == "__main__":

    grid = CoreGrid(np.zeros((24, 24)))
    grid.prettyPrintCellMat()
