import matplotlib.pyplot as plt
import numpy as np
import streamlit as st


def gradient_visualizer():
    st.header("Gradient Field Visualizer")

    expr = st.text_input("Scalar field f(x, y)", "x**2 + y**2")
    x_min, x_max = st.slider("x-range", -5.0, 5.0, (-2.0, 2.0))
    y_min, y_max = st.slider("y-range", -5.0, 5.0, (-5.0, 5.0))
    density = st.slider("Grid density", 10, 30, 20)

    x = np.linspace(x_min, x_max, density)
    y = np.linspace(y_min, y_max, density)
    X, Y = np.meshgrid(x, y)

    try:
        F = eval(expr, {"x": X, "y": Y, "np": np})
    except Exception as e:
        st.error(f"Error in expression: {e}")
        return

    dFx = (eval(expr, {"x": X + 1e-3, "y": Y, "np": np}) - F) / 1e-3
    dFy = (eval(expr, {"x": X, "y": Y + 1e-3, "np": np}) - F) / 1e-3

    fig, ax = plt.subplots()
    ax.quiver(X, Y, dFx, dFy)
    ax.set_title("Gradient ∇f(x, y)")
    st.pyplot(fig)
