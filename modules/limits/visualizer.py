import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def limit_visualizer():
    st.header("Limit Visualizer")

    expr = st.text_input("Function f(x)", "np.sin(x)/x")
    a = st.number_input("Point a", value=0.0)
    eps = st.number_input("Neighborhood size", value=1.0)

    # Domain around the point
    xs = np.linspace(a - eps, a + eps, 400)

    # Safe evaluation environment
    safe_env = {"x": xs, "np": np}

    # Evaluate function curve
    try:
        ys = eval(expr, {"__builtins__": {}}, safe_env)
    except Exception as e:
        st.error(f"Error in expression: {e}")
        return

    fig, ax = plt.subplots()
    ax.plot(xs, ys, label="f(x)")
    ax.axvline(a, color="red", linestyle="--", label="x = a")
    ax.set_title(f"Behavior of f(x) near x = {a}")
    ax.legend()
    st.pyplot(fig)

# import streamlit as st
# import numpy as np
# import matplotlib.pyplot as plt

# def limit_visualizer():
#     st.header("Limit Visualizer")

#     expr = st.text_input("Function f(x)", "np.sin(x)/x")
#     a = st.number_input("Point a", value=0.0)
#     eps = st.number_input("Neighborhood size", value=1.0)

#     xs = np.linspace(a - eps, a + eps, 400)
#     try:
#         ys = eval(expr)
#     except Exception as e:
#         st.error(f"Error in expression: {e}")
#         return

#     fig, ax = plt.subplots()
#     ax.plot(xs, ys)
#     ax.axvline(a, color="red", linestyle="--")
#     ax.set_title(f"Behavior of f(x) near x = {a}")
#     st.pyplot(fig)
