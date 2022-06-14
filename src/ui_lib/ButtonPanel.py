"""ButtonPanel class definition
"""
from typing import List, Union
import pygame


class ButtonPanel:
    """_summary_"""

    def __init__(self, size: Union[List[int], None] = None):
        self.surface: Union[pygame.surface.Surface, None] = (
            pygame.surface.Surface(size) if size is not None else None
        )

    def update(self) -> None:
        """_summary_"""

        assert self.surface is not None, "display panel has not been initialised yet"

    def setSurface(self, size: List[int]) -> None:
        """set the surface of the class by passing a size

        Args:
            size (List[int]): the size of the surface
        """

        self.surface = pygame.surface.Surface(size)
