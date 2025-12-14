import streamlit as st
import asyncio

from backend.utilities.general import run_async
from backend.data.super_class import SupermarketChain
from backend.data.shufersal import Shufersal
from backend.data.publishedprices import RamiLevi
from backend.utilities.general import get_chain_class_by_alias


async def my_async():
    await asyncio.sleep(2)
    return "Async operation complete!"


def render():
    st.title("Welcome to the Home Page")
    st.write("This is the main landing page of the application.")
    chain_alias = 'ramilevi'
    chain = get_chain_class_by_alias(chain_alias)
    st.write(f"Loaded chain: {chain.name} ({chain.alias})")
    stores = run_async(chain.prices, store_code=1)
    st.write(stores)


if __name__ == "__main__":
    render()