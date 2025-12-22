import streamlit as st

from backend.utilities.general import run_async
from backend.utilities.url_to_dict import data_dict
from backend.data.super_class import SupermarketChain


def render():
    """ The main function to render the shopping list page 1 """
    with st.container():
        st.title('Make Shopping List')
        st.subheader(' Choose up to 3 supermarket chains')

        with st.container(border=True):
            st.subheader('Supermarket Chain 1:')
            chain1 = st.selectbox(
                label="Select Supermarket Chain 1",
                label_visibility='hidden',
                options=sorted(SupermarketChain.registry, key=lambda x: x.alias),
                format_func=lambda x: x.alias.capitalize(),
                index=None,
                key='chain1',
                placeholder="Select Supermarket Chain",
            )
        chain2 = st.selectbox(
            label="Select Supermarket Chain 2",
            label_visibility='hidden',
            options=sorted(SupermarketChain.registry, key=lambda x: x.alias),
            format_func=lambda x: x.alias.capitalize(),
            index=None,
            key='chain2',
            placeholder="Select Supermarket Chain",
        )
        chain3 = st.selectbox(
            label="Select Supermarket Chain 3",
            label_visibility='hidden',
            options=sorted(SupermarketChain.registry, key=lambda x: x.alias),
            format_func=lambda x: x.alias.capitalize(),
            index=None,
            key='chain3',
            placeholder="Select Supermarket Chain",
        )