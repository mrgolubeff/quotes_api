from typing import Optional
from sqlalchemy import String
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from pathlib import Path

from config_reader import load_config

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
    data_folder = Path('ini_source')
    file_to_open = data_folder / 'app.ini'
    config = load_config(file_to_open)

    user = config.db_connect.user
    password = config.db_connect.password
    ip = config.db_connect.ip
    port = config.db_connect.port

    engine = create_engine(
        f"postgresql+pg8000://{user}:{password}@{ip}:{port}/oridia",
        echo=True
    )
    Base.metadata.create_all(engine)
