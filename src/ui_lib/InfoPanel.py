"""InfoPanel class definition
"""
# pylint: disable=dangerous-default-value,too-many-arguments,too-many-instance-attributes
from datetime import datetime
from typing import Dict, List, Union
import pygame


class InfoPanel:
    """panel displaying to the screen the current infos for the turn :
    - the index of the turn itself
    - the number of alive cells
    - the elapsed time
    """

    def __init__(
        self,
        size: List[int],
        font_size: int,
        font: str = "consolas",
        text_color: List[int] = [0, 0, 0],
        background_color: List[int] = [255, 255, 255],
    ):
        self.size = size
        self.surface: pygame.surface.Surface = pygame.surface.Surface(size)
        self.infos: Dict = {"alive_cells": 0, "turn": 1}
        self.ui_settings = {
            "font": pygame.font.SysFont(font, font_size),
            "text_color": text_color,
            "background_color": background_color,
        }

        # === timer ===
        self.timer_enabled: bool = False
        # get the latest timestamp every second since the beggining of the simulation
        self.timer: Union[None, datetime] = None
        self.elapsed_seconds: Union[None, int] = None

        # edit mode
        self.displayEditMode: bool = False
        self.edit_mode_text_surfs: List[pygame.surface.Surface] = [
            self.ui_settings["font"].render(
                text,
                True,
                self.ui_settings["text_color"],
            )
            for text in [
                "Edit mode running,",
                "press [ENTER] to start",
                "the simulation",
            ]
        ]

    def _draw(self) -> None:
        """draw the infos to the surface"""

        self._refreshTimer()
        assert (
            self.surface is not None and self.size is not None
        ), "info panel has not been initialised yet"

        self.surface.fill(self.ui_settings["background_color"])
        surfs = [
            self.ui_settings["font"].render(
                f"Alive cells : {self.infos['alive_cells']}",
                True,
                self.ui_settings["text_color"],
            ),
            self.ui_settings["font"].render(
                f"Turn #{self.infos['turn']}", True, self.ui_settings["text_color"]
            ),
            self.ui_settings["font"].render(
                f"Time : {self._getFormattedTime()}",
                True,
                self.ui_settings["text_color"],
            ),
        ]

        if self.displayEditMode:
            for i, text_surf in enumerate(self.edit_mode_text_surfs):
                self.surface.blit(
                    text_surf,
                    text_surf.get_rect(
                        center=[
                            self.size[0] // 2,
                            self.size[1] // (len(self.edit_mode_text_surfs) * 2)
                            + i * (self.size[1] // len(self.edit_mode_text_surfs)),
                        ]
                    ),
                )
        else:
            for i in range(len(self.infos.keys()) + 1):
                surf = surfs[i]
                self.surface.blit(
                    surf,
                    surf.get_rect(
                        center=[self.size[0] // 2, self.size[1] // (len(surfs) * 2) + i * self.size[1] // len(surfs)]  # type: ignore
                    ),
                )

    def update(self) -> None:
        """draw the metrics from the UIRunner to the surface"""

        self._draw()

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
        num_hour: int = 0
        num_min: int = 0
        remaining_sec: int = 0

        if self.elapsed_seconds is not None:
            num_hour = self.elapsed_seconds // 3600
            num_min = (self.elapsed_seconds - 3600 * num_hour) // 60
            remaining_sec = self.elapsed_seconds - 3600 * num_hour - 60 * num_min

        return f"{'0' if num_hour < 10 else ''}{num_hour}:{'0' if num_min < 10 else ''}{num_min}:{'0' if remaining_sec < 10 else ''}{remaining_sec}"

    def setInfos(self, alive_cells_number: int, turn_number: int) -> None:
        """set the infos regarding the current turn that will be displayed

        Args:
            alive_cells (int): number of cell alive for the turn
            turn_number (int): index of the turn
        """

        self.infos["alive_cells"] = alive_cells_number
        self.infos["turn"] = turn_number

    def setEditMode(self, state: bool) -> None:
        """set the state of the displayEditMode flag

        Args:
            state (bool): value to set the flag
        """
        self.displayEditMode = state
