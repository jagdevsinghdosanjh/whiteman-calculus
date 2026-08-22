import streamlit as st
import plotly.graph_objects as go
import numpy as np

# ---------------------------------------------------------
# Page Configuration
# ---------------------------------------------------------
st.set_page_config(page_title="Week 1 – Day 2", layout="wide")
st.title("Day 2: Inverse Functions & Transformations")

# ---------------------------------------------------------
# Concept Overview
# ---------------------------------------------------------
st.header("📘 Concept Overview")
st.write("""
Topics covered:
- One‑to‑one functions
- Finding inverses
- Horizontal line test
- Graph transformations (shift, stretch, reflect)
""")

# ---------------------------------------------------------
# Interactive Controls
# ---------------------------------------------------------
st.header("🎛️ Interactive Transformations")

col1, col2, col3 = st.columns(3)

with col1:
    h_shift = st.slider("Horizontal Shift (h)", -5.0, 5.0, 0.0)

with col2:
    v_shift = st.slider("Vertical Shift (k)", -5.0, 5.0, 0.0)

with col3:
    stretch = st.slider("Vertical Stretch (a)", 0.1, 5.0, 1.0)

reflect = st.checkbox("Reflect across x-axis")

# ---------------------------------------------------------
# Visualization Function
# ---------------------------------------------------------
def plot_inverse_transformations(h, k, a, reflect_flag):
    x = np.linspace(1, 10, 400)

    # Base function
    f = np.log(x)

    # Apply transformations: a * f(x - h) + k
    x_transformed = x - h
    f_transformed = a * np.log(np.clip(x_transformed, 0.1, None)) + k

    if reflect_flag:
        f_transformed = -f_transformed

    # Inverse of transformed function (approx)
    # If y = a ln(x - h) + k → inverse is x = exp((y - k)/a) + h
    y_vals = np.linspace(min(f_transformed), max(f_transformed), 400)
    inv_transformed = np.exp((y_vals - k) / (a if a != 0 else 1)) + h
    if reflect_flag:
        inv_transformed = np.exp((-y_vals - k) / (a if a != 0 else 1)) + h

    fig = go.Figure()

    # Original ln(x)
    fig.add_trace(go.Scatter(
        x=x, y=f, mode="lines", name="Original f(x)=ln(x)"
    ))

    # Transformed function
    fig.add_trace(go.Scatter(
        x=x, y=f_transformed, mode="lines", name="Transformed f(x)"
    ))

    # Inverse of transformed function
    fig.add_trace(go.Scatter(
        x=inv_transformed, y=y_vals, mode="lines", name="Inverse of Transformed f(x)"
    ))

    fig.update_layout(
        title="Interactive Inverse & Transformations",
        xaxis_title="x",
        yaxis_title="y",
        template="plotly_white"
    )

    return fig

# ---------------------------------------------------------
# Visualizations Section
# ---------------------------------------------------------
st.header("📊 Visualizations")
fig = plot_inverse_transformations(h_shift, v_shift, stretch, reflect)
st.plotly_chart(fig, use_container_width=True)

# ---------------------------------------------------------
# Practice Problems
# ---------------------------------------------------------
st.header("📝 Practice Problems")
st.info("Add Day‑2 problem set here.")

# import streamlit as st
# import plotly.graph_objects as go
# import numpy as np

# # ---------------------------------------------------------
# # Page Configuration
# # ---------------------------------------------------------
# st.set_page_config(page_title="Week 1 – Day 2", layout="wide")
# st.title("Day 2: Inverse Functions & Transformations")

# # ---------------------------------------------------------
# # Concept Overview
# # ---------------------------------------------------------
# st.header("📘 Concept Overview")
# st.write("""
# Topics covered:
# - One‑to‑one functions
# - Finding inverses
# - Horizontal line test
# - Graph transformations (shift, stretch, reflect)
# """)

# # ---------------------------------------------------------
# # Visualization Function
# # ---------------------------------------------------------
# def plot_inverse_functions():
#     x = np.linspace(1, 10, 400)
#     f = np.log(x)
#     inv = np.exp(x)

#     fig = go.Figure()

#     fig.add_trace(go.Scatter(
#         x=x, y=f, mode="lines", name="f(x) = ln(x)"
#     ))

#     fig.add_trace(go.Scatter(
#         x=f, y=x, mode="lines", name="Inverse: exp(x)"
#     ))

#     fig.update_layout(
#         title="Inverse Function Visualization",
#         xaxis_title="x",
#         yaxis_title="y",
#         template="plotly_white"
#     )

#     return fig

# # ---------------------------------------------------------
# # Visualizations Section
# # ---------------------------------------------------------
# st.header("📊 Visualizations")
# st.plotly_chart(plot_inverse_functions(), use_container_width=True)

# # ---------------------------------------------------------
# # Practice Problems
# # ---------------------------------------------------------
# st.header("📝 Practice Problems")
# st.info("Add Day‑2 problem set here.")
