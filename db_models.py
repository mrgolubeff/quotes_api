from typing import Optional
from sqlalchemy import String
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


class Base(DeclarativeBase):
    pass


class Quote(Base):
    __tablename__ = 'quote'

    id: Mapped[int] = mapped_column(primary_key=True)
    author: Mapped[str] = mapped_column(String(40))
    content: Mapped[str] = mapped_column(String(300))

    def __repr__(self) -> str:
        representaion = f'Quote(id={self.id}, author={self.author}, '
        + f'content={self.content[:30]})'
        return representaion


if __name__ == '__main__':
    engine = create_engine("sqlite://", echo=True)
    Base.metadata.create_all(engine)
