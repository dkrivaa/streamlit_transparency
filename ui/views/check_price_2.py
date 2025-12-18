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

    st.write(price_dict)


if __name__ == "__main__":
    render()

