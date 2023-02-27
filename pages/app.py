import streamlit as st
from streamlit_option_menu import option_menu

# 1. as sidebar menu
with st.sidebar:
    selected = option_menu("Main Menu", 
                           ["moun", 'capital ','mega'],)
    
if selected ==  "moun":
    st.title("Mountains Visualization Dashboard")
    st
    st.write("This is the mountains dashboard")
if selected ==  "capital ":
    st.title("Capital City Visualization Dashboard")
    st.write("This is the capital city dashboard")
if selected ==  "mega":
    st.title("Mega City Visualization Dashboard")
    st.write("This is the mega city dashboard")    

