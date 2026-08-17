import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def ode_visualizer():
    st.header("ODE Direction Field")

    expr = st.text_input("dy/dx = f(x, y)", "y - x")
    x_min, x_max = st.slider("x-range", -5.0, 5.0, (-2.0, 2.0))
    y_min, y_max = st.slider("y-range", -5.0, 5.0, (-2.0, 2.0))
    density = st.slider("Grid density", 10, 30, 20)

    x = np.linspace(x_min, x_max, density)
    y = np.linspace(y_min, y_max, density)
    X, Y = np.meshgrid(x, y)

    try:
        dY = eval(expr, {"x": X, "y": Y, "np": np})
    except Exception as e:
        st.error(f"Error in expression: {e}")
        return

    dX = np.ones_like(dY)
    mag = np.sqrt(dX**2 + dY**2)
    dX /= mag
    dY /= mag

    fig, ax = plt.subplots()
    ax.quiver(X, Y, dX, dY)
    ax.set_title("Direction Field")
    st.pyplot(fig)
