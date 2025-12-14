import subprocess
subprocess.run(["playwright", "install", "chromium", "--with-deps"], check=True)

import streamlit as st

from backend.data.super_class import SupermarketChain
from backend.data.shufersal import Shufersal

home_page = st.Page(
    title='Home',
    page='ui/views/home.py',
    default=True
)


pages = [home_page]
pg = st.navigation(pages=pages, position='hidden')

pg.run()