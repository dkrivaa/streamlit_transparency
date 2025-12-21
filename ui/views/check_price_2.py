import streamlit as st

from backend.utilities.general import run_async
from backend.utilities.url_to_dict import data_dict
from backend.data.super_class import SupermarketChain


@st.cache_data(ttl=1200)
def fresh_price_data(alias: str, store_code: str | int) -> dict | None:
    """ Fetch fresh data for the given chain and store code """
    # Get the supermarket chain class from its alias
    chain = next((c for c in SupermarketChain.registry if c.alias == alias), None)
    # Get the latest price URLs for the given chain and store code
    urls = run_async(chain.prices, store_code=store_code) if chain and store_code else None
    # Use pricefull URL and cookies if available
    url = urls.get('pricefull') or urls.get('PriceFull') if urls else None
    cookies = urls.get('cookies', None) if urls else None
    # Make data dict from data in pricefull URL
    price_dict = run_async(data_dict, url=url, cookies=cookies) if url else None
    # Clean data dict to only include dicts of items
    price_data = chain.get_price_data(price_data=price_dict) if price_dict else None
    return price_data


@st.cache_data(ttl=1200)
def fresh_promo_data(alias: str, store_code: str | int) -> dict | None:
    """ Fetch fresh data for the given chain and store code """
    # Get the supermarket chain class from its alias
    chain = next((c for c in SupermarketChain.registry if c.alias == alias), None)
    # Get the latest price URLs for the given chain and store code
    urls = run_async(chain.prices, store_code=store_code) if chain and store_code else None
    # Use promofull URL and cookies if available
    url = urls.get('promofull') or urls.get('PromoFull') if urls else None
    cookies = urls.get('cookies', None) if urls else None
    # Make data dict from data in pricefull URL
    promo_dict = run_async(data_dict, url=url, cookies=cookies) if url else None
    # Clean data dict to only include dicts of items
    promo_data = chain.get_promo_data(promo_data=promo_dict) if promo_dict else None
    return promo_data


def promo_element(promo: dict):
    """ Renders a single promo element """
    if promo.get('RewardType') == 1:
         return promo_element_1(promo)


def promo_element_1(promo: dict):
    """ Renders a single promo element with reward type 1"""
    st.markdown(f"**{promo.get('PromoDesc', 'N/A')}**")
    st.metric(
        label="Promotion Price",
        value=f"{promo.get('PromoPrice')} NIS",
    )
    st.write(f"- Valid Until: {promo.get('EndDate', 'N/A')}")
    st.divider()


def render():
    """" The main function to render the check price page 2 """
    st.title("Check Product Price")
    st.divider()
    # Retrieve chain and store from session state
    my_chain = st.session_state.get('chain', None)
    alias = my_chain.alias if my_chain else None
    my_store = st.session_state.get('store', None)
    # Fetch fresh data for the selected chain and store
    price_data = fresh_price_data(alias=alias, store_code=my_store) if alias and my_store else None
    promo_data = fresh_promo_data(alias=alias, store_code=my_store) if alias and my_store else None

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

            # Get price details for item from price data
            item_details = my_chain.get_shopping_prices(price_data=price_data,
                                                        shoppinglist=[item]) if price_data else None
            # Get relevant promo blacklist for the chain
            blacklist = my_chain.promo_blacklist() if my_chain else set()
            # Get promo details for item from promo data
            item_promos = my_chain.get_shopping_promos(promo_data=promo_data, shoppinglist=[item],
                                                       blacklist=blacklist) if promo_data else None
            # st.write(item_details)
            # Present results - price
            st.subheader('Price')
            st.metric(
                label=f"{item} - {
                    (
                        item_details.get(item, {}).get("ItemName")
                        or item_details.get(item, {}).get("ItemNm")
                        or "N/A"
                    )
                }",
                label_visibility='collapsed',
                value=(
                    f"{item_details[item]['ItemPrice']} NIS"
                    if item_details and item_details.get(item)
                    else "N/A"
                ),
            )

            st.divider()

            # Show promotions
            st.subheader('Promotions')
            if item_promos and item_promos.get(item):
                for promo in item_promos[item]:
                    promo_element(promo)
            else:
                st.info("No promotions available for this product at the moment.")

            st.write(item_promos)

    else:
        st.warning("No data available for the selected chain and store. Please go back and select again.")


if __name__ == "__main__":
    render()

