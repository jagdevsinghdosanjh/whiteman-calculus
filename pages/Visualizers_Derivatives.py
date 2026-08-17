import streamlit as st
from modules.derivatives.tangent_visualizer import tangent_visualizer

st.set_page_config(page_title="Derivatives Visualizer", layout="wide")
tangent_visualizer()
