import os

from dotenv import load_dotenv

load_dotenv(".env")

DB_HOST = os.getenv("DB_HOST") or "localhost"
DB_PORT = os.getenv("DB_PORT") or 5432
DB_USER = os.getenv("DB_USER") or "postgres"
DB_PASSWORD = os.getenv("DB_PASSWORD") or "postgres"
DB_NAME = os.getenv("DB_NAME") or "postgres"
