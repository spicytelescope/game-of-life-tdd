"""
Tests regarding the CoreGrid functions
"""
import pytest
from src.core_lib.CoreGrid import CoreGrid
from tests.core_lib_tests.test_config import BAD_DIM_GRID_HIGH
from tests.core_lib_tests.test_config import BAD_DIM_GRID_LOW
from tests.core_lib_tests.test_config import INCORRECT_INIT_GRID
from tests.core_lib_tests.test_config import LOAD_TEST_EXPECTED_GRID
from tests.core_lib_tests.test_config import LOAD_TEST_INIT_GRID
from tests.core_lib_tests.test_config import LOAD_TEST_N_TURN
from tests.core_lib_tests.test_config import NO_LIVING_EXPECTED_GRID
from tests.core_lib_tests.test_config import NO_LIVING_INIT_GRID
from tests.core_lib_tests.test_config import NORMAL_EXPECTED_GRID
from tests.core_lib_tests.test_config import NORMAL_INIT_GRID
from tests.core_lib_tests.test_config import NORMAL_N_TURN

# pylint: disable=unused-variable


def test_core_behaviour() -> None:
    """checking good behaviour of the core functions and more precisely the 3 core rules of the game after n turns"""

    grid: CoreGrid = CoreGrid(NORMAL_INIT_GRID)
    for _ in range(NORMAL_N_TURN):
        grid.applyRules()

    assert grid.getCellMat() == NORMAL_EXPECTED_GRID


def load_test_core_behaviour() -> None:

    """checking core grid behaviour with a huge number of turn"""

    grid: CoreGrid = CoreGrid(LOAD_TEST_INIT_GRID)

    for _ in range(LOAD_TEST_N_TURN):
        grid.applyRules()

    assert grid.getCellMat() == LOAD_TEST_EXPECTED_GRID


def test_bad_grid_dim() -> None:
    """check if expected crash regarding inputed grid having dimensions outside limits defined in the config file"""

    with pytest.raises(ValueError):
        grid: CoreGrid = CoreGrid(BAD_DIM_GRID_HIGH)
    with pytest.raises(ValueError):
        grid: CoreGrid = CoreGrid(BAD_DIM_GRID_LOW)


def test_no_living_cells() -> None:
    """create a mock result that is expected not to yield out living cells"""

    grid: CoreGrid = CoreGrid(NO_LIVING_INIT_GRID)
    grid.applyRules()

    assert grid.getCellMat() == NO_LIVING_EXPECTED_GRID


def test_incorrect_grid_init() -> None:
    """check if expected crash regarding incorrect values (e.g. not 1 or 0) when initialising grid"""
    with pytest.raises(ValueError):
        grid: CoreGrid = CoreGrid(INCORRECT_INIT_GRID)
