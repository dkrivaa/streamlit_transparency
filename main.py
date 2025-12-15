import subprocess
subprocess.run(["playwright", "install", "chromium"], check=True)

import streamlit as st

from backend.data.super_class import SupermarketChain
from backend.data.shufersal import Shufersal
from backend.data.publishedprices import PublishedPrices

home_page = st.Page(
    title='Home',
    page='ui/views/home.py',
    default=True
)

check_price_page = st.Page(
    title='Check Price',
    page='ui/views/check_price.py',
)

shopping_list_page = st.Page(
    title='Shopping List',
    page='ui/views/shopping_list.py',
)


pages = [home_page, check_price_page, shopping_list_page]
pg = st.navigation(pages=pages, position='top')

pg.run()