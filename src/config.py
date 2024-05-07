from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    Application settings.

    Attributes:
        DB_HOST (str | None): The hostname of the PostgreSQL server.
        DB_PORT (int | None): The port of the PostgreSQL server.
        DB_USER (str | None): The username to authenticate with the PostgreSQL server.
        DB_PASSWORD (str | None): The password to authenticate with the PostgreSQL server.
        DB_NAME (str | None): The name of the PostgreSQL database.
        DATABASE_URL (str | None): The URL of the PostgreSQL database.
    """

    DB_HOST: str | None = None
    DB_PORT: int | None = None
    DB_USER: str | None = None
    DB_PASSWORD: str | None = None
    DB_NAME: str | None = None
    DATABASE_URL: str | None = None

    class Config:
        """
        Configuration for environment variables.

        Attributes:
            env_file (str): The path to the environment file.
            env_file_encoding (str): The encoding of the environment file.
        """

        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
# FIXME Нужно задать динамическое значение DATABASE_URL
# в классе через pydantic(BaseSettings))
settings.DATABASE_URL = f"postgresql+asyncpg://{settings.DB_USER}:{settings.DB_PASSWORD}@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}"
