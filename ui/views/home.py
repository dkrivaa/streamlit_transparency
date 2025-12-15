import streamlit as st
import asyncio

from backend.utilities.general import run_async
from backend.data.super_class import SupermarketChain
from backend.data.shufersal import Shufersal
from backend.data.publishedprices import RamiLevi
from backend.utilities.general import get_chain_class_by_alias


def render():
    """ The main function to render the home page """
    st.title("CLARITY")
    st.subheader('Supermarket Price Transparency')
    st.divider()

    option_map = {
        0: {'icon': ':material/attach_money:', 'text': 'Check product price', 'page': 'ui/views/check_price.py'},
        1: {'icon': ':material/list:', 'text': 'Compare shopping list prices', 'page': 'ui/views/shopping_list.py'},
    }

    selection = st.pills(
        'Select',
        options=option_map.keys(),
        format_func=lambda option: f'{option_map[option]['icon']} {option_map[option]['text']}',
        selection_mode="single",
        default=None,
        # on_change=lambda: st.switch_page(option_map[selection]['page'])
    )

    if selection is not None:
        st.switch_page(option_map[selection]['page'])





    # chain_alias = 'ramilevi'
    # chain = get_chain_class_by_alias(chain_alias)
    # st.write(f"Loaded chain: {chain.name} ({chain.alias})")
    # stores = run_async(chain.prices, store_code=1)
    # st.write(stores)


if __name__ == "__main__":
    render()