import streamlit as st
import asyncio

from backend.utilities.general import run_async
from backend.data.super_class import SupermarketChain
from backend.database.utilities import get_stores_for_chain


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

        if chain:
            store_objects = run_async(get_stores_for_chain, chain=chain)
            store_options = {store.store_code: store.store_name for store in store_objects}
            store = st.selectbox(
                label="Select Store",
                label_visibility='hidden',
                options=sorted(list(store_options.keys()), key=int),
                format_func=lambda x: f'{x} - {store_options[x]}',
                index=None,
                placeholder="Select Supermarket Store",
            )

            st.write(store)



if __name__ == "__main__":
    render()
