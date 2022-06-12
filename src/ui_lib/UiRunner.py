"""UiRunner class definition
"""
from typing import List, Union
import numpy as np
import pygame
from src.ui_lib.DisplayPanel import DisplayPanel
from src.ui_lib.InfoPanel import InfoPanel
from src.ui_lib.SettingPanel import SettingPanel
from src.utils.confUtils import fetch_game_config


class UIRunner:
    """Handle the UI, makes sure that each components is correctly rendered"""

    def __init__(
        self,
        res: Union[List[int], None] = None,
        grid_dim: Union[List[int], None] = None,
    ):
        # parameters
        self._config = fetch_game_config()
        self.res: List[int] = (
            res if res is not None else self._config["videoSettings"]["res"]
        )
        self.grid_dim: List[int] = (
            grid_dim if grid_dim is not None else self._config["videoSettings"]["res"]
        )
        self.validateUiParams()

        # main window
        self.screen: pygame.surface.Surface = pygame.display.set_mode(self.res)

        # ui elements
        self.display_panel: DisplayPanel = DisplayPanel()
        self.setting_panel: SettingPanel = SettingPanel()
        self.info_panel: InfoPanel = InfoPanel()

    def draw(self):
        """Draw each"""

    def validateUiParams(self) -> None:
        """Make sure that the grid has authorized dimensions in regards to the resolution of the UI, and correct values for the cells too, make sure that the res has values within limits, and on the right type"""

        # grid_dim check up
        assert (
            np.array(self.grid_dim) % 2 == 0
        ).all(), "grid dimensions should be even numbers"

        assert np.all(
            [
                low <= x <= high
                for low, x, high in zip(
                    self._config["videoSettings"]["min_grid_dim"],
                    self.grid_dim,
                    self._config["videoSettings"]["res"],
                )
            ]
        ), f"grid_dim ({self.grid_dim}) should be between {self._config['videoSettings']['min_grid_dim']} and {self._config['videoSettings']['res']}"

        assert (
            np.array(self.res) % 2 == 0
        ).all(), "grid dimensions should be even numbers"

        assert np.all(
            [
                low <= x <= high
                for low, x, high in zip(
                    self._config["videoSettings"]["res_min"],
                    self.res,
                    self._config["videoSettings"]["res_max"],
                )
            ]
        ), f"res ({self.res}) should be between {self._config['videoSettings']['res_min']} and {self._config['videoSettings']['res_max']}"
