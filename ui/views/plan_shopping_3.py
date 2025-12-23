import streamlit as st

from backend.utilities.general import run_async
from backend.utilities.fresh_data_funcs import fresh_price_data, fresh_promo_data
from backend.data.super_class import SupermarketChain
from backend.database.utilities import get_stores_for_chain


