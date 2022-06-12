"""
Tests regarding the CoreGrid functions
"""
# pylint: disable=unused-variable,unused-argument, redefined-outer-name
import os
import pytest
from numpy.testing import assert_array_equal
from src.core_lib.CoreGrid import CoreGrid
from src.utils.confUtils import fetch_game_config
from tests.core_lib_tests.test_config import BAD_DIM_GRID_HIGH
from tests.core_lib_tests.test_config import BAD_DIM_GRID_LOW
from tests.core_lib_tests.test_config import BAD_DIM_GRID_ODD
from tests.core_lib_tests.test_config import INCORRECT_INIT_GRID
from tests.core_lib_tests.test_config import INCORRECT_VALUE_SET_CELL
from tests.core_lib_tests.test_config import LOAD_TEST_EXPECTED_GRID
from tests.core_lib_tests.test_config import LOAD_TEST_INIT_GRID
from tests.core_lib_tests.test_config import LOAD_TEST_N_TURN
from tests.core_lib_tests.test_config import NO_LIVING_EXPECTED_GRID
from tests.core_lib_tests.test_config import NO_LIVING_INIT_GRID
from tests.core_lib_tests.test_config import NORMAL_EXPECTED_GRID
from tests.core_lib_tests.test_config import NORMAL_INIT_GRID
from tests.core_lib_tests.test_config import NORMAL_N_TURN


@pytest.fixture()
def mock_config_file_handler():
    """Fixture to create a mock config file and clean-up it"""
    script_path: str = os.path.dirname(os.path.abspath(__file__))
    with open(f"{script_path}/../../src/utils/config.yaml", "w", encoding="utf-8") as f:
        f.write("Config file with bad extension")
        f.close()

    yield

    os.remove(f"{script_path}/../../src/utils/config.yaml")


def test_core_behaviour() -> None:
    """checking good behaviour of the core functions and more precisely the 3 core rules of the game after n turns"""

    grid: CoreGrid = CoreGrid(NORMAL_INIT_GRID)
    for _ in range(NORMAL_N_TURN):
        grid.applyRules()

    assert_array_equal(
        grid.getCellMat(), NORMAL_EXPECTED_GRID, err_msg="Grids aren't matching"
    )


# @pytest.mark.skip(reason="is way too slow")
def test_load_core_behaviour() -> None:

    """checking core grid behaviour with a huge number of turn"""

    grid: CoreGrid = CoreGrid(LOAD_TEST_INIT_GRID)

    for _ in range(LOAD_TEST_N_TURN):
        grid.applyRules()

    assert_array_equal(
        grid.getCellMat(), LOAD_TEST_EXPECTED_GRID, err_msg="Grids aren't matching"
    )


@pytest.mark.parametrize(
    "test_input_grid_dim", [BAD_DIM_GRID_HIGH, BAD_DIM_GRID_LOW, BAD_DIM_GRID_ODD]
)
def test_bad_grid_dim(test_input_grid_dim) -> None:
    """check if expected crash regarding inputed grid having dimensions outside limits defined in the config file"""

    with pytest.raises(AssertionError):
        grid: CoreGrid = CoreGrid(test_input_grid_dim)


def test_incorrect_grid_init() -> None:
    """check if expected crash regarding incorrect values (e.g. not 1 or 0) when initialising grid"""
    with pytest.raises(AssertionError):
        grid: CoreGrid = CoreGrid(INCORRECT_INIT_GRID)


def test_no_living_cells() -> None:
    """create a mock result that is expected not to yield out living cells"""

    grid: CoreGrid = CoreGrid(NO_LIVING_INIT_GRID)
    grid.applyRules()

    assert_array_equal(
        grid.getCellMat(),
        NO_LIVING_EXPECTED_GRID,
        err_msg="Grids aren't matching",
    )


def test_incorrect_set_cell() -> None:
    """checking if trying to add incorrect value (e.g. not in 0 or 1 to the grid using setCell method raise error) raise expected error"""

    with pytest.raises(AssertionError):
        grid: CoreGrid = CoreGrid(NORMAL_INIT_GRID)
        grid.setCell(0, 0, INCORRECT_VALUE_SET_CELL)  # type: ignore


def test_bad_config() -> None:
    """checking if trying to load incorrect config raises expected exception"""

    with pytest.raises(FileNotFoundError):
        fetch_game_config("../../some_bad_path.json")


def test_incorrect_config_file(mock_config_file_handler) -> None:
    """checking if trying to load at bad location a config file, or with bad extension raises expected exception"""

    with pytest.raises(AssertionError):
        fetch_game_config("config.yaml")
