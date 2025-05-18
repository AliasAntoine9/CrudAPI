from typing import Union

from crud_api import settings
from crud_api.database.postgres_configuration import PostgresConfiguration
from crud_api.database.sqlite_configuration import SqliteConfiguration


class SetupConfiguration:
    @staticmethod
    def setup() -> Union[PostgresConfiguration, SqliteConfiguration]:
        if settings.database_type == "postgres":
            return PostgresConfiguration()
        elif settings.database_type == "sqlite":
            return SqliteConfiguration()
        else:
            raise ValueError(f"settings.database_type ({settings.database_type}) is wrong")
