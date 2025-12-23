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
    icon=":material/attach_money:",
)

check_price_page2 = st.Page(
    title='Check Price',
    page='ui/views/check_price_2.py',
    icon=":material/attach_money:",
)

plan_shopping_page1 = st.Page(
    title='Plan Shopping',
    page='ui/views/plan_shopping_1.py',
    icon=":material/list:",
)

plan_shopping_page2 = st.Page(
    title='Plan Shopping',
    page='ui/views/plan_shopping_2.py',
    icon=":material/list:",
)

db_page = st.Page(
    title='Database',
    page='ui/views/db.py',
    icon=":material/data_table:",
)

pages = [home_page, check_price_page1, check_price_page2, plan_shopping_page1, plan_shopping_page2,
         db_page]
menu_pages = [home_page, ]
pg = st.navigation(pages=pages, position='hidden')

# Create custom navigation with columns
with st.container(border=True):
    cols = st.columns(len(menu_pages))
    for col, page in zip(cols, menu_pages):
        with col:
            st.page_link(page, label=page.title, icon=page.icon)


pg.run()
