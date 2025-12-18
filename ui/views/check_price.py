import streamlit as st
import asyncio

from backend.utilities.general import run_async
from backend.data.super_class import SupermarketChain
from backend.utilities.general import get_chain_class_by_alias


def sort_classes_by_alias(classes: list[type]) -> list[type]:
    """ Sorts the given list of classes by their alias attribute """
    return sorted(classes, key=lambda x: x.alias)


def render():
    """ The main function to render the check price page """
    st.title("Check Product Price")
    st.divider()

    with st.container(border=True):
        st.subheader("Where are you shopping?")
        chain = st.selectbox(
            label="Select Supermarket Chain",
            label_visibility='hidden',
            options=sort_classes_by_alias(SupermarketChain.registry),
            format_func=lambda x: x.alias.capitalize(),
            index=None,
            placeholder="Select Supermarket Chain",
        )

    chain = get_chain_class_by_alias(chain_alias)
    st.write(f"Loaded chain: {chain.name} ({chain.alias})")
    # stores = run_async(chain.prices, store_code=1)
    # st.write(stores)


if __name__ == "__main__":
    render()
