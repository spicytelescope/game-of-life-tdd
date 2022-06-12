"""UiRunner class definition
"""
from typing import Dict, List, Union
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
        self.videoSettings: Dict = {
            "res": res if res is not None else self._config["videoSettings"]["res"],
            "grid_dim": grid_dim
            if grid_dim is not None
            else self._config["videoSettings"]["res"],
        }
        self.validateUIParams()

        # main window
        self.main_window: pygame.surface.Surface = pygame.surface.Surface((210, 210))

        # ui elements
        self.display_panel: DisplayPanel = DisplayPanel()
        self.setting_panel: SettingPanel = SettingPanel()
        self.info_panel: InfoPanel = InfoPanel()
        self.panel_blit_points: Dict = {
            "display": [0, 0],
            "setting": [0, 0],
            "info": [0, 0],
        }
        self._setBlitPoints()
        print(dir(self))

    def _setBlitPoints(self):
        """According to ui rules, each ui components as it's blit point depending on the resolution inputed"""
        self.panel_blit_points["settings"] = [
            int(0.7 * self.videoSettings["res"][0]),
            int(0.2 * self.videoSettings["res"][1]),
        ]

    def draw(self):
        """Draw each ui components on the main window"""

        self.main_window.fill(self._config["ui"]["background_color"])

    def validateUIParams(self) -> None:
        """Make sure that the grid has authorized dimensions in regards to the resolution of the UI, and correct values for the cells too, make sure that the res has values within limits, and on the right type"""

        # grid_dim check up
        assert (
            np.array(self.videoSettings["grid_dim"]) % 2 == 0
        ).all(), "grid dimensions should be even numbers"

        assert np.all(
            [
                low <= x <= high
                for low, x, high in zip(
                    self._config["videoSettings"]["min_grid_dim"],
                    self.videoSettings["grid_dim"],
                    self._config["videoSettings"]["res"],
                )
            ]
        ), f"grid_dim ({self.videoSettings['grid_dim']}) should be between {self._config['videoSettings']['min_grid_dim']} and {self._config['videoSettings']['res']}"

        assert (
            np.array(self.videoSettings["res"]) % 2 == 0
        ).all(), "grid dimensions should be even numbers"

        assert np.all(
            [
                low <= x <= high
                for low, x, high in zip(
                    self._config["videoSettings"]["res_min"],
                    self.videoSettings["res"],
                    self._config["videoSettings"]["res_max"],
                )
            ]
        ), f"res ({self.videoSettings['res']}) should be between {self._config['videoSettings']['res_min']} and {self._config['videoSettings']['res_max']}"


if __name__ == "__main__":

    ui_runner: UIRunner = UIRunner()
