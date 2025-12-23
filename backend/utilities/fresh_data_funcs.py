import streamlit as st

from backend.utilities.general import run_async
from backend.utilities.url_to_dict import data_dict
from backend.data.super_class import SupermarketChain


@st.cache_data(ttl=1800)
def fresh_price_data(alias: str, store_code: str | int) -> dict | None:
    """ Fetch fresh data for the given chain and store code """
    # Get the supermarket chain class from its alias
    chain = next((c for c in SupermarketChain.registry if c.alias == alias), None)
    # Get the latest price URLs for the given chain and store code
    urls = run_async(chain.prices, store_code=store_code) if chain and store_code else None
    # Use pricefull URL and cookies if available
    url = urls.get('pricefull') or urls.get('PriceFull') if urls else None
    cookies = urls.get('cookies', None) if urls else None
    # Make data dict from data in pricefull URL
    price_dict = run_async(data_dict, url=url, cookies=cookies) if url else None
    # Clean data dict to only include dicts of items
    price_data = chain.get_price_data(price_data=price_dict) if price_dict else None
    return price_data


@st.cache_data(ttl=1800)
def fresh_promo_data(alias: str, store_code: str | int) -> dict | None:
    """ Fetch fresh data for the given chain and store code """
    # Get the supermarket chain class from its alias
    chain = next((c for c in SupermarketChain.registry if c.alias == alias), None)
    # Get the latest price URLs for the given chain and store code
    urls = run_async(chain.prices, store_code=store_code) if chain and store_code else None
    # Use promofull URL and cookies if available
    url = urls.get('promofull') or urls.get('PromoFull') if urls else None
    cookies = urls.get('cookies', None) if urls else None
    # Make data dict from data in pricefull URL
    promo_dict = run_async(data_dict, url=url, cookies=cookies) if url else None
    # Clean data dict to only include dicts of items
    promo_data = chain.get_promo_data(promo_data=promo_dict) if promo_dict else None
    return promo_data
