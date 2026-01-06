import streamlit as st
import asyncio

from backend.utilities.general import run_async
from backend.data.super_class import SupermarketChain
from backend.database.utilities import get_stores_for_chain
from ui.views.common_elements import select_chain_element, select_store_element


def render():
    """ The main function to render the check price page 1 """
    with st.container(border=True):
        st.title("Check Product Price")
        st.subheader("Where are you shopping?")

        # Select Supermarket Chain
        chain = select_chain_element(key='chain_selectbox')

        if chain:
            # Select Store for the selected chain
            store = select_store_element(chain=chain, key='store_selectbox')

            # Save selections to session state and continue
            if store:
                st.session_state.chain = chain
                st.session_state.alias = chain.alias
                st.session_state.store = store

                if st.button('Continue'):
                    st.switch_page('ui/views/check_price_2.py')


if __name__ == "__main__":
    render()
