import streamlit as st
import asyncio


async def my_async():
    await asyncio.sleep(2)
    return "Async operation complete!"


def render():
    st.title("Welcome to the Home Page")
    st.write("This is the main landing page of the application.")
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    result = loop.run_until_complete(my_async())
    st.write(result)


if __name__ == "__main__":
    render()