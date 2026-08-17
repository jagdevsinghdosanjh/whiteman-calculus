import streamlit as st
from modules.integrals.riemann_visualizer import riemann_visualizer

st.set_page_config(page_title="Integrals Visualizer", layout="wide")
riemann_visualizer()
