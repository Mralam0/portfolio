import streamlit
import streamlit as st

streamlit.set_page_config(layout="wide")


col1, col2  = st.columns(2)

with col1:
    st.image("images\image.png" )

with col2:
    st.title("Muhammad Rehan Alam")
    content = """
    mr
    """
    st.text(content)