import streamlit as st

from backend.utilities.general import run_async
from backend.data.super_class import SupermarketChain
from backend.database.utilities import get_stores_for_chain


def render():
    """ The main function to render the shopping planning page """

    with st.container():
        st.title('Plan Shopping')
        st.subheader('Make Shopping List')
        st.divider()



if __name__ == "__main__":
    render()