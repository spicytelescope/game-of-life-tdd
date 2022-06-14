"""UiRunner class definition
"""
# pylint: disable=too-many-arguments
import sys
from typing import Dict, List, Union
import numpy as np
import pygame
from src.ui_lib.DisplayPanel import DisplayPanel
from src.ui_lib.InfoPanel import InfoPanel
from src.ui_lib.ButtonPanel import ButtonPanel
from src.utils.confUtils import fetch_game_config


class UIRunner:
    """Handle the UI, makes sure that each components is correctly rendered"""

    def __init__(
        self,
        res: Union[List[int], None] = None,
        grid_dim: Union[List[int], None] = None,
        font: Union[str, None] = None,
        background_color: Union[List[int], None] = None,
        cell_color: Union[List[int], None] = None,
        text_color: Union[List[int], None] = None,
    ) -> None:

        # parameters
        self._config = fetch_game_config()
        self.videoSettings: Dict = {
            "res": res if res is not None else self._config["videoSettings"]["res"],
            "grid_dim": grid_dim
            if grid_dim is not None
            else self._config["videoSettings"]["grid_dim"],
            "font": font if font is not None else self._config["ui"]["font"],
            "background_color": background_color
            if background_color is not None
            else self._config["ui"]["background_color"],
            "cell_color": cell_color
            if cell_color is not None
            else self._config["ui"]["cell_color"],
            "text_color": text_color
            if text_color is not None
            else self._config["ui"]["text_color"],
        }
        self.validateUIParams()

        # main window
        pygame.init()
        pygame.display.set_caption("Game of Life - Spicy Telescope Version")
        self.main_window: pygame.surface.Surface = pygame.display.set_mode(
            self.videoSettings["res"]  # type: ignore
        )

        # ui elements
        self.display_panel: DisplayPanel = DisplayPanel()
        self.setting_panel: ButtonPanel = ButtonPanel()

        self.panel_blit_points: Dict = {
            "display": [0, 0],
            "setting": [0, 0],
            "info": [0, 0],
        }
        self._initUIElements()

    def _initUIElements(self) -> None:
        """According to ui rules, each ui components as it's blit point depending on the resolution inputed and its size, this function correctly set them for each ui comp"""

        # blit points
        self.panel_blit_points["setting"] = [
            int(0.7 * self.videoSettings["res"][0]),
            int(0.2 * self.videoSettings["res"][1]),
        ]
        self.panel_blit_points["info"] = [
            int(0.7 * self.videoSettings["res"][0]),
            0,
        ]

        # surface
        self.display_panel.setSurface(
            [int(0.7 * self.videoSettings["res"][0]), self.videoSettings["res"][1]]
        )
        self.setting_panel.setSurface(
            [
                int(0.3 * self.videoSettings["res"][0]),
                int(0.8 * self.videoSettings["res"][1]),
            ]
        )

        self.info_panel: InfoPanel = InfoPanel(
            [
                int(0.3 * self.videoSettings["res"][0]),
                int(0.2 * self.videoSettings["res"][1]),
            ],
            font=str(self.videoSettings["font"]),
        )

    def __refreshComponents(self) -> None:
        """make the info and display panels draw their provided and updated data for the turn done  :
        - the display panel draws the new core grid internal state
        - the info panel draw the metrics
        """
        self.setting_panel.update()
        self.display_panel.update()
        self.info_panel.update()

    def _draw(self) -> None:
        """Draw each ui components on the main window"""

        assert (
            self.display_panel.surface is not None
        ), "display panel has not been initialised yet"
        assert (
            self.setting_panel.surface is not None
        ), "setting panel has not been initialised yet"
        assert (
            self.info_panel.surface is not None
        ), "info panel has not been initialised yet"

        pygame.surface.Surface.fill(
            self.main_window, tuple(self._config["ui"]["background_color"])
        )

        self.__refreshComponents()
        self.main_window.blit(
            self.display_panel.surface, self.panel_blit_points["display"]
        )
        self.main_window.blit(
            self.setting_panel.surface, self.panel_blit_points["setting"]
        )
        self.main_window.blit(self.info_panel.surface, self.panel_blit_points["info"])

    def updateTurn(self) -> None:
        """update the main screen"""
        self._draw()
        pygame.display.flip()

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

        assert (
            self.videoSettings["font"] in pygame.font.get_fonts()
        ), f"Unknown {self.videoSettings['font']} (pygame.font.get_fonts() to know the available ones)"

        for test_color_name in ["background_color", "cell_color", "text_color"]:
            assert (
                (np.array(self.videoSettings[test_color_name]) >= 0)
                & (np.array(self.videoSettings[test_color_name]) <= 255)
            ).all(), f"{test_color_name} ({self.videoSettings[test_color_name]}) have pixel value not between 0 and 255"


if __name__ == "__main__":

    import random

    ui_runner: UIRunner = UIRunner()
    ui_runner.info_panel.startTimer()
    turn = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    turn += 1
                    ui_runner.info_panel.setInfos(random.randint(1, 40), turn)

        ui_runner.updateTurn()
