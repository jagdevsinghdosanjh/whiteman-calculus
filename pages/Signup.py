import streamlit as st
from supabase_client import supabase

st.set_page_config(page_title="Create Account", layout="wide")
st.title("Create Your Account")

email = st.text_input("Email")
password = st.text_input("Password", type="password")

if st.button("Sign Up"):
    res = supabase.auth.sign_up({"email": email, "password": password})

    if res.user:
        st.success("Account created! Please log in.")
        st.page_link("app.py", label="Go to Login")
        st.stop()
    else:
        st.error("Signup failed. Please try again.")
