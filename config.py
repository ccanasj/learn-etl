from sqlalchemy.engine import URL
from os import environ


SQLALCHEMY_DATABASE_URL = URL.create(
    drivername="postgresql",
    password=environ["POSTGRESQL_PASSWORD"],
    username=environ["POSTGRESQL_USER"],
    host=environ["POSTGRESQL_HOST"],
    port=environ["POSTGRESQL_PORT"],
    database=environ["POSTGRESQL_DATABASE"],
)
