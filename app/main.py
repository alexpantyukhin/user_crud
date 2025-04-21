from litestar import Litestar
from litestar.openapi.config import OpenAPIConfig
from app.controllers.user_controller import UserController
from config import DATABASE_URL
from litestar.logging import LoggingConfig


from litestar.plugins.sqlalchemy import (
    AsyncSessionConfig,
    SQLAlchemyAsyncConfig,
    SQLAlchemyPlugin,
)


session_config = AsyncSessionConfig(expire_on_commit=False)
sqlalchemy_config = SQLAlchemyAsyncConfig(
    connection_string=DATABASE_URL,
    before_send_handler="autocommit",
    session_config=session_config,
    create_all=False,
)
alchemy = SQLAlchemyPlugin(config=sqlalchemy_config)

openapi_config = OpenAPIConfig(
    title="Users API",
    version="1.0.0",
    description="API for users creation and management",
)


logging_config = LoggingConfig(
    root={"level": "INFO", "handlers": ["queue_listener"]},
    formatters={
        "standard": {"format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"}
    },
    log_exceptions="always",
)

logger = logging_config.configure()()



app = Litestar(
    route_handlers=[UserController],
    openapi_config=openapi_config,
    plugins=[alchemy],
    logging_config=logging_config)

if __name__ == "__main__":
    app.run()
