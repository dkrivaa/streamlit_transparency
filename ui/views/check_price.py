import streamlit as st
import asyncio

from backend.utilities.general import run_async
from backend.data.super_class import SupermarketChain
from backend.utilities.general import get_chain_class_by_alias


def render():
    """ The main function to render the check price page """
    st.title("Check Product Price")
    st.divider()

    with st.container(border=True):
        st.subheader("Where are you shopping?")
        chain = st.selectbox(
            "Select Supermarket Chain",
            options=sorted([cls.alias.capitalize() for cls in SupermarketChain.registry]),
        )

    # chain_alias = 'ramilevi'
    # chain = get_chain_class_by_alias(chain_alias)
    # st.write(f"Loaded chain: {chain.name} ({chain.alias})")
    # stores = run_async(chain.prices, store_code=1)
    # st.write(stores)


if __name__ == "__main__":
    render()
