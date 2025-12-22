import streamlit as st

from backend.utilities.general import run_async
from backend.data.super_class import SupermarketChain
from backend.database.utilities import get_stores_for_chain


def render():
    """ The main function to render the shopping list page 1 """
    with st.container():
        st.title('Make Shopping List')
        st.subheader('Choose up to 3 supermarket chains')

        for chain_num in range(1, 4):  # 1, 2, 3
            chain_key = f'chain{chain_num}'
            store_key = f'store{chain_num}'

            with st.container(border=True):
                st.subheader(f'Supermarket Chain {chain_num}:')

                chain = st.selectbox(
                    label=f"Select Supermarket Chain {chain_num}",
                    label_visibility='hidden',
                    options=sorted(SupermarketChain.registry, key=lambda x: x.alias),
                    format_func=lambda x: x.alias.capitalize(),
                    index=None,
                    key=chain_key,
                    placeholder="Select Supermarket Chain",
                )

                if chain:
                    store_objects = run_async(get_stores_for_chain, chain=chain)
                    store_options = {store.store_code: store.store_name for store in store_objects}

                    store = st.selectbox(
                        label="Select Store",
                        label_visibility='hidden',
                        options=sorted(list(store_options.keys()), key=int),
                        format_func=lambda x: f'{x} - {store_options[x]}',
                        index=None,
                        key=store_key,
                        placeholder="Select Supermarket Store",
                    )

                    if store:
                        st.session_state[chain_key] = chain
                        st.session_state[f'alias{chain_num}'] = chain.alias
                        st.session_state[store_key] = store


if __name__ == "__main__":
    render()