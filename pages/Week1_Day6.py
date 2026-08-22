import streamlit as st
import plotly.graph_objects as go
import numpy as np

# ---------------------------------------------------------
# Page Configuration
# ---------------------------------------------------------
st.set_page_config(page_title="Week 1 – Day 6", layout="wide")
st.title("Day 6: Problem Set + Function Visualizations")

# ---------------------------------------------------------
# Summary Section
# ---------------------------------------------------------
st.header("📘 Summary of Week 1")
st.write("""
Today you consolidate:
- Functions & graphs
- Inverses & transformations
- Limits (intuitive + rigorous)
- Continuity & limit laws
""")

# ---------------------------------------------------------
# Interactive Controls
# ---------------------------------------------------------
st.header("🎛️ Choose Topics to Visualize")

topic_options = {
    "Day 1: f(x)=x²": lambda x: x**2,
    "Day 2: sin(x) Transform": lambda x: np.sin(x),
    "Day 3: Limit Function (x²−1)/(x−1)": lambda x: (x**2 - 1) / (x - 1),
    "Day 4: Linear Limit 2x+1": lambda x: 2*x + 1,
    "Day 5: Continuity f(x)=x+2": lambda x: np.where(x != 1, x + 2, None)
}

selected_topics = st.multiselect(
    "Select one or more Week‑1 topics to visualize:",
    list(topic_options.keys()),
    default=list(topic_options.keys())  # show all by default
)

# ---------------------------------------------------------
# Visualization Function
# ---------------------------------------------------------
def plot_combined_topics(selected):
    x = np.linspace(-10, 10, 400)
    fig = go.Figure()

    for topic in selected:
        y = topic_options[topic](x)
        fig.add_trace(go.Scatter(
            x=x, y=y, mode="lines", name=topic
        ))

    fig.update_layout(
        title="Interactive Combined Visualizations for Week 1",
        xaxis_title="x",
        yaxis_title="y",
        legend_title="Topics",
        template="plotly_white"
    )

    return fig

# ---------------------------------------------------------
# Visualizations Section
# ---------------------------------------------------------
st.header("📊 Visualizations")
fig = plot_combined_topics(selected_topics)
st.plotly_chart(fig, use_container_width=True)

# ---------------------------------------------------------
# Problem Set Section
# ---------------------------------------------------------
st.header("📝 Full Week‑1 Problem Set")
st.info("Add complete problem bank here.")

# import streamlit as st
# import plotly.graph_objects as go
# import numpy as np
# st.set_page_config(page_title="Week 1 – Day 6", layout="wide")
# st.title("Day 6: Problem Set + Function Visualizations")

# st.header("📘 Summary of Week 1")
# st.write("""
# Today you consolidate:
# - Functions & graphs
# - Inverses & transformations
# - Limits (intuitive + rigorous)
# - Continuity & limit laws
# """)

# st.header("📊 Visualizations")
# st.info("Add combined visualizations for all Week‑1 concepts.")


# x = np.linspace(-10, 10, 400)

# fig = go.Figure()

# fig.add_trace(go.Scatter(x=x, y=x**2, mode="lines", name="Day 1: f(x)=x²"))
# fig.add_trace(go.Scatter(x=x, y=np.sin(x), mode="lines", name="Day 2: sin(x) Transform"))
# fig.add_trace(go.Scatter(x=x, y=(x**2 - 1)/(x - 1), mode="lines", name="Day 3: Limit Function"))
# fig.add_trace(go.Scatter(x=x, y=2*x + 1, mode="lines", name="Day 4: Linear Limit"))
# fig.add_trace(go.Scatter(x=x, y=np.where(x != 1, x + 2, None), mode="lines", name="Day 5: Continuity"))

# fig.update_layout(
#     title="Combined Visualizations for Week 1",
#     xaxis_title="x",
#     yaxis_title="y",
#     legend_title="Topics"
# )

# st.plotly_chart(fig, use_container_width=True)

# st.header("📝 Full Week‑1 Problem Set")
# st.info("Add complete problem bank here.")
