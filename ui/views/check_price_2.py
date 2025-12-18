import streamlit as st

from backend.utilities.general import run_async
from backend.utilities.url_to_dict import data_dict


def render():
    """" The main function to render the check price page 2 """
    st.title("Check Product Price")
    st.divider()

    my_chain = st.session_state.get('chain', None)
    my_store = st.session_state.get('store', None)
    urls = run_async(my_chain.prices, store_code=my_store) if my_chain and my_store else None

    url = urls.get('pricefull', None) if urls else None
    cookies = urls.get('cookies', None) if urls else None

    price_dict = run_async(data_dict, url=url, cookies=cookies) if url else None
    price_data = run_async(my_chain.get_price_data, price_data=price_dict) if price_dict else None
    item_details = run_async(my_chain.get_shopping_prices, price_data=price_data, shopping_list=[7290000072753]) if price_data else None


    st.write(item_details)


if __name__ == "__main__":
    render()

