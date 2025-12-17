from sqlalchemy.ext.asyncio import (
    AsyncSession,
    create_async_engine,
    async_sessionmaker,
)
from sqlalchemy.dialects.sqlite import insert as sqlite_insert
import asyncio

from backend.database.models import Base, Store


from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
DATABASE_URL = f"sqlite+aiosqlite:///{BASE_DIR / 'supermarket.db'}"


async def get_engine(database_url: str = DATABASE_URL):
    """ Create and return an asynchronous SQLAlchemy engine. """
    engine = create_async_engine(database_url, echo=True)
    return engine


async def get_session(engine) -> AsyncSession:
    """ Create and return an asynchronous SQLAlchemy session. """
    async_session = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
    return async_session()


# --- Function to create database ---
async def create_db():
    engine = await get_engine()
    async with engine.begin() as conn:
        # Use run_sync to call synchronous create_all in async context
        await conn.run_sync(Base.metadata.create_all)
    await engine.dispose()
    print("✅ Database and tables created successfully!")


async def insert_new_stores(stores_data_list: list[dict]):
    """
    Insert new stores into the database, ignoring duplicates based on chain_code and store_code.
    Params:
        stores_data_list - list of dicts of stores data for some chain
    """
    engine = await get_engine()
    async with await get_session(engine) as session:
        stmt = sqlite_insert(Store).values(stores_data_list)
        stmt = stmt.on_conflict_do_nothing(index_elements=["chain_code", "store_code"])
        await session.execute(stmt)
        await session.commit()
