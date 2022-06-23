"""MainRunner class definition
"""
from datetime import datetime
from typing import Union

import numpy as np
from src.ui_lib.UiRunner import UIRunner
from src.core_lib.CoreGrid import CoreGrid
from src.utils.confUtils import fetch_game_config


class MainRunner:
    """Main runner communicating with every components, designed to interface with the main script"""

    def __init__(self) -> None:

        # components
        self.gameConfig = fetch_game_config()
        self.core_grid: Union[None, CoreGrid] = None
        self.ui_runner: UIRunner = UIRunner(
            self.gameConfig,
            gameCallbacks={
                "START": self.startSimulation,
                "STOP": self.stopSimulation,
                "RESET": self.resetSimulation,
            },
        )

        # game state
        self.simulationRunning: bool = False

        # turn handling
        assert (
            self.gameConfig["simulation"]["turn_timeout"] > 0
        ), "turn timeout interval must be greater than 0"
        self.gameTurn: int = 0
        self.turnTimeoutTimer: datetime = datetime.now()

    def mainLoop(self) -> None:
        """Start the main game loop"""

        default_cell_mat: np.ndarray = self.ui_runner.runEditMode()
        self.core_grid = CoreGrid(self.gameConfig, default_cell_mat)

        continue_game: bool = True

        while continue_game:

            # turn updating in regars to the timeout
            if (
                self.simulationRunning
                and (datetime.now() - self.turnTimeoutTimer).total_seconds() * 1000
                > self.gameConfig["simulation"]["turn_timeout"]
            ):
                self.turnTimeoutTimer = datetime.now()
                self.addTurn()

            self.ui_runner.checkEvent()
            self.ui_runner.update()

    def setSimulationState(self, new_simulation_state: bool) -> None:
        """set the simulation state, pretty self explanatory

        Args:
            new_simulation_state (bool): new simulation state
        """
        self.simulationRunning = new_simulation_state

    def addTurn(self) -> None:
        """Add a turn by :
        - computing the next cell matrix state in core_grid
        - retrieving all new informations from core_grid and transmit them to the ui_runner
        """

        self.gameTurn += 1

        # core grid update
        assert self.core_grid is not None, "core_grid not initialised in main loop"
        self.core_grid.applyRules()

        # ui update
        self.ui_runner.info_panel.setInfos(
            self.core_grid.getAliveCellCount(), self.gameTurn
        )
        self.ui_runner.display_panel.setCellMat(self.core_grid.getCellMat())

    def startSimulation(self) -> None:
        """start the simulation, by starting the timer and setting the right simulation state"""

        self.setSimulationState(True)
        self.ui_runner.info_panel.startTimer()
        for button in list(self.ui_runner.button_panel.buttons.values()):
            button.setClickableState(False) if button.ui_settings[
                "label"
            ] == "START" else button.setClickableState(True)

    def stopSimulation(self) -> None:
        """stop the simulation, by stopping the timer and setting the right simulation state"""
        self.setSimulationState(False)
        self.ui_runner.info_panel.stopTimer()
        for button in list(self.ui_runner.button_panel.buttons.values()):
            button.setClickableState(False) if button.ui_settings[
                "label"
            ] == "STOP" else button.setClickableState(True)

    def resetSimulation(self) -> None:
        """reset the simulation, by reseting the timer but also the cell mat to its original state in both the core grid AND the ui (display panel)

        Afterward, run the edit mode"""
        self.setSimulationState(False)
        self.gameTurn = 0

        # ui button reset
        self.ui_runner.info_panel.resetTimer()

        # reset cell mat in every components
        assert self.core_grid is not None, "core_grid is not initialised properly"
        self.core_grid.resetCellMat()
        self.ui_runner.display_panel.setCellMat(self.core_grid.initial_cell_mat)

        # create new default cell mat & reset infos
        default_cell_mat: np.ndarray = self.ui_runner.runEditMode()
        self.core_grid.initCellMat(default_cell_mat)
