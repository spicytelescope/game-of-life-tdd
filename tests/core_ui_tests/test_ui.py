"""
Tests regarding the ui_lib functions
"""
# pylint: disable=unused-variable

import pytest
from src.ui_lib.UiRunner import UIRunner
from tests.core_ui_tests.test_config import BAD_DIM_HIGH
from tests.core_ui_tests.test_config import BAD_DIM_LOW
from tests.core_ui_tests.test_config import BAD_DIM_ODD
from tests.core_ui_tests.test_config import BAD_RES_HIGH
from tests.core_ui_tests.test_config import BAD_RES_LOW
from tests.core_ui_tests.test_config import BAD_RES_ODD
from tests.core_ui_tests.test_config import BAD_FONT
from tests.core_ui_tests.test_config import BAD_BG_COLOR
from tests.core_ui_tests.test_config import BAD_CELL_COLOR
from tests.core_ui_tests.test_config import BAD_TEXT_COLOR


@pytest.mark.parametrize(
    "test_input_grid_dim", [BAD_DIM_HIGH, BAD_DIM_LOW, BAD_DIM_ODD]
)
def test_bad_grid_dim(test_input_grid_dim) -> None:
    """check if expected crash regarding inputed grid having dimensions outside limits defined in the config file"""

    with pytest.raises(AssertionError):
        ui_runner: UIRunner = UIRunner(grid_dim=test_input_grid_dim)


@pytest.mark.parametrize("test_input_res", [BAD_RES_LOW, BAD_RES_HIGH, BAD_RES_ODD])
def test_bad_res(test_input_res) -> None:
    """check if expected crash regarding inputed res having dimensions outside limits defined in the config file"""

    with pytest.raises(AssertionError):
        ui_runner: UIRunner = UIRunner(res=test_input_res)


def test_bad_font() -> None:
    """check if a bad font raises expected error"""
    with pytest.raises(AssertionError):
        ui_runner: UIRunner = UIRunner(font=BAD_FONT)


def test_bad_colors() -> None:
    """check if a bad color for the background / cells raises expected error"""

    with pytest.raises(AssertionError):
        ui_runner: UIRunner = UIRunner(background_color=BAD_BG_COLOR)
    with pytest.raises(AssertionError):
        ui_runner: UIRunner = UIRunner(cell_color=BAD_CELL_COLOR)
    with pytest.raises(AssertionError):
        ui_runner: UIRunner = UIRunner(text_color=BAD_TEXT_COLOR)
