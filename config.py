import os

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+asyncpg://postgres:postgres@db:5432/users_test_task")
DEBUG = True
SQLALCHEMY_TRACK_MODIFICATIONS = False