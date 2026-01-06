import streamlit as st
import asyncio

from backend.utilities.general import run_async
from backend.data.super_class import SupermarketChain
from backend.database.utilities import get_stores_for_chain


def sort_classes_by_alias(classes: list[type]) -> list[type]:
    """
    Helper function for select_chain_element function.
    Sorts the given list of classes by their alias attribute """
    return sorted(classes, key=lambda x: x.alias)


def select_chain_element(key: str) -> SupermarketChain:
    """
    Renders the supermarket chain selection element.
    Args:
        key (str): The unique key for this selectbox element.
    """
    # Select Supermarket Chain
    chain = st.selectbox(
        label="Select Supermarket Chain",
        label_visibility='hidden',
        options=sort_classes_by_alias(SupermarketChain.registry),
        format_func=lambda x: x.alias.capitalize(),
        index=None,
        placeholder="Select Supermarket Chain",
        key=key
    )

    return chain


def select_store_element(chain: SupermarketChain, key: str) -> str:
    """
    Renders the store selection element for the given supermarket chain.
    Args:
        chain (SupermarketChain): The selected supermarket chain.
        key (str): The unique key for this selectbox element.
    """
    store_objects = run_async(get_stores_for_chain, chain=chain)
    store_options = {store.store_code: store.store_name for store in store_objects}

    store = st.selectbox(
        label="Select Store",
        label_visibility='hidden',
        options=sorted(list(store_options.keys()), key=int),
        format_func=lambda x: f'{x} - {store_options[x]}',
        index=None,
        placeholder="Select Supermarket Store",
        key=key
    )

    return store

