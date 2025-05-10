import sys
import tomli
import logging

with open("pyproject.toml", "rb") as file:
    pyproject = tomli.load(file)
__name__ = pyproject["project"]["name"]
__version__ = pyproject["project"]["version"]

logging.root.setLevel(logging.INFO)
logging.basicConfig(format="{asctime} - {levelname} - {message}", style="{", datefmt="%Y-%m-%d %H:%M:%S")
logger = logging.getLogger("Crud-API")

if "setup.py" not in sys.argv:

    from dynaconf import Dynaconf
    settings = Dynaconf(
        default_env="base",
        env="local",
        envvar_prefix="DYNACONF",
        environments=True,
        includes=["configs/**/*"],
        merge_enabled=True
    )

    settings.api_name = __name__
    settings.api_version = __version__
