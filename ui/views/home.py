import streamlit as st
import asyncio

from backend.utilities.general import run_async
from backend.data.super_class import SupermarketChain
from backend.data.shufersal import Shufersal
from backend.data.publishedprices import RamiLevi
from backend.utilities.general import get_chain_class_by_alias


def render():
    """ The main function to render the home page """
    st.title("CLARITY")
    st.subheader('Supermarket Price Transparency')
    st.image('https://images.unsplash.com/photo-1677751177812-eef0b47b888d?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NHx8Z3JvY2VyeSUyMHByaWNlc3xlbnwwfHwwfHx8MA%3D%3D',
             width=100)


    chain_alias = 'ramilevi'
    chain = get_chain_class_by_alias(chain_alias)
    st.write(f"Loaded chain: {chain.name} ({chain.alias})")
    stores = run_async(chain.prices, store_code=1)
    st.write(stores)


if __name__ == "__main__":
    render()