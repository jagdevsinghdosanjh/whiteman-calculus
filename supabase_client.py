from supabase import create_client, ClientOptions
import streamlit as st

SUPABASE_URL = st.secrets["SUPABASE_URL"]
SUPABASE_KEY = st.secrets["SUPABASE_KEY"]

# Correct schema configuration
options = ClientOptions(schema="calculus_portal")

supabase = create_client(
    SUPABASE_URL,
    SUPABASE_KEY,
    options=options
)

def login(email, password):
    return supabase.auth.sign_in_with_password(
        {"email": email, "password": password}
    )

def get_user():
    return supabase.auth.get_user()
