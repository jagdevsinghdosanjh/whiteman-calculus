import streamlit as st
from modules.limits.visualizer import limit_visualizer

st.set_page_config(page_title="Limits Visualizer", layout="wide")
limit_visualizer()
