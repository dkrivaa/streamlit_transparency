import streamlit as st

import asyncpg
import asyncio

from backend.utilities.general import run_async
from backend.database.db import create_db
from backend.database.utilities import update_stores_db

from backend.data.super_class import SupermarketChain


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
            run_async(create_db, key='result')
        if 'result' in st.session_state:
            st.success(st.session_state.result)

    if st.button("Update Database"):
        with st.spinner("Updating database..."):
            run_async(update_stores_db)
        st.success("Database updated successfully.")


if __name__ == "__main__":
    render()