# to run Streamlit run main.py
import streamlit as st
from langchain_helper import *
st.title("Restaurent name generator")
cuisine=st.sidebar.selectbox('pick a cuisine', ('indian','mexican','italian','American'))



if cuisine:
    response=generate_restaurent_details(cuisine=cuisine)
    st.header(response['restaurent_name'])
    st.write('Menu items')
    menu_items = [item.strip() for item in response['menu'].split(",")]
    for item in menu_items:
        st.write(f"- {item}")
else:
    pass


