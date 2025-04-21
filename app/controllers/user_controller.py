from collections.abc import AsyncGenerator
from uuid import UUID
from litestar import Controller, get, post, delete, patch
from litestar.di import Provide
from litestar.params import Parameter
from app.models.user import User
from app.services.user_service import UserService
from app.schemas.user import UserCreate, UserUpdate, UserResponse
from advanced_alchemy.extensions.litestar import service
from sqlalchemy.ext.asyncio import AsyncSession

async def provide_users_service(db_session: AsyncSession) -> AsyncGenerator[UserService]:
    async with UserService.new(session=db_session) as service:
        yield service

class UserController(Controller):

    path = "/users"
    dependencies = {"users_service": Provide(provide_users_service)}
    tags = ["Users"]


    @get()
    async def list_users(
        self,
        users_service: UserService
    ) -> service.OffsetPagination[UserResponse]:
        results, total = await users_service.list_and_count()
        return users_service.to_schema(results, total, schema_type=UserResponse)

    @post()
    async def create_user(
        self,
        users_service: UserService,
        data: UserCreate
    ) -> UserResponse:
        obj = await users_service.create(data, auto_commit=True)
        return users_service.to_schema(obj, schema_type=UserResponse)

    @get(path="/{user_id:int}")
    async def get_user(
        self,
        users_service: UserService,
        user_id: int = Parameter(
            title="User ID",
            description="The user to retrieve.",
        ),
    ) -> UserResponse:
        obj = await users_service.get(user_id)
        return users_service.to_schema(obj, schema_type=UserResponse)

    @patch(path="/{user_id:int}")
    async def update_user(
        self,
        data: UserUpdate,
        users_service: UserService,
        user_id: int = Parameter(
            title="User ID",
            description="The user to update.",
        ),
    ) -> UserResponse:
        obj = await users_service.update(data, item_id=user_id, auto_commit=True)
        return users_service.to_schema(obj, schema_type=UserResponse)

    @delete(path="/{user_id:int}")
    async def delete_user(
        self,
        users_service: UserService,
        user_id: int = Parameter(
            title="User ID",
            description="The user to delete.",
        ),
    ) -> None:
        await users_service.delete(user_id)
