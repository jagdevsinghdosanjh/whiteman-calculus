import streamlit as st
import plotly.graph_objects as go
import numpy as np

# ---------------------------------------------------------
# Page Configuration
# ---------------------------------------------------------
st.set_page_config(page_title="Week 1 – Day 3", layout="wide")
st.title("Day 3: Limits – Intuition (Whitman Ch.2)")

# ---------------------------------------------------------
# Concept Overview
# ---------------------------------------------------------
st.header("📘 Concept Overview")
st.write("""
Intuitive understanding of limits:
- Approaching a value
- Left-hand & right-hand behavior
- Graph-based limit intuition
""")

# ---------------------------------------------------------
# Interactive Controls
# ---------------------------------------------------------
st.header("🎛️ Interactive Limit Explorer")

col1, col2 = st.columns(2)

with col1:
    approach_point = st.slider("Approach x → a", -2.0, 2.0, 1.0, step=0.1)

with col2:
    show_lr = st.checkbox("Show Left & Right Approach Arrows")

# ---------------------------------------------------------
# Visualization Function
# ---------------------------------------------------------
def plot_limit_intuition(a, show_lr_arrows):
    x = np.linspace(-2, 2, 400)
    y = (x**2 - 1) / (x - 1)

    # True limit value at x = 1
    limit_value = 2

    fig = go.Figure()

    # Main function curve
    fig.add_trace(go.Scatter(
        x=x, y=y, mode="lines", name="f(x) = (x²−1)/(x−1)"
    ))

    # Removable discontinuity point
    fig.add_trace(go.Scatter(
        x=[1], y=[limit_value],
        mode="markers",
        marker=dict(size=10, color="red"),
        name="Limit Point (Removable)"
    ))

    # Dynamic approach marker
    y_a = (a**2 - 1) / (a - 1) if a != 1 else None

    fig.add_trace(go.Scatter(
        x=[a], y=[y_a],
        mode="markers",
        marker=dict(size=12, color="blue"),
        name=f"Approach Point (x → {a})"
    ))

    # Left & right arrows
    if show_lr_arrows:
        fig.add_annotation(x=a - 0.2, y=limit_value,
                           text="← Left-hand limit",
                           showarrow=True, arrowhead=2)

        fig.add_annotation(x=a + 0.2, y=limit_value,
                           text="Right-hand limit →",
                           showarrow=True, arrowhead=2)

    fig.update_layout(
        title="Interactive Limit Intuition: Removable Discontinuity",
        xaxis_title="x",
        yaxis_title="f(x)",
        template="plotly_white"
    )

    return fig

# ---------------------------------------------------------
# Visualizations Section
# ---------------------------------------------------------
st.header("📊 Visualizations")
fig = plot_limit_intuition(approach_point, show_lr)
st.plotly_chart(fig, use_container_width=True)

# ---------------------------------------------------------
# Practice Problems
# ---------------------------------------------------------
st.header("📝 Practice Problems")
st.info("Add Day‑3 problem set here.")

# import streamlit as st
# import plotly.graph_objects as go
# import numpy as np

# st.set_page_config(page_title="Week 1 – Day 3", layout="wide")
# st.title("Day 3: Limits – Intuition (Whitman Ch.2)")

# st.header("📘 Concept Overview")
# st.write("""
# Intuitive understanding of limits:
# - Approaching a value
# - Left-hand & right-hand behavior
# - Graph-based limit intuition
# """)

# st.header("📊 Visualizations")
# st.info("Add limit-approach animations or graphs here.")

# x = np.linspace(-2, 2, 400)
# y = (x**2 - 1) / (x - 1)

# fig = go.Figure()
# fig.add_trace(go.Scatter(x=x, y=y, mode="lines", name="(x²−1)/(x−1)"))
# fig.add_trace(go.Scatter(x=[1], y=[2], mode="markers", marker=dict(size=10, color="red"), name="Limit Point"))

# fig.update_layout(title="Limit Intuition: Removable Discontinuity", xaxis_title="x", yaxis_title="y")
# st.plotly_chart(fig, use_container_width=True)

# st.header("📝 Practice Problems")
# st.info("Add Day‑3 problem set here.")
