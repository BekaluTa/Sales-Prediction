
import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu

from Dashboard.home import home_app
from Dashboard.overview import overview_app
from Dashboard.predict import prdict_app

st.set_page_config(page_title="Sales Prediction on Pharmacy Data")

slected = option_menu(
    menu_title=None,
    options=["Home", "Overview", "Predict"],
    icons=["house", "globe2", "app"],
    menu_icon="cast",
    orientation="horizontal"
)
styles = {
    "container": {"padding": "0!important", "background-color": "#fafafa"},
    "icon": {"color": "orange", "font-size": "25px"},
    "nav-link": {"font-size": "25px", "text-align": "left", "margin": "0px", "--hover-color": "#eee"},
    "nav-link-selected": {"background-color": "green"},
}
st.title("Sales Data Prediction")


if slected == "Home":
    home_app()
elif slected == "Overview":
    overview_app()
else:
    prdict_app()