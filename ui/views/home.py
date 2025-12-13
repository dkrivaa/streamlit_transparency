import streamlit as st
import asyncio


async def my_async():
    return asyncio.run(asyncio.sleep(1, result="Async Result"))


def render():
    st.title("Welcome to the Home Page")
    st.write("This is the main landing page of the application.")
    asyncio.run(my_async())


if __name__ == "__main__":
    render()