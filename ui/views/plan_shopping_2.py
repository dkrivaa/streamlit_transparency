import streamlit as st

from backend.utilities.general import run_async
from backend.utilities.fresh_data_funcs import fresh_price_data, fresh_promo_data
from backend.data.super_class import SupermarketChain
from backend.database.utilities import get_stores_for_chain


def render():
    """ The main function to render the shopping planning page """

    with st.container():
        st.title('Plan Shopping')
        st.subheader('Make Shopping List')
        st.divider()

        st.write(st.session_state)

        #
        # my_chain = st.session_state.get('chain1', None)
        # alias = my_chain.alias if my_chain else None
        # my_store = st.session_state.get('store', None)
        # # Fetch fresh data for the selected chain and store
        # try:
        #     # Get fresh price and promo data
        #     price_data = fresh_price_data(alias=alias, store_code=my_store) if alias and my_store else None
        #     promo_data = fresh_promo_data(alias=alias, store_code=my_store) if alias and my_store else None
        # except TypeError as e:
        #     # Catch if data is getting updated on servers
        #     price_data = None
        #     promo_data = None
        #     st.error('The selected supermarket chain is currently updating the data. '
        #              'Please try again in a few minutes.')



if __name__ == "__main__":
    render()