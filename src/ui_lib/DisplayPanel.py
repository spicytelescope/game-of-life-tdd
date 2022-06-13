"""DisplayPanel class definition
"""

from typing import List, Union
import pygame


class DisplayPanel:
    """_summary_"""

    def __init__(self, size: Union[List[int], None] = None):
        self.surface: Union[pygame.surface.Surface, None] = (
            pygame.surface.Surface(size) if size is not None else None
        )

    def update(self) -> None:
        """draw the new internal state of the grid to the surface"""

        assert self.surface is not None, "display panel has not been initialised yet"
        self.surface.fill((255, 0, 0))

    def setSurface(self, size: List[int]) -> None:
        """set the surface of the class by passing a size

        Args:
            size (List[int]): the size of the surface
        """
        self.surface = pygame.surface.Surface(size)

    # TODO displayPannel implementation
