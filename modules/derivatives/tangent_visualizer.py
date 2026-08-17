import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def tangent_visualizer():
    st.header("Derivative / Tangent Visualizer")

    expr = st.text_input("Function f(x)", "x**2")
    x0 = st.number_input("Point x0", value=1.0)
    h = st.number_input("Small h", value=1e-3)

    # Define x for vectorized evaluation
    xs = np.linspace(x0 - 3, x0 + 3, 400)

    # Safe evaluation environment
    safe_env = {"x": xs, "np": np}

    try:
        ys = eval(expr, {"__builtins__": {}}, safe_env)
    except Exception as e:
        st.error(f"Error in expression: {e}")
        return

    # Evaluate f(x0) and f(x0+h)
    try:
        f_x0 = eval(expr, {"__builtins__": {}}, {"x": x0, "np": np})
        f_x0_h = eval(expr, {"__builtins__": {}}, {"x": x0 + h, "np": np})
    except Exception as e:
        st.error(f"Error evaluating at x0: {e}")
        return

    slope = (f_x0_h - f_x0) / h
    tangent_ys = f_x0 + slope * (xs - x0)

    fig, ax = plt.subplots()
    ax.plot(xs, ys, label="f(x)")
    ax.plot(xs, tangent_ys, label="Tangent at x0", linestyle="--")
    ax.scatter([x0], [f_x0], color="red")
    ax.legend()
    st.pyplot(fig)

# import streamlit as st
# import numpy as np
# import matplotlib.pyplot as plt

# def tangent_visualizer():
#     st.header("Derivative / Tangent Visualizer")

#     expr = st.text_input("Function f(x)", "x**2")
#     x0 = st.number_input("Point x0", value=1.0)
#     h = st.number_input("Small h", value=1e-3)

#     xs = np.linspace(x0 - 3, x0 + 3, 400)
    
#     # Safe evaluation environment
#     safe_env = {"x": xs, "np": np}
    
#     try:
#         ys = eval(expr)
#     except Exception as e:
#         st.error(f"Error in expression: {e}")
#         return

#     f_x0 = eval(expr, {"x": x0, "np": np})
#     f_x0_h = eval(expr, {"x": x0 + h, "np": np})
#     slope = (f_x0_h - f_x0) / h
#     tangent_ys = f_x0 + slope * (xs - x0)

#     fig, ax = plt.subplots()
#     ax.plot(xs, ys, label="f(x)")
#     ax.plot(xs, tangent_ys, label="Tangent at x0", linestyle="--")
#     ax.scatter([x0], [f_x0], color="red")
#     ax.legend()
#     st.pyplot(fig)