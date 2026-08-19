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

    # -----------------------------
    # Evaluate f(x) over the range
    # -----------------------------
    try:
        ys = eval(expr, {"__builtins__": {}}, safe_env)
    except Exception as e:
        st.error(f"Error in expression: {e}")
        return

    # -----------------------------
    # Evaluate f(x0) and f(x0 + h)
    # -----------------------------
    try:
        f_x0 = eval(expr, {"__builtins__": {}}, {"x": x0, "np": np})
        f_x0_h = eval(expr, {"__builtins__": {}}, {"x": x0 + h, "np": np})
    except Exception as e:
        st.error(f"Error evaluating at x0: {e}")
        return

    # -----------------------------
    # Compute slope and tangent line
    # -----------------------------
    slope = (f_x0_h - f_x0) / h
    tangent_ys = f_x0 + slope * (xs - x0)

    # -----------------------------
    # Plot
    # -----------------------------
    fig, ax = plt.subplots()
    ax.plot(xs, ys, label="f(x)")
    ax.plot(xs, tangent_ys, label="Tangent at x0", linestyle="--")
    ax.scatter([x0], [f_x0], color="red")
    ax.legend()
    st.pyplot(fig)

    # ---------------------------------------------------------
    # Whitman Calculus Dynamic Description (Visible to Students)
    # ---------------------------------------------------------
    st.markdown("---")
    st.subheader("📘 Whitman Calculus Interpretation")

    st.markdown(f"""
### 🎯 What You Just Visualized

This tool shows exactly what Whitman Calculus Chapter 3 describes:
the **derivative as the slope of the tangent line**.

### 1. Function You Entered  
You entered:  
**f(x) = {expr}**

Whitman uses simple, smooth functions like this to build intuition about
how tangent lines behave and how slopes change.

### 2. Point of Tangency  
You chose:  
**x₀ = {x0}**

At this point:
- The function value is **f(x₀) = {f_x0:.4f}**
- The approximate derivative is **f'(x₀) ≈ {slope:.4f}**

Whitman emphasizes that the tangent line at x₀ is the **best linear approximation**
to the curve near that point.

### 3. The Role of h  
You selected:  
**h = {h}**

In Whitman’s limit definition:
\[f'(x_0) = \lim_{h \to 0} \frac{f(x_0 + h) - f(x_0)}{h}\]



Your value of h controls how close the secant line is to the true tangent.
As h → 0, the secant becomes the tangent — exactly what you see here.

### 4. Tangent Line You Saw  
The tangent line plotted is:



\[T(x) = f(x_0) + f'(x_0)(x - x_0)\]



Whitman stresses that this line:
- touches the curve at exactly one point  
- shares the same instantaneous slope  
- is the geometric meaning of the derivative  

### 📚 Why This Matters (Whitman Style)

This visualizer helps you *feel* the derivative:
- You see the curve  
- You see the tangent  
- You see how h controls the limit  
- You see slope emerging from geometry  

This is exactly the intuition Whitman builds in **Chapter 3: Derivatives**.
""")
