"""InfoPanel class definition
"""
from datetime import datetime
from typing import Dict, List, Union
import pygame


class InfoPanel:
    """panel displaying to the screen the current infos for the turn :
    - the index of the turn itself
    - the number of alive cells
    - the elapsed time
    """

    def __init__(self, size: Union[List[int], None] = None, font: str = "consolas"):
        self.surface: Union[pygame.surface.Surface, None] = (
            pygame.surface.Surface(size) if size is not None else None
        )
        self.infos: Dict = {"alive_cells": 0, "turn": 1}
        self.font: str = font

        # === timer ===
        self.timer_enabled: bool = False
        # get the latest timestamp every second since the beggining of the simulation
        self.timer: Union[None, datetime] = None
        self.elapsed_seconds: Union[None, int] = None

    def _draw(self) -> None:
        """draw the infos to the surface"""

    def update(self) -> None:
        """draw the metrics from the UIRunner to the surface"""

        assert self.surface is not None, "display panel has not been initialised yet"
        self._draw()
        self.surface.fill((0, 255, 0))

    def setSurface(self, size: List[int]) -> None:
        """set the surface of the class by passing a size

        Args:
            size (List[int]): the size of the surface
        """

        self.surface = pygame.surface.Surface(size)

    def _refreshTimer(self) -> None:
        """refresh the timer"""
        if (
            self.timer_enabled
            and self.timer is not None
            and self.elapsed_seconds is not None
        ):
            if (datetime.now() - self.timer).total_seconds() > 1:
                self.timer = datetime.now()
                self.elapsed_seconds += 1

    def startTimer(self) -> None:
        """start the timer or restart it if the value in self.timer & self.elapsed_seconds aren't None"""
        self.timer_enabled = True
        if self.timer is None:
            self.timer = datetime.now()
            self.elapsed_seconds = 0

    def stopTimer(self) -> None:
        """stop the timer"""
        self.timer_enabled = False

    def resetTimer(self) -> None:
        """reset the timer by setting self.elapsed_seconds & self.timer to None"""
        self.timer = None
        self.elapsed_seconds = None

    def _getFormattedTime(self) -> str:
        """return the elapsed time from second to string with hours, minutes and seconds

        Returns:
            str: the formatted string following this format : %H:%m:%s
        """
        assert (
            self.elapsed_seconds is not None
        ), "Cannot format time because self.elapsed_seconds is None"

        num_hour: int = self.elapsed_seconds // 3600
        num_min: int = (self.elapsed_seconds - 3600 * num_hour) // 60
        remaining_sec: int = self.elapsed_seconds - 3600 * num_hour - 60 * num_min
        return f"{'0' if num_hour < 10 else ''}{num_hour}:{'0' if num_min < 10 else ''}{num_min}:{'0' if remaining_sec < 10 else ''}{remaining_sec}"

    def setInfos(self, alive_cells_number: int, turn_number: int) -> None:
        """set the infos regarding the current turn that will be displayed

        Args:
            alive_cells (int): number of cell alive for the turn
            turn_number (int): index of the turn
        """

        self.infos["alive_cells"] = alive_cells_number
        self.infos["turn"] = turn_number
