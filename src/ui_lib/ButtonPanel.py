"""ButtonPanel class definition
"""
# pylint: disable=dangerous-default-value,too-many-arguments
from typing import Dict, List
import pygame
from src.ui_lib.UIButton import UIButton


class ButtonPanel:
    """pannel display to the screen 3 buttons for the user to interact with :
    - start button
    - pause button
    - reset button"""

    def __init__(
        self,
        size: List[int],
        font_size: int,
        callbacks: Dict,
        font: str = "consolas",
        text_color: List[int] = [0, 0, 0],
        background_color: List[int] = [173, 216, 230],
    ):

        # surface
        self.size: List[int] = size
        self.surface: pygame.surface.Surface = pygame.surface.Surface(size)

        # components
        self.labels: List[str] = ["START", "STOP", "RESET"]
        self.callbacks: Dict = callbacks
        self.buttons: List[UIButton] = [
            UIButton(
                [self.size[0] // 2, self.size[1] // (len(self.labels) * 2)],
                font_size * 2,  # factor 2 to get big button text effect
                label=label,
                callback=self.callbacks[label],
            )
            for label in self.labels
        ]
        self.blitPoints = {
            self.labels[i]: [
                self.size[0] // 2,
                self.size[1] // (len(self.labels) * 2)
                + i * self.size[1] // len(self.labels),
            ]
            for i in range(len(self.labels))
        }

        # ui
        self.ui_settings: Dict = {
            "font": pygame.font.SysFont(font, font_size),
            "text_color": text_color,
            "background_color": background_color,
        }

    def update(self) -> None:
        """_summary_"""

        assert self.surface is not None, "display panel has not been initialised yet"
        self._draw()

    def _draw(self):
        """draw to the screen the different buttons"""

        assert (
            self.surface is not None and self.size is not None
        ), "info panel has not been initialised yet"

        self.surface.fill(self.ui_settings["background_color"])
        for button in self.buttons:
            button_surf: pygame.surface.Surface = button.draw()
            self.surface.blit(
                button_surf,
                button.surface.get_rect(
                    center=self.blitPoints[button.ui_settings["label"]]
                ),
            )

    def checkEvents(self, clickPos: List[float]) -> None:
        """Update the click state of each button according to the event captured

        Args:
            event (pygame.event.Event): pygame event object checked for the click
        """
        for button in self.buttons:
            button.setClickState(
                button.surface.get_rect(
                    center=self.blitPoints[button.ui_settings["label"]]
                ).collidepoint(clickPos)
            )
