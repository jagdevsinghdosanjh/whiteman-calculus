import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def riemann_visualizer():
    st.header("Riemann Sum / Area Visualizer")

    expr = st.text_input("Function f(x)", "np.sin(x)")
    a = st.number_input("Lower limit a", value=0.0)
    b = st.number_input("Upper limit b", value=np.pi)
    n = st.slider("Number of rectangles", 4, 100, 10)

    # Domain for plotting
    xs = np.linspace(a, b, 400)

    # Safe evaluation environment
    safe_env = {"x": xs, "np": np}

    # Evaluate function curve
    try:
        ys = eval(expr, {"__builtins__": {}}, safe_env)
    except Exception as e:
        st.error(f"Error in expression: {e}")
        return

    # Midpoint Riemann sum
    dx = (b - a) / n
    x_mid = np.linspace(a + dx/2, b - dx/2, n)

    try:
        y_mid = eval(expr, {"__builtins__": {}}, {"x": x_mid, "np": np})
    except Exception as e:
        st.error(f"Error evaluating midpoints: {e}")
        return

    approx = np.sum(y_mid * dx)

    # Plot
    fig, ax = plt.subplots()
    ax.plot(xs, ys, label="f(x)")

    for xm, ym in zip(x_mid, y_mid):
        ax.bar(xm, ym, width=dx, alpha=0.3, align="center")

    ax.set_title(f"Approximate integral ≈ {approx:.4f}")
    ax.legend()
    st.pyplot(fig)

# import streamlit as st
# import numpy as np
# import matplotlib.pyplot as plt

# def riemann_visualizer():
#     st.header("Riemann Sum / Area Visualizer")

#     expr = st.text_input("Function f(x)", "np.sin(x)")
#     a = st.number_input("Lower limit a", value=0.0)
#     b = st.number_input("Upper limit b", value=np.pi)
#     n = st.slider("Number of rectangles", 4, 100, 10)

#     xs = np.linspace(a, b, 400)
#     try:
#         ys = eval(expr)
#     except Exception as e:
#         st.error(f"Error in expression: {e}")
#         return

#     dx = (b - a) / n
#     x_mid = np.linspace(a + dx/2, b - dx/2, n)
#     y_mid = eval(expr, {"x": x_mid, "np": np})
#     approx = np.sum(y_mid * dx)

#     fig, ax = plt.subplots()
#     ax.plot(xs, ys, label="f(x)")
#     for xm, ym in zip(x_mid, y_mid):
#         ax.bar(xm, ym, width=dx, alpha=0.3, align="center")
#     ax.set_title(f"Approximate integral ≈ {approx:.4f}")
#     st.pyplot(fig)
