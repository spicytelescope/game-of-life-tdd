"""UIButton class definition
"""

# pylint: disable=dangerous-default-value,too-many-arguments
from typing import List
import pygame


class UIButton:
    """Represent a UI element that can be clicked and trigger a callback"""

    def __init__(
        self,
        size: List[int],
        font_size: int,
        text_color: List[int] = [0, 0, 0],
        font: str = "consolas",
        label: str = "",
        clickable=True,
    ):

        self.size = size

        # ui
        self.ui_settings = {
            "font": pygame.font.Font(font, font_size),
            "label": label,
            "text_color": text_color,
        }

        # surface
        self.UNPRESSED_BUTTON_SPRITE: pygame.surface.Surface = pygame.image.load(
            "../../assets/unpressed_button_sprite.png"
        )
        self.PRESSED_BUTTON_SPRITE: pygame.surface.Surface = pygame.image.load(
            "../../assets/pressed_button_sprite.png"
        )
        self.surface = pygame.surface.Surface(size)

        # event
        self.clickable = clickable
        self.clicked = False

    def draw(self) -> pygame.surface.Surface:
        """draw the button surface according to ui parameters and the full drawn surface to be used by parent classes"""

        self.surface = pygame.surface.Surface(self.size)
        if self.clickable and self.clicked:
            self.surface = pygame.transform.scale(
                self.PRESSED_BUTTON_SPRITE, (self.size)
            )
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
