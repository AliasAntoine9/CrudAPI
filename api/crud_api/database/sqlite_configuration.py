from typing import Dict, Optional

from pydantic import SecretStr
from sqlalchemy import create_engine, Engine, URL
from sqlalchemy.orm import sessionmaker

from crud_api import settings, logger


class SqliteConfiguration:
    def __init__(self):
        self._database_type: str = settings.database_type
        self._drivername: Optional[str] = None
        self._host: Optional[str] = None
        self._port: Optional[int] = None
        self._database: Optional[str] = None
        self._database_schema: Optional[str] = None
        self._with_echo: bool = False

    def load_from_settings(self) -> None:
        try:
            secrets_db = dict(settings.secrets.database.get(self._database_type))
        except Exception:
            logger.warning("Database secrets could not be loaded!")
            secrets_db = {}
        configs_db = {**settings.database.get(self._database_type), **secrets_db}
        self._set_attributes(configs_db)

    def _set_attributes(self, configs: Dict):
        for config_name, value in configs.items():
            if config_name != "password":
                setattr(self, f"_{config_name}", value)
            else:
                setattr(self, f"_{config_name}", SecretStr(value))

    @staticmethod
    def create_session(engine: Engine):
        return sessionmaker(autocommit=False, autoflush=False, bind=engine)

    def create_engine(self) -> Engine:
        url = URL.create(
            drivername=self._drivername,
            host=self._host,
            database=self._database,
        )
        connect_args = {"check_same_thread": False}

        return create_engine(
            url,
            echo=self._with_echo,
            connect_args=connect_args,
            pool_recycle=3600
        )
