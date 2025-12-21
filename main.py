import subprocess
subprocess.run(["playwright", "install", "chromium"], check=True)

import streamlit as st

from backend.data.super_class import SupermarketChain
from backend.data.binaprojects import BinaProjects
from backend.data.carrefour import CarrefourParent
# from backend.data.hazihinam import HaziHinam
# from backend.data.laibcatalog import LaibCatalog
from backend.data.publishedprices import PublishedPrices
from backend.data.shufersal import Shufersal


home_page = st.Page(
    title='Home',
    page='ui/views/home.py',
    default=True
)

check_price_page1 = st.Page(
    title='Check Price',
    page='ui/views/check_price_1.py',
)

check_price_page2 = st.Page(
    title='Check Price',
    page='ui/views/check_price_2.py',
)

shopping_list_page = st.Page(
    title='Shopping List',
    page='ui/views/shopping_list.py',
)

db_page = st.Page(
    title='Database',
    page='ui/views/db.py',
)

pages = [home_page, check_price_page1, check_price_page2, shopping_list_page, db_page]
menu_pages = [home_page, check_price_page1, shopping_list_page, ]
pg = st.navigation(pages=pages, position='hidden')

pg.run()

""" Simple navigator function for Streamlit apps """
nav = st.pills(
                label='navigator',
                label_visibility='hidden',
                options=[st.page_link[page]["title"] for page in menu_pages],
            )
