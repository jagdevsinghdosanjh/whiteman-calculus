import streamlit as st
from datetime import date
from supabase_client import supabase, get_user

# ---------------------------------------------------------
# AUTH CHECK
# ---------------------------------------------------------
user = get_user()
if not user:
    st.error("Please log in before registering.")
    st.page_link("app.py", label="Go to Login")
    st.stop()

student_id = user.user.id
email = user.user.email

# ---------------------------------------------------------
# CHECK IF ALREADY REGISTERED
# ---------------------------------------------------------
existing = (
    supabase.table("students")
    .select("id")
    .eq("id", student_id)
    .execute()
)

if existing.data:
    st.success("You are already registered!")
    st.page_link("app.py", label="Go to Today's Lesson")
    st.stop()

# ---------------------------------------------------------
# REGISTRATION FORM
# ---------------------------------------------------------
st.title("Student Registration")

full_name = st.text_input("Full Name")

if st.button("Register"):
    supabase.table("students").insert({
        "id": student_id,
        "email": email,
        "full_name": full_name,
        "join_date": str(date.today())
    }).execute()

    st.success("Registration complete!")
    st.page_link("app.py", label="Go to Today's Lesson")
    st.stop()
