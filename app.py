import json
import os
import streamlit as st
from datetime import date
from pathlib import Path

from supabase_client import get_user, login, supabase
from utils.attendance_utils import mark_attendance
from utils.date_utils import get_day_number, get_week_and_day, is_sunday


# ---------------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------------
st.set_page_config(page_title="Calculus Learning Portal", layout="wide")


# ---------------------------------------------------------
# LOAD CSS
# ---------------------------------------------------------
def load_css():
    css_path = Path(__file__).parent / "assets" / "styles.css"
    if css_path.exists():
        st.markdown(f"<style>{css_path.read_text()}</style>", unsafe_allow_html=True)

load_css()


# ---------------------------------------------------------
# AUTHENTICATION
# ---------------------------------------------------------
user = get_user()
if not user:
    st.title("Login to Calculus Portal")

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        login(email, password)
        st.rerun()   # Force rerun so navigation appears immediately

    st.page_link("pages/Signup.py", label="Create a new account")
    st.stop()

student_id = user.user.id
student_email = user.user.email


# ---------------------------------------------------------
# REGISTRATION CHECK
# ---------------------------------------------------------
student_exists = (
    supabase.table("students")
    .select("id")
    .eq("id", student_id)
    .execute()
)

if not student_exists.data:
    st.error("You must complete registration before accessing lessons.")
    st.page_link("pages/Register.py", label="Go to Registration")
    st.stop()


# ---------------------------------------------------------
# SIDEBAR NAVIGATION + LOGOUT
# ---------------------------------------------------------
st.sidebar.title("Navigation")

st.sidebar.page_link("app.py", label="Today's Lesson")
st.sidebar.page_link("pages/Student_Dashboard.py", label="Student Dashboard")
st.sidebar.page_link("pages/Admin_Dashboard.py", label="Admin Dashboard")

st.sidebar.markdown("---")
st.sidebar.subheader("Week Overviews")
for i in range(1, 16):
    st.sidebar.page_link(f"pages/Week_{i:02d}.py", label=f"Week {i} Overview")

st.sidebar.markdown("---")
st.sidebar.subheader("Assignments")
st.sidebar.page_link("pages/Assignments.py", label="Assignments & Quizzes")

st.sidebar.markdown("---")
st.sidebar.subheader("Visualizers")
st.sidebar.page_link("pages/Visualizers_Limits.py", label="Limits")
st.sidebar.page_link("pages/Visualizers_Derivatives.py", label="Derivatives")
st.sidebar.page_link("pages/Visualizers_Integrals.py", label="Integrals")
st.sidebar.page_link("pages/Visualizers_ODE.py", label="ODE")
st.sidebar.page_link("pages/Visualizers_Multivariable.py", label="Multivariable")

st.sidebar.markdown("---")
if st.sidebar.button("Logout"):
    supabase.auth.sign_out()
    st.rerun()   # Immediately reload → user goes back to login


# ---------------------------------------------------------
# JOINING DATE
# ---------------------------------------------------------
if "join_date" not in st.session_state:
    st.session_state.join_date = date.today()

join_date = st.session_state.join_date
today = date.today()


# ---------------------------------------------------------
# SUNDAY SKIP
# ---------------------------------------------------------
if is_sunday(today):
    st.title("Sunday – No Class")
    st.info("Relax, revise lightly, or explore visualizations.")
    st.stop()


# ---------------------------------------------------------
# DAY NUMBER → WEEK/DAY
# ---------------------------------------------------------
day_number = get_day_number(join_date, today)
week, day = get_week_and_day(day_number)


# ---------------------------------------------------------
# LOAD CURRICULUM
# ---------------------------------------------------------
BASE_DIR = os.path.dirname(__file__)
CURRICULUM_PATH = os.path.join(BASE_DIR, "data", "curriculum.json")

with open(CURRICULUM_PATH, "r", encoding="utf-8") as f:
    curriculum = json.load(f)

topic = curriculum.get(f"Week {week}", {}).get(f"Day {day}", "No topic assigned")


# ---------------------------------------------------------
# MARK ATTENDANCE
# ---------------------------------------------------------
mark_attendance(student_id, "Present")


# ---------------------------------------------------------
# SAFE PROGRESS LOGGING
# ---------------------------------------------------------
existing_progress = (
    supabase.table("student_progress")
    .select("id")
    .eq("student_id", student_id)
    .eq("progress_date", str(today))
    .execute()
)

if not existing_progress.data:
    day_in_week = ((day_number - 1) % 7) + 1

    supabase.table("student_progress").insert({
        "student_id": student_id,
        "progress_date": str(today),
        "week_number": week,
        "day_number": day_number,
        "day_in_week": day_in_week
    }).execute()


# ---------------------------------------------------------
# DISPLAY TODAY'S LESSON
# ---------------------------------------------------------
st.title(f"Week {week} – Day {day}")
st.subheader(topic)

st.success("Your attendance for today has been marked as **Present**.")
st.info("Use the sidebar to explore dashboards, visualizers, and week overviews.")

# import json
# import os
# import streamlit as st
# from datetime import date
# from pathlib import Path

# from supabase_client import get_user, login, supabase
# from utils.attendance_utils import mark_attendance
# from utils.date_utils import get_day_number, get_week_and_day, is_sunday


