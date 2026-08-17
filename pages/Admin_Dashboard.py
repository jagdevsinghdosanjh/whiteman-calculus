import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import date, timedelta

from supabase_client import supabase


# ---------------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------------
st.set_page_config(page_title="Admin Analytics Dashboard", layout="wide")
st.title("Admin Analytics Dashboard")


# ---------------------------------------------------------
# AUTH CHECK
# ---------------------------------------------------------
user = supabase.auth.get_user()
if not user:
    st.error("You must be logged in.")
    st.stop()

admin_emails = st.secrets.get("ADMIN_EMAILS", "").split(",")

if user.user.email not in admin_emails:
    st.error("You are not authorized to view this page.")
    st.stop()


# ---------------------------------------------------------
# LOAD STUDENTS
# ---------------------------------------------------------
students_res = supabase.table("students").select("*").execute()
students_df = pd.DataFrame(students_res.data or [])

st.subheader("👥 Students Overview")
st.write(f"Total students: **{len(students_df)}**")

if not students_df.empty:
    st.dataframe(students_df[["full_name", "email", "join_date"]])


# ---------------------------------------------------------
# ATTENDANCE HEATMAP (Last 30 Days)
# ---------------------------------------------------------
st.markdown("## 📅 Attendance Heatmap (Last 30 Days)")

today = date.today()
start_date = today - timedelta(days=30)

# att_res = (
#     supabase.table("attendance")
#     .select("student_id,attendance_date,status,students(full_name)")
#     .gte("attendance_date", str(start_date))
#     .order("attendance_date", desc=False)
#     .execute()
# )
att_res = (
    supabase.table("attendance")
    .select("attendance_date, status, student_id, students(full_name)")
    .order("attendance_date", desc=False)
    .limit(30)
    .execute()
)

att_df = pd.DataFrame(att_res.data or [])

if not att_df.empty:
    # Flatten join
    att_df["full_name"] = att_df["students"].apply(
        lambda x: x["full_name"] if isinstance(x, dict) else None
    )

    att_df["attendance_date"] = pd.to_datetime(att_df["attendance_date"])
    att_df["status_numeric"] = att_df["status"].apply(lambda x: 1 if x == "Present" else 0)

    heatmap_df = att_df.pivot_table(
        index="full_name",
        columns="attendance_date",
        values="status_numeric",
        fill_value=0
    )

    fig = px.imshow(
        heatmap_df,
        aspect="auto",
        color_continuous_scale=["red", "green"],
        title="Attendance Heatmap (Green = Present, Red = Absent)"
    )
    st.plotly_chart(fig, use_container_width=True)
else:
    st.info("No attendance data available.")


# att_df = pd.DataFrame(att_res.data or [])

# if not att_df.empty:
#     att_df["attendance_date"] = pd.to_datetime(att_df["attendance_date"])
#     att_df["status_numeric"] = att_df["status"].apply(lambda x: 1 if x == "Present" else 0)

#     heatmap_df = att_df.pivot_table(
#         index="students.full_name",
#         columns="attendance_date",
#         values="status_numeric",
#         fill_value=0
#     )

#     fig = px.imshow(
#         heatmap_df,
#         aspect="auto",
#         color_continuous_scale=["red", "green"],
#         title="Attendance Heatmap (Green = Present, Red = Absent)"
#     )
#     st.plotly_chart(fig, use_container_width=True)
# else:
#     st.info("No attendance data available.")


# ---------------------------------------------------------
# WEEKLY PROGRESS DISTRIBUTION
# ---------------------------------------------------------
st.markdown("## 📊 Weekly Progress Distribution")

prog_res = (
    supabase.table("student_progress")
    .select("student_id,week_number,day_number,students(full_name)")
    .order("week_number", desc=False)
    .execute()
)
prog_res = (
    supabase.table("student_progress")
    .select("student_id,week_number,day_number,students(full_name)")
    .order("week_number", desc=False)
    .execute()
)
prog_df = pd.DataFrame(prog_res.data or [])

