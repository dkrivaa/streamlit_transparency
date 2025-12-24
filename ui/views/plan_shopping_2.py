import streamlit as st

from backend.utilities.general import run_async
from backend.utilities.fresh_data_funcs import fresh_price_data, fresh_promo_data
from backend.data.super_class import SupermarketChain
from backend.database.utilities import get_stores_for_chain


def shoppinglist_element(price_data: dict):
    """ Renders the shopping list element """
    with st.form('shoppinglist form', clear_on_submit=True):
        item = st.selectbox(
            label='Select Barcode',
            label_visibility='hidden',
            options=sorted([d['ItemCode'] for d in price_data], key=int),
            format_func=lambda x: (
                f"{x} - "
                f"{next(
                    d.get('ItemPrice')
                    for d in price_data
                    if d.get('ItemCode') == x
                )} ₪ - "
                f"{next(
                    d.get('ItemName') or d.get('ItemNm')
                    for d in price_data
                    if d.get('ItemCode') == x
                )}"
            ),
            index=None,
            placeholder="Add Product to Shopping List",
        )

        if item:
            quantity = st.number_input(
                            label='Quantity (units, kg, etc.)',
                            label_visibility='hidden',
                            min_value=0,
                            value=1,
                            step=1,
                            format="%0.1f",
                            placeholder='Enter Quantity (units, kg, etc.)'
                        )

        submitted = st.form_submit_button('Add to Shopping List')
        if submitted and item:
            st.session_state.shoppinglist.append(item)
            st.success(f'Added {item} to shopping list!')


def render():
    """ The main function to render the shopping planning page """

    with st.container():
        st.title('Plan Shopping')
        st.subheader('Make Shopping List')
        st.divider()

        if 'shoppinglist' not in st.session_state:
            st.session_state['shoppinglist'] = []

        st.write(st.session_state)

        # Fetch fresh data for the first selected chain and store
        my_chain = st.session_state.get('chain1', None)
        alias = my_chain.alias if my_chain else None
        my_store = st.session_state.get('store1', None)

        try:
            # Get fresh price and promo data
            price_data1 = fresh_price_data(alias=alias, store_code=my_store) if alias and my_store else None
            promo_data1 = fresh_promo_data(alias=alias, store_code=my_store) if alias and my_store else None
        except TypeError as e:
            # Catch if data is getting updated on servers
            price_data1 = None
            promo_data1 = None
            st.error('The selected supermarket chain is currently updating the data. '
                     'Please try again in a few minutes.')

        if price_data1:
            shoppinglist_element(price_data=price_data1)

            st.write(st.session_state.shoppinglist)

            if st.button('Continue to Price Comparison'):
                st.switch_page('ui/views/plan_shopping_3.py')


if __name__ == "__main__":
    render()