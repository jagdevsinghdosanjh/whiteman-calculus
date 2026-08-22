import streamlit as st
import plotly.graph_objects as go
import numpy as np

# ---------------------------------------------------------
# Page Configuration
# ---------------------------------------------------------
st.set_page_config(page_title="Week 1 – Day 5", layout="wide")
st.title("Day 5: Continuity & Limit Laws")

# ---------------------------------------------------------
# Concept Overview
# ---------------------------------------------------------
st.header("📘 Concept Overview")
st.write("""
Topics covered:
- Definition of continuity
- Types of discontinuities
- Limit algebra laws
- Composition & continuity
""")

# ---------------------------------------------------------
# Interactive Controls
# ---------------------------------------------------------
st.header("🎛️ Interactive Continuity Explorer")

col1, col2, col3 = st.columns(3)

with col1:
    slope = st.slider("Slope (m)", 0.5, 5.0, 1.0, step=0.1)

with col2:
    discontinuity_x = st.slider("Discontinuity at x =", -3.0, 3.0, 1.0, step=0.1)

with col3:
    show_hole = st.checkbox("Show Removable Discontinuity", value=True)

# ---------------------------------------------------------
# Visualization Function
# ---------------------------------------------------------
def plot_continuity(m, hole_x, show_hole_flag):
    x = np.linspace(-3, 3, 400)

    # Base function: f(x) = m*x + 2
    y = m * x + 2

    # Remove value at discontinuity point
    y_plot = np.where(np.abs(x - hole_x) < 1e-6, None, y)

    fig = go.Figure()

    # Main function
    fig.add_trace(go.Scatter(
        x=x, y=y_plot, mode="lines", name=f"f(x) = {m}x + 2"
    ))

    # Hole (removable discontinuity)
    if show_hole_flag:
        fig.add_trace(go.Scatter(
            x=[hole_x], y=[m * hole_x + 2],
            mode="markers",
            marker=dict(size=12, color="red"),
            name="Hole (Removable Discontinuity)"
        ))

    fig.update_layout(
        title="Interactive Continuity & Removable Discontinuity",
        xaxis_title="x",
        yaxis_title="f(x)",
        template="plotly_white"
    )

    return fig

# ---------------------------------------------------------
# Visualizations Section
# ---------------------------------------------------------
st.header("📊 Visualizations")
fig = plot_continuity(slope, discontinuity_x, show_hole)
st.plotly_chart(fig, use_container_width=True)

# ---------------------------------------------------------
# Practice Problems
# ---------------------------------------------------------
st.header("📝 Practice Problems")
st.info("Add Day‑5 problem set here.")

# import streamlit as st
# import plotly.graph_objects as go
# import numpy as np
# st.set_page_config(page_title="Week 1 – Day 5", layout="wide")
# st.title("Day 5: Continuity & Limit Laws")

# st.header("📘 Concept Overview")
# st.write("""
# Topics covered:
# - Definition of continuity
# - Types of discontinuities
# - Limit algebra laws
# - Composition & continuity
# """)

# st.header("📊 Visualizations")
# st.info("Add continuity/discontinuity graphs here.")


# x = np.linspace(-3, 3, 400)
# y = np.where(x != 1, x + 2, None)

# fig = go.Figure()
# fig.add_trace(go.Scatter(x=x, y=y, mode="lines", name="f(x)=x+2"))
# fig.add_trace(go.Scatter(x=[1], y=[3], mode="markers", marker=dict(size=10, color="red"), name="Hole at x=1"))

# fig.update_layout(title="Continuity & Removable Discontinuity", xaxis_title="x", yaxis_title="f(x)")
# st.plotly_chart(fig, use_container_width=True)

# st.header("📝 Practice Problems")
# st.info("Add Day‑5 problem set here.")
