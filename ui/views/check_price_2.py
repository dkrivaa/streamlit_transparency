import streamlit as st

from backend.utilities.general import run_async
from backend.utilities.url_to_dict import data_dict
from backend.data.super_class import SupermarketChain


@st.cache_data(ttl=1200)
def fresh_data(alias: str, store_code: str | int) -> dict | None:
    """ Fetch fresh data for the given chain and store code """
    # Get the supermarket chain class from its alias
    chain = next((c for c in SupermarketChain.registry if c.alias == alias), None)
    # Get the latest price URLs for the given chain and store code
    urls = run_async(chain.prices, store_code=store_code) if chain and store_code else None
    # Use pricefull URL and cookies if available
    url = urls.get('pricefull', None) if urls else None
    cookies = urls.get('cookies', None) if urls else None
    # Make data dict from data in pricefull URL
    price_dict = run_async(data_dict, url=url, cookies=cookies) if url else None
    # Clean data dict to only include dicts of items
    price_data = run_async(chain.get_price_data, price_data=price_dict) if price_dict else None
    return price_data


def render():
    """" The main function to render the check price page 2 """
    st.title("Check Product Price")
    st.divider()
    # Retrieve chain and store from session state
    my_chain = st.session_state.get('chain', None)
    alias = my_chain.alias if my_chain else None
    my_store = st.session_state.get('store', None)
    # Fetch fresh data for the selected chain and store
    price_data = fresh_data(alias=alias, store_code=my_store) if alias and my_store else None

    st.write(price_data)

    if price_data:
        st.write('Your Data is Ready!')

        with st.container(border=True):
            st.subheader("Product Details")
            # Get item details for a sample barcode
            item = st.selectbox(
                label='Select Barcode',
                label_visibility='hidden',
                options = sorted([d['ItemCode'] for d in price_data], key=int),
                format_func=lambda x: f'{x} - {[d['ItemName'] for d in price_data if d["ItemCode"] == x][0]}',
                index=None,
                placeholder="Select Product Barcode",
            )

            item_details = run_async(my_chain.get_shopping_prices, price_data=price_data,
                                     shoppinglist=[item]) if price_data else None
            st.write(item_details)

    else:
        st.warning("No data available for the selected chain and store. Please go back and select again.")


if __name__ == "__main__":
    render()

