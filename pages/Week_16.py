import streamlit as st
import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_PATH = os.path.join(BASE_DIR, "data", "curriculum.json")

st.set_page_config(page_title="Week 16 – Topics Overview", layout="wide")

st.title("Week 16 – Topics Overview")

with open(DATA_PATH, "r", encoding="utf-8") as f:
    curriculum = json.load(f)

week = curriculum.get("Week 16", {})

if not week:
    st.warning("No topics defined for Week 16.")
else:
    for day, topic in week.items():
        st.markdown(f"### {day}: {topic}")
