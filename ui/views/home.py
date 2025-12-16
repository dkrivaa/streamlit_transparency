import streamlit as st



def options():
    """ Returns dict of options for home page navigation """
    return {
        0: {'icon': ':material/attach_money:', 'text': 'I am shopping', 'page': 'ui/views/check_price.py'},
        1: {'icon': ':material/list:', 'text': 'Plan my shopping', 'page': 'ui/views/shopping_list.py'},
    }


def render():
    """ The main function to render the home page """
    # Title and subtitle
    st.title("CLARITY")
    st.subheader('Supermarket Price Transparency')
    st.divider()

    # Options for navigation
    option_map = options()

    # Pills selection for navigation
    selection = st.pills(
        'Select',
        options=option_map.keys(),
        format_func=lambda option: f'{option_map[option]['icon']} {option_map[option]['text']}',
        selection_mode="single",
        default=None,
    )

    # Navigate to selected page
    if selection is not None:
        st.switch_page(option_map[selection]['page'])


if __name__ == "__main__":
    render()