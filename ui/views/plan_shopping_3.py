import streamlit as st

from backend.utilities.general import run_async
from backend.utilities.fresh_data_funcs import fresh_price_data, fresh_promo_data
from backend.data.super_class import SupermarketChain
from backend.database.utilities import get_stores_for_chain


def data():
    """ Fetches data for shopping list from the selected stores """
    chains = [chain for chain in list(st.session_state.keys()) if chain.startswith('chain')]
    # Dict to hold items data per chain
    items = {}
    # Fetch data for each selected store
    for num in range(len(chains)):
        chain_key = f'chain{num + 1}'
        alias_key = f'alias{num + 1}'
        store_key = f'store{num + 1}'

        my_chain = st.session_state.get(chain_key, None)
        alias = st.session_state.get(alias_key, None)
        my_store = st.session_state.get(store_key, None)

        try:
            # Get fresh price and promo data
            price_data = fresh_price_data(alias=alias, store_code=my_store) if alias and my_store else None
            # promo_data = fresh_promo_data(alias=alias, store_code=my_store) if alias and my_store else None
        except TypeError as e:
            # Catch if data is getting updated on servers
            price_data = None
            # promo_data = None

        # Make list of item barcodes in st.session_state shopping list
        shopping_list_barcodes = [item['item'] for item in st.session_state.get('shoppinglist', [])]
        # Get item data for items in shopping list
        data = [d for d in price_data if
                d['ItemCode'] in shopping_list_barcodes] if price_data else []
        items[f'{st.session_state.get(alias_key)}-{st.session_state.get(store_key)}'] = data
    #
    return items


def render():
    """ The main function to render the shopping planning page 3 """

    with st.container():
        st.subheader('Plan Shopping - Step 3')
        st.write('Review your shopping list and compare prices across selected supermarket chains.')
        st.divider()

        st.write(st.session_state)

        items_data = data()

        st.write(items_data)




if __name__ == "__main__":
    render()