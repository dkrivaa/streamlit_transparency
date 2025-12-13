import streamlit as st

home_page = st.Page(
    title='Home',
    page='ui.views/home.py',
    default=True
)


pages = [home_page]
pg = st.navigation(pages=pages, position='hidden')

pg.run()