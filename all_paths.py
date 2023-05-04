import pathlib
from typing import Final

ROOT_PATH: Final[pathlib.Path] = pathlib.Path(__file__).parent
PATH_TO_PROXIES: Final[pathlib.Path] = ROOT_PATH.joinpath("proxies.yaml")
PATH_TO_KEYS: Final[pathlib.Path] = ROOT_PATH.joinpath("api-keys.yaml")
