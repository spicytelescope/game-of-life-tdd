"""utils regarding configuration file
"""
import json
import os
from typing import Dict


def fetch_game_config(conf_filepath: str = "../config.json"):
    """return the game config by fetching it from <conf_filepath>

    Args:
        conf_filepath (str, optional): path to the config file. Defaults to "../config.json".

    Returns:
        _type_: Dict containing the parameters of the game
    """
    script_path: str = os.path.dirname(os.path.abspath(__file__))
    conf_file_path: str = f"{script_path}/{conf_filepath}"

    assert (
        conf_file_path[-5:] == ".json"
    ), f"Bad file extension, the only supported one is 'json', not {conf_file_path[-5:]}"
    with open(conf_file_path, encoding="utf8") as f:
        conf_data: Dict = json.load(f)

    return conf_data


if __name__ == "__main__":
    print(fetch_game_config())
