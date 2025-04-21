from app.models.user import User

from advanced_alchemy.extensions.litestar import (
    repository,
    service,
)

class UserService(service.SQLAlchemyAsyncRepositoryService[User]):

    class UserRepo(repository.SQLAlchemyAsyncRepository[User]):
        model_type = User

    repository_type = UserRepo