# # ---------------------------------------------------------
# # PAGE CONFIG
# # ---------------------------------------------------------
# st.set_page_config(page_title="Calculus Learning Portal", layout="wide")


# # ---------------------------------------------------------
# # LOAD CSS
# # ---------------------------------------------------------
# def load_css():
#     css_path = Path(__file__).parent / "assets" / "styles.css"
#     if css_path.exists():
#         st.markdown(f"<style>{css_path.read_text()}</style>", unsafe_allow_html=True)

# load_css()


# # ---------------------------------------------------------
# # AUTHENTICATION
# # ---------------------------------------------------------
# user = get_user()
# if not user:
#     st.title("Login to Calculus Portal")
#     email = st.text_input("Email")
#     password = st.text_input("Password", type="password")

#     if st.button("Login"):
#         login(email, password)
#         st.rerun()   # ← FIX: forces Streamlit to reload with authenticated session

#     st.stop()

# # if not user:
# #     st.title("Login to Calculus Portal")

# #     email = st.text_input("Email")
# #     password = st.text_input("Password", type="password")

# #     if st.button("Login"):
# #         login(email, password)

# #     st.page_link("pages/Signup.py", label="Create a new account")
# #     st.stop()

# student_id = user.user.id
# student_email = user.user.email


# # ---------------------------------------------------------
# # REGISTRATION CHECK
# # ---------------------------------------------------------
# student_exists = (
#     supabase.table("students")
#     .select("id")
#     .eq("id", student_id)
#     .execute()
# )

# if not student_exists.data:
#     st.error("You must complete registration before accessing lessons.")
#     st.page_link("pages/Register.py", label="Go to Registration")
#     st.stop()


# # ---------------------------------------------------------
# # SIDEBAR NAVIGATION
# # ---------------------------------------------------------
# st.sidebar.title("Navigation")

# st.sidebar.page_link("app.py", label="Today's Lesson")
# st.sidebar.page_link("pages/Student_Dashboard.py", label="Student Dashboard")
# st.sidebar.page_link("pages/Admin_Dashboard.py", label="Admin Dashboard")

# st.sidebar.markdown("---")
# st.sidebar.subheader("Week Overviews")
# for i in range(1, 16):
#     st.sidebar.page_link(f"pages/Week_{i:02d}.py", label=f"Week {i} Overview")

# st.sidebar.markdown("---")
# st.sidebar.subheader("Assignments")
# st.sidebar.page_link("pages/Assignments.py", label="Assignments & Quizzes")

# st.sidebar.markdown("---")
# st.sidebar.subheader("Visualizers")
# st.sidebar.page_link("pages/Visualizers_Limits.py", label="Limits")
# st.sidebar.page_link("pages/Visualizers_Derivatives.py", label="Derivatives")
# st.sidebar.page_link("pages/Visualizers_Integrals.py", label="Integrals")
# st.sidebar.page_link("pages/Visualizers_ODE.py", label="ODE")
# st.sidebar.page_link("pages/Visualizers_Multivariable.py", label="Multivariable")


# # ---------------------------------------------------------
# # JOINING DATE
# # ---------------------------------------------------------
# if "join_date" not in st.session_state:
#     st.session_state.join_date = date.today()

# join_date = st.session_state.join_date
# today = date.today()


# # ---------------------------------------------------------
# # SUNDAY SKIP
# # ---------------------------------------------------------
# if is_sunday(today):
#     st.title("Sunday – No Class")
#     st.info("Relax, revise lightly, or explore visualizations.")
#     st.stop()


# # ---------------------------------------------------------
# # DAY NUMBER → WEEK/DAY
# # ---------------------------------------------------------
# day_number = get_day_number(join_date, today)
# week, day = get_week_and_day(day_number)


# # ---------------------------------------------------------
# # LOAD CURRICULUM
# # ---------------------------------------------------------
# BASE_DIR = os.path.dirname(__file__)
# CURRICULUM_PATH = os.path.join(BASE_DIR, "data", "curriculum.json")

# with open(CURRICULUM_PATH, "r", encoding="utf-8") as f:
#     curriculum = json.load(f)

# topic = curriculum.get(f"Week {week}", {}).get(f"Day {day}", "No topic assigned")


# # ---------------------------------------------------------
# # MARK ATTENDANCE
# # ---------------------------------------------------------
# mark_attendance(student_id, "Present")


# # ---------------------------------------------------------
# # SAFE PROGRESS LOGGING
# # ---------------------------------------------------------
# existing_progress = (
#     supabase.table("student_progress")
#     .select("id")
#     .eq("student_id", student_id)
#     .eq("progress_date", str(today))
#     .execute()
# )


# # if not existing_progress.data:
# #     supabase.table("student_progress").insert({
# #         "student_id": student_id,
# #         "progress_date": str(today),
# #         "week_number": week,
# #         "day_number": day
# #     }).execute()


# # ---------------------------------------------------------
# # DISPLAY TODAY'S LESSON
# # ---------------------------------------------------------
# st.title(f"Week {week} – Day {day}")
# st.subheader(topic)

# st.success("Your attendance for today has been marked as **Present**.")
# st.info("Use the sidebar to explore dashboards, visualizers, and week overviews.")
