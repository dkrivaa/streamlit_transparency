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
    icon=":material/home:",
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

# Create custom navigation with columns
with st.container(border=True):
    cols = st.columns(len(menu_pages))
    for col, page in zip(cols, menu_pages):
        with col:
            st.page_link(page, label=page.title, icon=page.icon)


pg.run()
