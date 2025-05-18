from typing import Generator

from sqlalchemy.orm import Session

from crud_api import logger
from crud_api.database.setup_configuration import SetupConfiguration


database_configuration = SetupConfiguration().setup()
database_configuration.load_from_settings()

ENGINE = database_configuration.create_engine()
SESSION = database_configuration.create_session(ENGINE)


def get_db() -> Generator[Session, None, None]:
    session = SESSION()
    try:
        yield session
    except Exception as exc:
        logger.error("Rollback SQL")
        session.rollback()
        raise exc
    finally:
        session.close()
