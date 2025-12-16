import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
import os
from supabase import create_client, Client
url: str = os.environ.get("db.babnnvuqximsunvrxyal.supabase.co")
key: str = os.environ.get("abbgC6AYLZevUZZl")
supabase: Client = create_client(url, key)

response = (
    supabase.table("User")
    .select("*")
    .execute()
)
st.write(response)
