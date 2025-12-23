import streamlit as st

from backend.utilities.general import run_async
from backend.utilities.fresh_data_funcs import fresh_price_data, fresh_promo_data
from backend.data.super_class import SupermarketChain
from backend.database.utilities import get_stores_for_chain


def render():
    """ The main function to render the shopping planning page 3 """

    with st.container():
        st.subheader('Plan Shopping - Step 3')
        st.write('Review your shopping list and compare prices across selected supermarket chains.')
        st.divider()

        st.write(st.session_state)

        chains = [chain for chain in list(st.session_state.keys()) if chain.startswith('chain')]

        st.write(chains)


if __name__ == "__main__":
    render()