import streamlit as st
from multiapp import MultiApp
from app import home, fe_LEDs, fe_LIPs

app = MultiApp()
st.set_page_config(page_title='| Home Page', page_icon='👋')

app.add_app("My Home Page", home.app)
app.add_app("Leaf Diseases Detection", fe_LEDs.app)
app.run()