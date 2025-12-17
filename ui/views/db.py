import streamlit as st

import asyncpg
import asyncio

from backend.utilities.general import run_async
from backend.database.db import create_db


async def test_asyncpg():
    conn = await asyncpg.connect(
        user="postgres",
        password=st.secrets["DB_PASSWORD"],
        host=st.secrets["DB_HOST"],   # e.g. xyz.supabase.co
        database="postgres",
        port=5432,
        ssl="require"
    )
    val = await conn.fetchval("SELECT 1")
    await conn.close()
    return val



def render():
    """ UI function to create the database and tables """
    st.header("Create Database")
    st.write(
        """
        Click the button below to create the database and its tables.
        This action only needs to be performed once during the initial setup.
        """
    )

    if st.button("Create Database"):
        with st.spinner("Creating database..."):
            run_async(create_db)
        st.success("✅ Database and tables created successfully!")

    if st.button("Test asyncpg"):
        try:
            result = run_async(test_asyncpg)
            st.success(f"Connected! Result = {result}")
        except Exception as e:
            st.error(str(e))


if __name__ == "__main__":
    render()