import streamlit as st

from backend.utilities.general import run_async
from backend.data.super_class import SupermarketChain
from backend.database.utilities import get_stores_for_chain


def chain_selection_element():
    """ Renders the supermarket chain selection element """
    for chain_num in range(1, 4):  # 1, 2, 3
        chain_key = f'chain{chain_num}'
        store_key = f'store{chain_num}'

        with st.container(border=True):
            st.write(f'Supermarket Chain {chain_num}:')

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
                    st.session_state[f'alias{chain_num}'] = chain.alias


def render():
    """ The main function to render the shopping planning page 1 """
    # clear cache
    st.cache_data.clear()

    with st.container():
        st.subheader('Plan Shopping')
        st.write('Choose up to 3 supermarket chains to compare prices when planning your shopping.')

        # Render chain selection elements
        chain_selection_element()

        if st.button('Continue'):
            st.switch_page('ui/views/plan_shopping_2.py')


if __name__ == "__main__":
    render()