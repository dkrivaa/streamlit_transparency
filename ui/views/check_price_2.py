import streamlit as st

from backend.utilities.general import run_async
from backend.utilities.url_to_dict import data_dict
from backend.utilities.fresh_data_funcs import fresh_price_data, fresh_promo_data
from backend.data.super_class import SupermarketChain
from ui.views.common_elements import price_element, promo_element


def render():
    """" The main function to render the check price page 2 """
    st.title("Check Product Price")
    st.divider()
    # Retrieve chain and store from session state
    my_chain = st.session_state.get('chain', None)
    alias = my_chain.alias if my_chain else None
    my_store = st.session_state.get('store', None)
    # Fetch fresh data for the selected chain and store
    try:
        # Get fresh price and promo data
        price_data = fresh_price_data(alias=alias, store_code=my_store) if alias and my_store else None
        promo_data = fresh_promo_data(alias=alias, store_code=my_store) if alias and my_store else None
    except TypeError as e:
        # Catch if data is getting updated on servers
        price_data = None
        promo_data = None
        st.error('The selected supermarket chain is currently updating the data. '
                 'Please try again in a few minutes.')

    if price_data:
        st.success('Your Data is Ready!')

        with st.container(border=True):
            st.subheader("Product Details")
            # Get item details for a barcode
            item = st.selectbox(
                label='Select Barcode',
                label_visibility='hidden',
                options = sorted([d['ItemCode'] for d in price_data], key=int),
                format_func=lambda x: (
                    f"{x} - "
                    f"{next(
                        d.get('ItemName') or d.get('ItemNm')
                        for d in price_data
                        if d.get('ItemCode') == x
                    )}"
                ),
                index=None,
                placeholder="Select Product Barcode",
            )

            # Continue only if an item is selected
            if item:
                # Get price details for item from price data
                item_details = my_chain.get_shopping_prices(price_data=price_data,
                                                            shoppinglist=[item]) if price_data else None
                # Get relevant promo blacklist for the chain
                blacklist = my_chain.promo_blacklist() if my_chain else set()
                # Get promo details for item from promo data
                item_promos = my_chain.get_shopping_promos(promo_data=promo_data, shoppinglist=[item],
                                                           blacklist=blacklist) if promo_data else None
                # Show price
                price_element(item, item_details)

                # Show promotions
                if item_promos:
                    st.subheader('Promotions')
                    if item_promos and item_promos.get(item):
                        for promo in item_promos[item]:
                            promo_element(promo)
                    else:
                        st.info("No promotions available for this product at the moment.")

    else:
        st.warning("No data available for the selected chain and store. Please go back and select again.")


if __name__ == "__main__":
    render()

