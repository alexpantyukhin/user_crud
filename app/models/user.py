from sqlalchemy import Column, BigInteger, String, TIMESTAMP, func
from advanced_alchemy.extensions.litestar import (
    base
)

class BaseModel(base.BigIntBase):
    __abstract__ = True

    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(TIMESTAMP(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

class User(BaseModel):
    __tablename__ = 'users'

    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    password = Column(String, nullable=False)
