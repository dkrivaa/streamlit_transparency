import streamlit as st

from backend.utilities.general import run_async
from backend.database.db import create_db


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


if __name__ == "__main__":
    render()