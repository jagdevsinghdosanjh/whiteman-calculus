import streamlit as st
import plotly.graph_objects as go
import numpy as np

# ---------------------------------------------------------
# Page Configuration
# ---------------------------------------------------------
st.set_page_config(page_title="Week 1 – Day 4", layout="wide")
st.title("Day 4: Limits – Rigorous MIT Definition")

# ---------------------------------------------------------
# Concept Overview
# ---------------------------------------------------------
st.header("📘 Concept Overview")
st.write("""
Formal limit definition (MIT style):
- ε–δ definition
- Logical structure of proofs
- Why rigor matters
""")

# ---------------------------------------------------------
# Interactive Controls
# ---------------------------------------------------------
st.header("🎛️ ε–δ Interactive Controls")

col1, col2, col3 = st.columns(3)

with col1:
    eps = st.slider("Choose ε", 0.1, 2.0, 0.5, step=0.1)

with col2:
    delta = st.slider("Choose δ", 0.1, 2.0, 0.5, step=0.1)

with col3:
    x_approach = st.slider("Move x toward 2", 0.0, 4.0, 2.0, step=0.1)

# ---------------------------------------------------------
# Visualization Function
# ---------------------------------------------------------
def plot_epsilon_delta(eps, delta, x_val):
    x = np.linspace(0, 4, 400)
    f = 2*x + 1
    a = 2
    L = 5

    fig = go.Figure()

    # Main function
    fig.add_trace(go.Scatter(
        x=x, y=f, mode="lines", name="f(x) = 2x + 1"
    ))

    # ε-band around L
    fig.add_hrect(
        y0=L - eps, y1=L + eps,
        fillcolor="lightgreen", opacity=0.3, line_width=0,
        annotation_text="ε-band", annotation_position="top left"
    )

    # δ-band around a
    fig.add_vrect(
        x0=a - delta, x1=a + delta,
        fillcolor="lightblue", opacity=0.3, line_width=0,
        annotation_text="δ-band", annotation_position="top right"
    )

    # Moving point showing f(x)
    y_val = 2*x_val + 1
    fig.add_trace(go.Scatter(
        x=[x_val], y=[y_val],
        mode="markers",
        marker=dict(size=12, color="red"),
        name=f"Point (x={x_val:.2f}, f(x)={y_val:.2f})"
    ))

    fig.update_layout(
        title="Interactive ε–δ Visualization",
        xaxis_title="x",
        yaxis_title="f(x)",
        template="plotly_white"
    )

    return fig

# ---------------------------------------------------------
# Visualizations Section
# ---------------------------------------------------------
st.header("📊 Visualizations")
fig = plot_epsilon_delta(eps, delta, x_approach)
st.plotly_chart(fig, use_container_width=True)

# ---------------------------------------------------------
# Practice Problems
# ---------------------------------------------------------
st.header("📝 Practice Problems")
st.info("Add Day‑4 problem set here.")

# import streamlit as st
# import plotly.graph_objects as go
# import numpy as np
# st.set_page_config(page_title="Week 1 – Day 4", layout="wide")
# st.title("Day 4: Limits – Rigorous MIT Definition")

# st.header("📘 Concept Overview")
# st.write("""
# Formal limit definition (MIT style):
# - ε–δ definition
# - Logical structure of proofs
# - Why rigor matters
# """)

# st.header("📊 Visualizations")
# st.info("Add epsilon-delta interactive visualization here.")


# x = np.linspace(0, 4, 400)
# f = 2*x + 1
# L = 5  # limit at x=2

# fig = go.Figure()
# fig.add_trace(go.Scatter(x=x, y=f, mode="lines", name="f(x)=2x+1"))

# # epsilon band
# eps = 0.5
# fig.add_hrect(y0=L-eps, y1=L+eps, fillcolor="lightgreen", opacity=0.3, line_width=0)

# # delta band
# delta = 0.5
# fig.add_vrect(x0=2-delta, x1=2+delta, fillcolor="lightblue", opacity=0.3, line_width=0)

# fig.update_layout(title="ε–δ Visualization for Limit", xaxis_title="x", yaxis_title="f(x)")
# st.plotly_chart(fig, use_container_width=True)

# st.header("📝 Practice Problems")
# st.info("Add Day‑4 problem set here.")
