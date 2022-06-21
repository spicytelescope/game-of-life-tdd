"""UIButton class definition
"""

# pylint: disable=dangerous-default-value,too-many-arguments,too-many-instance-attributes
import os
from typing import Callable, Dict, List, Union
from datetime import datetime
import pygame


class UIButton:
    """Represent a UI element that can be clicked and trigger a callback"""

    def __init__(
        self,
        size: List[int],
        font_size: int,
        label: str,
        text_color: List[int] = [0, 0, 0],
        font: str = "consolas",
        clickable: bool = True,
        callback: Union[None, Callable] = None,
    ):

        self.size: List[int] = size

        # ui
        self.ui_settings: Dict = {
            "font": pygame.font.SysFont(font, font_size),
            "label": label,
            "text_color": text_color,
        }

        # surface
        script_path: str = os.path.dirname(os.path.abspath(__file__))
        self.UNPRESSED_BUTTON_SPRITE: pygame.surface.Surface = pygame.image.load(
            f"{script_path}/../../assets/unpressed_button_sprite.png"
        ).convert_alpha()
        self.PRESSED_BUTTON_SPRITE: pygame.surface.Surface = pygame.image.load(
            f"{script_path}/../../assets/pressed_button_sprite.png"
        ).convert_alpha()
        self.surface: pygame.surface.Surface = pygame.surface.Surface(size)
        self.clickTimeoutTimer: datetime = datetime.now()

        # event
        self.clickable: bool = clickable
        self.clicked: bool = False
        self.callback: Union[None, Callable] = callback
        self.callback_available: bool = True

    def draw(self) -> pygame.surface.Surface:
        """draw the button surface according to ui parameters and the full drawn surface to be used by parent classes"""

        if self.clickable and self.clicked:
            # exectuing callback once after the click
            if self.callback is not None and self.callback_available:
                self.callback()
                self.callback_available = False

            self.surface = pygame.transform.scale(
                self.PRESSED_BUTTON_SPRITE, (self.size)
            )

            if (datetime.now() - self.clickTimeoutTimer).total_seconds() > 1:
                self.clicked = False
                self.callback_available = True

        else:
            self.surface = pygame.transform.scale(
                self.UNPRESSED_BUTTON_SPRITE, (self.size)
            )

        text_surf: pygame.surface.Surface = self.ui_settings["font"].render(
            self.ui_settings["label"], True, self.ui_settings["text_color"]
        )
        self.surface.blit(
            text_surf, text_surf.get_rect(center=[self.size[0] // 2, self.size[1] // 2])
        )

        return self.surface

    def setClickState(self, clickState: bool) -> None:
        """set the click state

        Args:
            clickState (bool): pygame event object checked for the click
        """
        # start the timer
        if clickState and not self.clicked:
            self.clickTimeoutTimer = datetime.now()

        self.clicked = clickState
