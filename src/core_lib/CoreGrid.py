"""CoreGric class definition
"""
from typing import Dict

import copy
import numpy as np
from numpy.typing import _Shape
from tabulate import tabulate  # type: ignore
from src.utils.confUtils import fetch_game_config
from src.utils.CustomTypes import ALIVE_CELL_STATE
from src.utils.CustomTypes import DEAD_CELL_STATE
from src.utils.CustomTypes import GRID_CELL_STATE_TYPE


class CoreGrid:
    """Handle the main grid which keep tracks of the current state of the game's cells, core functions for the grid processing"""

    def __init__(self, default_cell_mat: np.ndarray):

        self._turn = 0

        self.initial_cell_mat: np.ndarray = default_cell_mat  # used for resetCellmat()
        self.cell_mat: np.ndarray = default_cell_mat
        self.old_cell_mat: np.ndarray = default_cell_mat
        self.grid_dim: _Shape = default_cell_mat.shape
        self.gameConfig: Dict = fetch_game_config()["videoSettings"]
        self.validateGrid()

    def prettyPrintCellMat(self, tabulate_fmt="grid") -> None:
        """Pretty print the grid using tabulate 'grid' format"""

        print(f"================ #{self._turn} ================")
        print(tabulate(self.cell_mat, tablefmt=tabulate_fmt))

    def applyRules(
        self,
    ) -> None:
        """Apply the 3 main rules of the Game of Life to the main matrix"""

        self._turn += 1
        self.old_cell_mat = copy.deepcopy(self.cell_mat)

        for i in range(self.grid_dim[0]):
            for j in range(self.grid_dim[1]):
                self.setCell(i, j, self._applyRulesOnCell(i, j))
        # self.prettyPrintCellMat()

    def _applyRulesOnCell(self, i: int, j: int) -> GRID_CELL_STATE_TYPE:
        """apply the rules on one cell, selected by its indexes on the grid

        Args:
            i (int): row index of the cell
            j (int): column index of the cell

        Returns:
            GRID_CELL_STATE_TYPE: the next state on the cell after 1 turn
        """
        cell_state: GRID_CELL_STATE_TYPE = self.old_cell_mat[i][j]
        next_state: GRID_CELL_STATE_TYPE = DEAD_CELL_STATE

        cell_surrounding: np.ndarray = self.__getCurrentNeighbors(i, j)
        if cell_state == ALIVE_CELL_STATE:
            # substracting one because the current cell tested is alrady on the 'alive' state
            if sum(
                np.count_nonzero(x == ALIVE_CELL_STATE) for x in cell_surrounding
            ) - 1 in [2, 3]:
                next_state = ALIVE_CELL_STATE  # alive cell surviving, rule #1
        else:
            if (
                sum(np.count_nonzero(x == ALIVE_CELL_STATE) for x in cell_surrounding)
                == 3
            ):
                next_state = ALIVE_CELL_STATE  # dead cell becoming alive, rule #2

        return next_state

    def __getCurrentNeighbors(self, i: int, j: int) -> np.ndarray:
        """Return the current neighborhood of the cell at row i and column j, regardless of the border of the grid, set the out-of-border neighbour to DEAD_CELL_STATE.

        Args:
            i (int): row index of the cell
            j (int): column index of the cell

        Returns:
            np.ndarray: neighborhood of the cell at row i and column j of the grid
        """
        surr_neighbours: np.ndarray = np.full((3, 3), DEAD_CELL_STATE)

        for offset_i in [-1, 0, 1]:
            for offset_j in [-1, 0, 1]:
                # checking only cells inside the grid, the other will remain set to DEAD_CELL_STATE
                if not (
                    i + offset_i < 0
                    or j + offset_j < 0
                    or i + offset_i > self.grid_dim[0] - 1
                    or j + offset_j > self.grid_dim[1] - 1
                ):
                    # retrieving cell mat value to create the neighbours
                    surr_neighbours[offset_i + 1][offset_j + 1] = self.old_cell_mat[
                        i + offset_i
                    ][j + offset_j]

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
        ), f"grid_dim ({self.grid_dim}) should be between {self.gameConfig['min_grid_dim']} and {self.gameConfig['res']}"

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
        self.cell_mat = copy.deepcopy(self.initial_cell_mat)
        self.old_cell_mat = copy.deepcopy(self.initial_cell_mat)


if __name__ == "__main__":

    grid: CoreGrid = CoreGrid(np.zeros((24, 24)))
    grid.prettyPrintCellMat()
