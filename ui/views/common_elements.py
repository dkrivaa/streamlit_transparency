import streamlit as st
import asyncio

from backend.utilities.general import run_async
from backend.data.super_class import SupermarketChain
from backend.database.utilities import get_stores_for_chain


def sort_classes_by_alias(classes: list[type]) -> list[type]:
    """
    Helper function for select_chain_element function.
    Sorts the given list of classes by their alias attribute """
    return sorted(classes, key=lambda x: x.alias)


def select_chain_element(key: str) -> SupermarketChain:
    """
    Renders the supermarket chain selection element.
    Args:
        key (str): The unique key for this selectbox element.
    """
    # Select Supermarket Chain
    chain = st.selectbox(
        label="Select Supermarket Chain",
        label_visibility='hidden',
        options=sort_classes_by_alias(SupermarketChain.registry),
        format_func=lambda x: x.alias.capitalize(),
        index=None,
        placeholder="Select Supermarket Chain",
        key=key
    )

    return chain


def select_store_element(chain: SupermarketChain, key: str) -> str:
    """
    Renders the store selection element for the given supermarket chain.
    Args:
        chain (SupermarketChain): The selected supermarket chain.
        key (str): The unique key for this selectbox element.
    """
    store_objects = run_async(get_stores_for_chain, chain=chain)
    store_options = {store.store_code: store.store_name for store in store_objects}

    store = st.selectbox(
        label="Select Store",
        label_visibility='hidden',
        options=sorted(list(store_options.keys()), key=int),
        format_func=lambda x: f'{x} - {store_options[x]}',
        index=None,
        placeholder="Select Supermarket Store",
        key=key
    )

    return store


def price_element(item: str, item_details: dict):
    """ Renders a single price element for the given item """
    st.subheader('Price')
    st.metric(
        label=f"{item} - {
        (
                item_details.get(item, {}).get("ItemName")
                or item_details.get(item, {}).get("ItemNm")
                or "N/A"
        )
        }",
        label_visibility='collapsed',
        value=(
            f"{item_details[item]['ItemPrice']} NIS"
            if item_details and item_details.get(item)
            else "N/A"
        ),
    )

    st.divider()


def promo_element(promo: dict):
    """ Renders a single promo element according to reward type"""
    # Dispatcher
    PROMO_RENDERERS = {
        '1': render_quantity_discount,
        '2': render_percentage_discount,
        '3': render_percentage_discount,
        '6': render_quantity_discount,
        '10': render_quantity_discount,
    }
    # Get reward type and corresponding handler
    reward_type = promo.get('RewardType')
    handler = PROMO_RENDERERS.get(reward_type, None)
    # Get chain from session state
    chain = st.session_state.get('chain', None)
    # Call handler if exists
    handler(chain, promo)


def render_quantity_discount(chain: SupermarketChain, promo: dict):
    """ Renders a single promo element with reward type 1"""
    st.markdown(f"**{promo.get('PromotionDescription', 'N/A')}**")
    st.metric(
        label="Promotion Price",
        value=f"{promo.get('DiscountedPrice', 'N/A')} NIS",
    )
    st.write(f"- Minimum Quantity: {promo.get('MinQty', 'N/A')}")
    st.write(f"- Maximum Quantity: {promo.get('MaxQty', 'N/A')}")
    st.write(f"- Minimum Purchase: {promo.get('MinPurchaseAmnt', 'N/A')}")
    st.write(f"- Target Customers: {chain.promo_audience(promo)}")
    st.write(f"- Valid Until: {promo.get('PromotionEndDate', 'N/A')}")
    st.divider()


def render_percentage_discount(chain: SupermarketChain, promo: dict):
    """ Renders a single promo element with reward type 2"""
    st.markdown(f"**{promo.get('PromotionDescription', 'N/A')}**")
    st.metric(
        label="Promotion Discount",
        value=f"{int(promo.get('DiscountRate')) / 100}%",
    )
    st.write(f"- Minimum Quantity: {promo.get('MinQty', 'N/A')}")
    st.write(f"- Maximum Quantity: {promo.get('MaxQty', 'N/A')}")
    st.write(f"- Target Customers: {chain.promo_audience(promo)}")
    st.write(f"- Valid Until: {promo.get('PromotionEndDate', 'N/A')}")
    st.divider()