if not prog_df.empty:
    # Flatten join
    prog_df["full_name"] = prog_df["students"].apply(
        lambda x: x["full_name"] if isinstance(x, dict) else None
    )

    week_counts = prog_df.groupby(["full_name", "week_number"]).size().reset_index(name="days_completed")

    fig2 = px.bar(
        week_counts,
        x="week_number",
        y="days_completed",
        color="full_name",
        title="Days Completed Per Week (All Students)",
        text="days_completed"
    )
    st.plotly_chart(fig2, use_container_width=True)
else:
    st.info("No progress data available.")

# prog_df = pd.DataFrame(prog_res.data or [])

# if not prog_df.empty:
#     week_counts = prog_df.groupby(["students.full_name", "week_number"]).size().reset_index(name="days_completed")

#     fig2 = px.bar(
#         week_counts,
#         x="week_number",
#         y="days_completed",
#         color="students.full_name",
#         title="Days Completed Per Week (All Students)",
#         text="days_completed"
#     )
#     st.plotly_chart(fig2, use_container_width=True)
# else:
#     st.info("No progress data available.")


# ---------------------------------------------------------
# STUDENT COMPLETION STATUS
# ---------------------------------------------------------
st.markdown("## 🏁 Student Completion Status")
prog_df = pd.DataFrame(prog_res.data or [])

if not prog_df.empty:
    # Flatten join
    prog_df["full_name"] = prog_df["students"].apply(
        lambda x: x["full_name"] if isinstance(x, dict) else None
    )

    completion_df = prog_df.groupby("full_name").agg(
        total_days=("day_number", "max"),
        max_week=("week_number", "max")
    ).reset_index()

    fig3 = px.bar(
        completion_df,
        x="full_name",
        y="total_days",
        title="Total Days Completed (Per Student)",
        text="total_days"
    )
    st.plotly_chart(fig3, use_container_width=True)
else:
    st.info("No completion data available.")

# if not prog_df.empty:
#     completion_df = prog_df.groupby("students.full_name").agg(
#         total_days=("day_number", "max"),
#         max_week=("week_number", "max")
#     ).reset_index()

#     fig3 = px.bar(
#         completion_df,
#         x="students.full_name",
#         y="total_days",
#         title="Total Days Completed (Per Student)",
#         text="total_days"
#     )
#     st.plotly_chart(fig3, use_container_width=True)
# else:
#     st.info("No completion data available.")


# ---------------------------------------------------------
# PRESENT / ABSENT SUMMARY (Today)
# ---------------------------------------------------------
st.markdown("## 📌 Attendance Summary (Today)")

att_today = (
    supabase.table("attendance")
    .select("student_id,status,students(full_name)")
    .eq("attendance_date", str(today))
    .execute()
)

att_today_df = pd.DataFrame(att_today.data or [])

if not att_today_df.empty:
    present_count = (att_today_df["status"] == "Present").sum()
    absent_count = (att_today_df["status"] == "Absent").sum()

    st.write(f"**Present:** {present_count}")
    st.write(f"**Absent:** {absent_count}")

    fig4 = px.pie(
        att_today_df,
        names="status",
        title="Today's Attendance Split"
    )
    st.plotly_chart(fig4, use_container_width=True)
else:
    st.info("No attendance recorded today.")


# ---------------------------------------------------------
# RECENT ACTIVITY LOG
# ---------------------------------------------------------
st.markdown("## 📝 Recent Activity Log")

recent_prog = (
    supabase.table("student_progress")
    .select("progress_date,week_number,day_number,students(full_name)")
    .order("progress_date", desc=True)
    .limit(50)
    .execute()
)

recent_df = pd.DataFrame(recent_prog.data or [])

if not recent_df.empty:
    st.dataframe(recent_df)
else:
    st.info("No recent activity.")