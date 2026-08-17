import streamlit as st
import json
import os
from datetime import date
import plotly.express as px
import pandas as pd

from supabase_client import supabase
from utils.date_utils import get_day_number, get_week_and_day


BASE_DIR = os.path.dirname(os.path.dirname(__file__))
CURRICULUM_PATH = os.path.join(BASE_DIR, "data", "curriculum.json")


def load_curriculum():
    with open(CURRICULUM_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def get_student_record():
    user = supabase.auth.get_user()
    if not user:
        return None

    student_id = user.user.id
    res = supabase.table("students").select("*").eq("id", student_id).single().execute()
    return res.data


st.set_page_config(page_title="Student Dashboard", layout="wide")
st.title("Student Dashboard")

student = get_student_record()
if not student:
    st.error("No student record found.")
    st.stop()

full_name = student["full_name"]
join_date = date.fromisoformat(student["join_date"])

st.subheader(f"Welcome, {full_name}")
st.write(f"Joining date: **{join_date}**")

today = date.today()
day_number = get_day_number(join_date, today)
week_number, day_in_week = get_week_and_day(day_number)

curriculum = load_curriculum()
week_label = f"Week {week_number}"
topic = curriculum.get(week_label, {}).get(f"Day {day_in_week}", "No topic assigned")

st.markdown(f"### Today’s Topic")
st.write(topic)


# ---------------------------------------------------------
# Attendance Data
# ---------------------------------------------------------
att_res = (
    supabase.table("attendance")
    .select("attendance_date,status")
    .eq("student_id", student["id"])
    .order("attendance_date", desc=True)
    .limit(30)
    .execute()
)

attendance_df = pd.DataFrame(att_res.data or [])


# ---------------------------------------------------------
# Progress Data
# ---------------------------------------------------------
prog_res = (
    supabase.table("student_progress")
    .select("progress_date,week_number,day_number,day_in_week")
    .eq("student_id", student["id"])
    .order("progress_date", desc=False)
    .execute()
)

progress_df = pd.DataFrame(prog_res.data or [])


# ---------------------------------------------------------
# CHART 1 — Daily Progress Line Chart
# ---------------------------------------------------------
st.markdown("## 📈 Daily Progress")

if not progress_df.empty:
    fig = px.line(
        progress_df,
        x="progress_date",
        y="day_number",
        markers=True,
        title="Daily Learning Progress (Day Number Over Time)"
    )
    st.plotly_chart(fig, use_container_width=True)
else:
    st.info("No progress data available yet.")


# ---------------------------------------------------------
# CHART 2 — Week Completion Bar Chart
# ---------------------------------------------------------
st.markdown("## 📊 Week Completion Overview")

if not progress_df.empty:
    week_counts = progress_df.groupby("week_number").size().reset_index(name="days_completed")
    fig2 = px.bar(
        week_counts,
        x="week_number",
        y="days_completed",
        title="Days Completed Per Week",
        text="days_completed"
    )
    st.plotly_chart(fig2, use_container_width=True)
else:
    st.info("No weekly progress data available yet.")


# ---------------------------------------------------------
# CHART 3 — Attendance Streak Chart
# ---------------------------------------------------------
st.markdown("## 🔁 Attendance Streak")

if not attendance_df.empty:
    attendance_df["status_numeric"] = attendance_df["status"].apply(lambda x: 1 if x == "Present" else 0)
    fig3 = px.bar(
        attendance_df.sort_values("attendance_date"),
        x="attendance_date",
        y="status_numeric",
        title="Attendance Record (1 = Present, 0 = Absent)",
        color="status_numeric"
    )
    st.plotly_chart(fig3, use_container_width=True)
else:
    st.info("No attendance data available yet.")