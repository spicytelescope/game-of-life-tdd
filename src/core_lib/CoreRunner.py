"""MainRunner class definition
"""


class MainRunner:
    """Main runner communicating with every components, designed to interface with the main script"""

    def __init__(self):

        self.core_grid = None
        self.ui_runner = None

    def update(self):
        """_summary_"""
