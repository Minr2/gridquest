import streamlit as st

st.title("GridQuest")
st.subheader("Select Difficulty")

if st.button("Beginner"):
    st.session_state.diff = "beginner"
    st.switch_page("app.py")

if st.button("Advanced"):
    st.session_state.diff = "advanced"
    st.switch_page("app.py")