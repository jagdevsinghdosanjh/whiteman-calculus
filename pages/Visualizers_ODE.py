import streamlit as st
from modules.differential_equations.ode_solver import ode_visualizer

st.set_page_config(page_title="ODE Visualizer", layout="wide")
ode_visualizer()
