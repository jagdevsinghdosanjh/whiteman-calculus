import streamlit as st
from modules.multivariable.gradient_visualizer import gradient_visualizer

st.set_page_config(page_title="Multivariable Visualizer", layout="wide")
gradient_visualizer()
