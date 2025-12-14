import streamlit as st
import asyncio

from backend.utilities.general import run_async
from backend.data.super_class import SupermarketChain


async def my_async():
    await asyncio.sleep(2)
    return "Async operation complete!"


def render():
    st.title("Welcome to the Home Page")
    st.write("This is the main landing page of the application.")
    # result = run_async(my_async())
    st.write(SupermarketChain.registry)


if __name__ == "__main__":
    render()