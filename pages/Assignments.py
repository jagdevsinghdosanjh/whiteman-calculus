import streamlit as st
import pandas as pd
from supabase_client import supabase
from datetime import datetime

st.set_page_config(page_title="Assignments & Quizzes", layout="wide")
st.title("Assignments & Quizzes")

# ---------------------------------------------------------
# AUTH CHECK
# ---------------------------------------------------------
user = supabase.auth.get_user()
if not user:
    st.error("You must be logged in.")
    st.stop()

student_id = user.user.id

# ---------------------------------------------------------
# LOAD ASSIGNMENTS
# ---------------------------------------------------------
assign_res = (
    supabase.table("assignments")
    .select("*")
    .order("created_at", desc=True)
    .execute()
)

assignments = assign_res.data or []

if not assignments:
    st.info("No assignments available yet.")
    st.stop()

assignment_map = {a["title"]: a for a in assignments}

choice = st.selectbox("Select an assignment", list(assignment_map.keys()))
assignment = assignment_map[choice]

st.subheader(assignment["title"])
st.write(assignment.get("description", ""))

# ---------------------------------------------------------
# LOAD QUESTIONS
# ---------------------------------------------------------
q_res = (
    supabase.table("questions")
    .select("*")
    .eq("assignment_id", assignment["id"])
    .execute()
)

questions = q_res.data or []

if not questions:
    st.info("No questions defined for this assignment.")
    st.stop()

answers = {}
st.markdown("### Questions")

# ---------------------------------------------------------
# RENDER QUESTIONS
# ---------------------------------------------------------
for q in questions:
    st.markdown(f"**Q{q['id']}**: {q['question_text']}")
    q_type = q["question_type"]

    if q_type == "MCQ":
        opts = q["options"] or []
        ans = st.radio("Choose an option", opts, key=f"q_{q['id']}")
    elif q_type == "NUMERIC":
        ans = st.number_input("Your answer", key=f"q_{q['id']}")
        ans = str(ans)
    else:
        ans = st.text_input("Your answer (expression)", key=f"q_{q['id']}")

    answers[q["id"]] = ans
    st.markdown("---")

# ---------------------------------------------------------
# SUBMIT ASSIGNMENT
# ---------------------------------------------------------
if st.button("Submit Assignment"):
    total_marks = 0
    max_marks = sum(q["max_marks"] for q in questions)

    sub_res = supabase.table("submissions").insert({
        "student_id": student_id,
        "assignment_id": assignment["id"],
        "total_marks_obtained": 0,
        "max_marks": max_marks
    }).execute()

    submission = sub_res.data[0]
    submission_id = submission["id"]

    items_payload = []

    for q in questions:
        qid = q["id"]
        correct = q["correct_answer"]
        given = str(answers.get(qid, "")).strip()
        q_type = q["question_type"]

        is_correct = False

        if q_type == "MCQ":
            is_correct = (given == correct)
        elif q_type == "NUMERIC":
            try:
                is_correct = (float(given) == float(correct))
            except Exception:
                is_correct = False
        else:
            is_correct = (given.replace(" ", "") == correct.replace(" ", ""))

        marks = q["max_marks"] if is_correct else 0
        total_marks += marks

        items_payload.append({
            "submission_id": submission_id,
            "question_id": qid,
            "student_answer": given,
            "is_correct": is_correct,
            "marks_obtained": marks
        })

    supabase.table("submission_items").insert(items_payload).execute()

    supabase.table("submissions").update({
        "total_marks_obtained": total_marks
    }).eq("id", submission_id).execute()

    st.success(f"Submitted! You scored {total_marks} / {max_marks}.")
