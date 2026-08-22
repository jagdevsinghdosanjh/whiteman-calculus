import streamlit as st
import plotly.graph_objects as go
import numpy as np

# ---------------------------------------------------------
# Page Configuration
# ---------------------------------------------------------
st.set_page_config(page_title="Week 1 – Day 1", layout="wide")
st.title("Day 1: Functions & Graphs (Whitman Ch.1)")

# ---------------------------------------------------------
# Concept Overview
# ---------------------------------------------------------
st.header("📘 Concept Overview")
st.write("""
Functions describe relationships between quantities. Today you learn:
- What a function is
- Domain & range
- Graph interpretation
- Increasing/decreasing behavior
""")

# ---------------------------------------------------------
# Visualization Function
# ---------------------------------------------------------
def plot_function():
    x = np.linspace(-10, 10, 400)
    y = x**2

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, mode="lines", name="f(x)=x²"))
    fig.update_layout(
        title="Function Plot: f(x) = x²",
        xaxis_title="x",
        yaxis_title="f(x)",
        template="plotly_white"
    )
    return fig

# ---------------------------------------------------------
# Visualizations Section
# ---------------------------------------------------------
st.header("📊 Visualizations")
st.plotly_chart(plot_function(), use_container_width=True)

# ---------------------------------------------------------
# Practice Problems
# ---------------------------------------------------------
st.header("📝 Practice Problems")
st.info("Add Day‑1 problem set here.")
