"""DisplayPanel class definition
"""
# pylint: disable=dangerous-default-value,too-many-arguments

from math import ceil
import sys
from typing import Dict, List
import numpy as np
import pygame
from src.utils.CustomTypes import ALIVE_CELL_STATE, DEAD_CELL_STATE


class DisplayPanel:
    """Handle the display of the grid, represent the real time state of the core grid
    Furthermore, before the game begins, it let the user place the first cells (create the inital game state)
    """

    def __init__(
        self,
        size: List[int],
        grid_dim: List[int],
        font_size: int,
        editModeCallbacks: Dict,
        font: str = "consolas",
        text_color: List[int] = [0, 0, 0],
        background_color: List[int] = [0, 0, 0],
        grid_color: List[int] = [255, 255, 255],
        cell_color: List[int] = [255, 0, 0],
    ):
        # surface
        self.size: List[int] = size
        self.surface: pygame.surface.Surface = pygame.surface.Surface(size)

        # ui
        self.ui_settings = {
            "font": pygame.font.SysFont(font, font_size),
            "text_color": text_color,
            "background_color": background_color,
            "grid_color": grid_color,
            "cell_color": cell_color,
        }

        # grid handling
        self.grid_dim: List[int] = grid_dim
        self.cell_mat: np.ndarray = np.array(np.zeros(self.grid_dim))
        self.CELL_SHAPE: List[int] = [
            ceil(res_dim / grid_dim)
            for res_dim, grid_dim in zip(self.size, self.grid_dim)
        ]
        self.editModeCallbacks = editModeCallbacks

    def update(self) -> None:
        """draw the new internal state of the grid to the surface"""

        assert self.surface is not None, "display panel has not been initialised yet"
        self.surface.fill(self.ui_settings["background_color"])
        self._draw()

    def setCellMat(self, new_cell_mat: np.ndarray) -> None:
        """set the cell mat, this function is called each time a new state of the internal grid is coming and needs to be displayed

        Args:
            new_cell_mat (np.ndarray): the new cell mat
        """
        self.cell_mat = new_cell_mat

    def _draw(self) -> None:
        """draw the interal core grid state to the surface, according to the ui colors inputed"""
        # draw the grid

        for i in range(self.grid_dim[1]):
            start_point: List[int] = [0, i * self.CELL_SHAPE[1]]
            end_point: List[int] = [self.size[0], i * self.CELL_SHAPE[1]]
            pygame.draw.aaline(
                self.surface, self.ui_settings["grid_color"], start_point, end_point
            )

        for j in range(self.grid_dim[0]):
            start_point = [j * self.CELL_SHAPE[0], 0]
            end_point = [j * self.CELL_SHAPE[0], self.size[1]]
            pygame.draw.aaline(
                self.surface, self.ui_settings["grid_color"], start_point, end_point
            )

        # fill the grid according to cell_matrix
        for i in range(self.grid_dim[1]):
            for j in range(self.grid_dim[1]):
                if self.cell_mat[i][j] == ALIVE_CELL_STATE:

                    # note that the "+1" and "-1" are here to highlight the grid by putting constraint on the cell display
                    pygame.draw.rect(
                        self.surface,
                        self.ui_settings["cell_color"],
                        [
                            j * self.CELL_SHAPE[0] + 1,
                            i * self.CELL_SHAPE[1] + 1,
                            self.CELL_SHAPE[0] - 1,
                            self.CELL_SHAPE[1] - 1,
                        ],
                    )

    def runEditMode(self) -> None:
        """create a custom game loop to edit and create an initial grid before running the simulation"""

        # this function triggers its own internal game loop
        edit_mode_running = True
        while edit_mode_running:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and all(
                    0 <= event.pos[x] < self.size[x] for x in [0, 1]
                ):
                    cell_coor_selected = [
                        event.pos[x] // self.CELL_SHAPE[x] for x in [0, 1]
                    ]
                    self.cell_mat[cell_coor_selected[1]][cell_coor_selected[0]] = (
                        ALIVE_CELL_STATE
                        if self.cell_mat[cell_coor_selected[1]][cell_coor_selected[0]]
                        == DEAD_CELL_STATE
                        else DEAD_CELL_STATE
                    )

                elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    edit_mode_running = False
                elif event.type == pygame.QUIT:
                    sys.exit()

            self.editModeCallbacks["refresh_screen"]()
            self._draw()
            pygame.display.flip()
