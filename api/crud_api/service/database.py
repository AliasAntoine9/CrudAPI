from pathlib import Path

from sqlalchemy import text
from sqlalchemy.orm import Session

from crud_api import logger


def initialization(db: Session) -> None:
    with open(Path(__file__).parent.parent / "create_database/sql") as file:
        create_database_query = file.read()

    with open(Path(__file__).parent.parent / "feed_database/sql") as file:
        feed_database_query = file.read()

    try:
        db.execute(text(create_database_query))
        db.execute(text(feed_database_query))
    except Exception as exc:
        logger.error("A problem occurs while initializing the Database")
        raise exc
