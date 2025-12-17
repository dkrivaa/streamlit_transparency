import subprocess
subprocess.run(["playwright", "install", "chromium"], check=True)

import streamlit as st

from backend.data.super_class import SupermarketChain
# from backend.data.binaprojects import BinaProjects
# from backend.data.carrefour import Carrefour
# from backend.data.hazihinam import HaziHinam
# from backend.data.laibcatalog import LaibCatalog
from backend.data.publishedprices import PublishedPrices
from backend.data.shufersal import Shufersal


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

db_page = st.Page(
    title='Database',
    page='ui/views/db.py',
)


pages = [home_page, check_price_page, shopping_list_page, db_page]
pg = st.navigation(pages=pages, position='top')

pg.run()