import streamlit as st
from multiapp import MultiApp
from pages.eda import eda
from pages.home import home

st.set_page_config(page_title='AutoDS',
                   layout='wide')

app = MultiApp()

# Add all your application here
app.add_app("Home", home)
app.add_app("EDA", eda)

# The main app
app.run()
